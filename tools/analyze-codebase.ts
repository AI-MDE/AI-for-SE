import { Project, SyntaxKind } from "ts-morph";
import fs from "fs";
import path from "path";

const tsConfigFilePath = fs.existsSync("tsconfig.json") ? "tsconfig.json" : undefined;

const project = new Project(
  tsConfigFilePath
    ? { tsConfigFilePath }
    : { skipAddingFilesFromTsConfig: true }
);

if (!tsConfigFilePath) {
  project.addSourceFilesAtPaths(["src/**/*.ts", "test/**/*.ts"]);
}

type MethodMap = {
  name: string;
  params: { name: string; type: string }[];
  returnType: string;
  calls: string[];
};

type ArtifactMap = {
  file: string;
  artifactType: "class" | "function" | "interface" | "type";
  name: string;
  extends?: string;
  implements?: string[];
  methods?: MethodMap[];
  exports: string[];
  imports: string[];
};

const artifacts: ArtifactMap[] = [];

for (const sourceFile of project.getSourceFiles()) {
  const filePath = path.relative(process.cwd(), sourceFile.getFilePath());

  const imports = sourceFile.getImportDeclarations().map(i => i.getModuleSpecifierValue());
  const exports = sourceFile.getExportedDeclarations();

  for (const cls of sourceFile.getClasses()) {
    artifacts.push({
      file: filePath,
      artifactType: "class",
      name: cls.getName() ?? "<anonymous>",
      extends: cls.getExtends()?.getText(),
      implements: cls.getImplements().map(i => i.getText()),
      imports,
      exports: Array.from(exports.keys()),
      methods: cls.getMethods().map(m => ({
        name: m.getName(),
        params: m.getParameters().map(p => ({
          name: p.getName(),
          type: p.getType().getText()
        })),
        returnType: m.getReturnType().getText(),
        calls: m.getDescendantsOfKind(SyntaxKind.CallExpression)
          .map(c => c.getExpression().getText())
      }))
    });
  }

  for (const fn of sourceFile.getFunctions()) {
    artifacts.push({
      file: filePath,
      artifactType: "function",
      name: fn.getName() ?? "<anonymous>",
      imports,
      exports: Array.from(exports.keys())
    });
  }

  for (const intf of sourceFile.getInterfaces()) {
    artifacts.push({
      file: filePath,
      artifactType: "interface",
      name: intf.getName(),
      imports,
      exports: Array.from(exports.keys())
    });
  }

  for (const alias of sourceFile.getTypeAliases()) {
    artifacts.push({
      file: filePath,
      artifactType: "type",
      name: alias.getName(),
      imports,
      exports: Array.from(exports.keys())
    });
  }
}

const outputPath = ".ai/code-map.full.json";
fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, JSON.stringify({ generatedAt: new Date().toISOString(), artifacts }, null, 2));

console.log(`Wrote ${outputPath} with ${artifacts.length} artifacts.`);
