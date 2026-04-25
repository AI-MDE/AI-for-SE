# Sample MDE Workspace

This folder shows the proposed `.mde/` artifact structure for a project using the MDE MCP server.

Since MCP is the integration surface, no `.ai/` folder is required in the sample project.

## Structure

```text
.mde/
  models/
  evidence/
  work-items/
  plans/
  context/
  approvals/
  reports/
  patches/
```

## Rule

`.mde/` contains project state, generated artifacts, plans, approvals, reports, and context used by MCP commands.

Skills and command behavior live in the MCP server/tools, not inside the sample project.
