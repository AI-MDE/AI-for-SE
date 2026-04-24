import fs from "fs";

const requiredFiles = [
  ".ai/architecture.md",
  ".ai/app.config.json",
  ".ai/project-patterns.md",
  ".ai/skills/add-command.md",
  ".ai/skills/fix-bug.md",
  ".ai/skills/extract-project-patterns.md",
  ".ai/skills/integrate-existing-code.md",
  "specs/micro-spec.template.md"
];

console.log("AI-MDE-Light project initiation check\n");

let ok = true;

for (const file of requiredFiles) {
  if (fs.existsSync(file)) {
    console.log(`OK      ${file}`);
  } else {
    console.error(`MISSING ${file}`);
    ok = false;
  }
}

console.log("\nNext steps:");
console.log("1. Run: npm run analyze");
console.log("2. Ask AI to use .ai/skills/extract-project-patterns.md");
console.log("3. Review and normalize .ai/project-patterns.md");
console.log("4. Use specs/micro-spec.template.md for the first change request");

if (!ok) {
  process.exit(1);
}
