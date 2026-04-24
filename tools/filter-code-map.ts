import fs from "fs";
import path from "path";

type Args = {
  entity?: string;
  operation?: string;
  artifactType?: string;
  depth?: string;
};

function parseArgs(argv: string[]): Args {
  const args: Args = {};
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i];
    const value = argv[i + 1];
    if (key === "--entity") args.entity = value;
    if (key === "--operation") args.operation = value;
    if (key === "--artifactType") args.artifactType = value;
    if (key === "--depth") args.depth = value;
  }
  return args;
}

const args = parseArgs(process.argv.slice(2));
const inputPath = ".ai/code-map.full.json";
const outputPath = ".ai/context/task.submap.json";
const filesPath = ".ai/context/task.files.txt";

if (!fs.existsSync(inputPath)) {
  throw new Error(`Missing ${inputPath}. Run npm run analyze first.`);
}

const map = JSON.parse(fs.readFileSync(inputPath, "utf8"));
const terms = [args.entity, args.operation].filter(Boolean).map(t => String(t).toLowerCase());

const artifacts = map.artifacts.filter((a: any) => {
  if (args.artifactType && a.artifactType !== args.artifactType) return false;

  if (terms.length === 0) return true;

  const haystack = JSON.stringify({
    file: a.file,
    name: a.name,
    methods: a.methods,
    imports: a.imports,
    exports: a.exports
  }).toLowerCase();

  return terms.some(term => haystack.includes(term));
});

fs.mkdirSync(path.dirname(outputPath), { recursive: true });
fs.writeFileSync(outputPath, JSON.stringify({ filter: args, artifacts }, null, 2));

const uniqueFiles = Array.from(new Set(artifacts.map((a: any) => a.file))).sort();
fs.writeFileSync(filesPath, uniqueFiles.join("\n"));

console.log(`Wrote ${outputPath} with ${artifacts.length} artifacts.`);
console.log(`Wrote ${filesPath} with ${uniqueFiles.length} files.`);
