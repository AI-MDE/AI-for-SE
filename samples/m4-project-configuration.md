# M4. Project Configuration — Sample

## Technology Stack

| Layer | Technology |
|---|---|
| Language | TypeScript |
| Runtime | Node.js |
| Server framework | Express |
| Database | PostgreSQL |
| ORM / Query | Raw SQL with typed mappers |
| Testing | Jest |
| UI | Pug templates (server-rendered) |
| Build | tsc + tsx for dev |

---

## Folder Structure

```
APP/
  src/
    server/
      shared/                    # Cross-cutting utilities
        context-object.ts
        logger.ts
        service-base.ts
        generate-id.ts
      {module}/                  # One folder per subject module
        controller/
          {entity}.controller.ts
        service/
          {entity}.service.ts
        query_service/
          {entity}.query-service.ts
        domain/
          {entity}.entity.ts
        data_access/
          {entity}.repository.interface.ts
          {entity}.repository.ts
          {entity}.mapper.ts
        dto/
          {action}-{entity}.command.ts
          {entity}.response.dto.ts
          {entity}-read.dto.ts
        validators/
          {entity}.access-control.ts
          {entity}.state-transition.ts
          {entity}.business-rules.ts
        index.ts
    ui/
      src/
        {module}/
          pages/
            {page-name}.tsx
          routes.ts
          index.ts
  views/                         # Pug templates
    {module}/
      {page}.pug
  public/                        # Static assets
  output/
    trace/                       # Generated trace maps
  test/
    {module}/
      {entity}.test.ts

design/
  entities/                      # Entity specifications
    ent-{entity}.json
  subjects/                      # Subject specifications
    {subject}/
      subject.json
  ui/                            # UI specifications
    {subject}/
      ui.json
```

---

## Environment

| Variable | Purpose | Example |
|---|---|---|
| DATABASE_URL | PostgreSQL connection string | `postgresql://localhost:5432/hr2` |
| PORT | HTTP server port | `3000` |
| NODE_ENV | Runtime environment | `development` |

---

## Commands

| Command | Purpose |
|---|---|
| `npm run dev` | Start dev server with hot reload |
| `npm run build` | Compile TypeScript |
| `npm run test` | Run Jest test suite |
| `npm run seed` | Load seed data |
| `npm run analyze` | Generate code map |
