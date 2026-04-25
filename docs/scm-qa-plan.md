# SCM and QA Plan

## Source Control Management

### Branching model

- `main` is the protected branch and represents the stable project state.
- Every new task uses a short-lived feature branch named after the task, such as `feature/event-publish-flow` or `docs/api-spec`.
- Hotfixes can use a dedicated `hotfix/*` branch if a production issue appears.

### Pull request process

- Open a pull request for every branch before merging to `main`.
- At least one teammate reviews the pull request.
- The author addresses comments before merge.
- Pull requests should stay focused on one change set.

### Commit strategy

- Commit frequently with small, task-based commits.
- Use clear messages such as `Add guest registration API spec` or `Update reduced MVP architecture diagram`.
- Avoid mixing unrelated documentation and code changes in the same commit when possible.

### Team workflow for a four-member student team

- One person owns the current documentation baseline.
- One person validates diagrams and architecture consistency.
- One person checks API and database sections.
- One person verifies language, formatting, and submission readiness.

## Quality Assurance

### Testing strategy

- Prioritize manual smoke testing for the main MVP flows.
- Add targeted unit or component tests where they provide clear value without slowing the team down.
- Validate staging before any production-facing update.

### Core smoke-test scenarios

- Organizer can register and log in.
- Organizer can create an event draft.
- Organizer can publish the event and receive a valid slug route.
- Guest can open the public event page.
- Guest can submit the registration form successfully.
- Organizer can view the guest list.
- Organizer can mark a guest as checked in offline.

### Test types

- Unit tests
  - utility helpers
  - payload validation
  - service logic around event publishing and guest registration
- Integration tests
  - API endpoint request and response behavior
  - database writes for event and guest flows
- Manual UI tests
  - public event page
  - event creation form
  - guest registration form
  - guest list and check-in screen

### Suggested tools

- Framework/unit testing: Jest or Vitest
- API testing: Postman or Bruno
- Manual browser validation: Chrome or Edge
- Deployment verification: Vercel preview or staging deployment

## Deployment Validation

### Environments

- Production: `https://www.rizi.app`
- Staging: `https://staging.rizi.app`

### Release checks

- Confirm the correct environment variables are configured.
- Confirm the build succeeds on Vercel.
- Confirm the main public route and at least one event slug route load successfully.
- Confirm guest registration works in staging before promoting any release process to production.

## Definition of Done for This Phase

- Documentation files are complete and internally consistent.
- Mermaid diagrams match the written architecture and API flows.
- The submission `.docx` is generated and readable.
- The repository reflects the reduced MVP scope and does not present out-of-scope platform features as current deliverables.
