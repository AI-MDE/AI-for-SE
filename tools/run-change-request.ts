import fs from "fs";

const required = [
  "specs/micro-spec.template.md",
  ".ai/context/task.submap.json"
];

console.log("Running AI-MDE-Light change request pipeline\n");

for (const file of required) {
  if (!fs.existsSync(file)) {
    console.error(`Missing required file: ${file}`);
    process.exit(1);
  }
}

console.log("Step 1: Micro-spec present");
console.log("Step 2: Code-map filtered (task.submap.json exists)");
console.log("Step 3: Ready for AI execution with selected skill");
console.log("Step 4: After AI edits, run validation:");
console.log("        npm run build");
console.log("        npm test");
console.log("        npm run validate-task");

console.log("\nPipeline ready.");
