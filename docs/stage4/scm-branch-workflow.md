# GitHub SCM Branch Workflow and PR Rules

**KAN-27 — Confirmed by: Oways (@oways-work)**
**Sprint 0 | May 1, 2026**

## Branch Strategy

| Branch type | Naming pattern | Target | Purpose |
|-------------|---------------|--------|---------|
| Feature | `feature/KAN-XX-short-name` | `staging` | New functionality |
| Fix | `fix/KAN-XX-short-name` | `staging` | Bug resolution |
| Docs | `docs/KAN-XX-short-name` | `main` | Documentation only |

## Active Branches (Sprint 0)

- `staging` — integration branch, maps to https://staging.rizi.app
- `main` — production branch, maps to https://www.rizi.app

## Pull Request Rules

1. Every PR must reference its Jira issue key in the title (e.g. `[KAN-31] Add event creation form`)
2. PR description must include: summary of changes, testing steps, and staging validation link
3. Minimum one reviewer approval before merge into `staging`
4. SCM (Oways) verifies branch scope and build status before approving
5. `main` is updated only after sprint review, QA evidence, and staging validation pass

## Vercel Staging Confirmation

- Vercel project: `rizi-staging`
- Branch mapping: `staging` → https://staging.rizi.app
- Build command: `next build`
- Environment variables confirmed in Vercel dashboard (KAN-28)

## Workflow Diagram

```
feature/KAN-XX  →  PR review (SCM)  →  staging  →  sprint review + QA  →  main
```

## Merge Checklist

- [ ] Jira issue key in PR title
- [ ] Changes summary in PR body
- [ ] Staging preview URL included
- [ ] At least one approval
- [ ] No failing build checks
