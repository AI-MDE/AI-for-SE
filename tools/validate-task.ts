import fs from "fs";

const requiredFiles = [
  ".ai/architecture.md",
  ".ai/app.config.json",
  ".ai/project-patterns.md",
  ".ai/context/task.submap.json"
];

let ok = true;

for (const file of requiredFiles) {
  if (!fs.existsSync(file)) {
    console.error(`Missing required file: ${file}`);
    ok = false;
  }
}

if (!ok) {
  process.exit(1);
}

console.log("Task context validation passed.");
