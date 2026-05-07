# Sprint 1 Review Notes

**KAN-42 | Sprint 1 | May 2–8, 2026**
**Prepared by: Tariq (@TariqRash)**

## Completed Tasks

| Jira | Summary | Status |
|------|---------|--------|
| KAN-30 | Organizer can register and log in | Done |
| KAN-31 | Organizer can create and edit an event | Done |
| KAN-32 | Organizer can publish an event to a public URL | Done |
| KAN-33 | Guest can open public event page | Done |

## Demo Scope

- Organizer sign-up and login via Supabase Auth on https://staging.rizi.app
- Event creation form: title, date, venue, capacity, description
- Event publish flow: draft → published with public slug route
- Public event page: guest can open `/events/[slug]` without authentication

## Staging Evidence

- Staging URL: https://staging.rizi.app
- All Sprint 1 Must-have stories pass on staging
- Auth session persists across page reload

## Blockers and Risks

- None critical. Google Maps key needed for venue display (Sprint 2, KAN-37)

## Follow-up Tasks

- KAN-34: Guest registration moves to Sprint 2 as planned
- Capacity enforcement edge case deferred to Sprint 2 QA

## Merged PRs

- `feature/KAN-30-organizer-auth` → staging ✅
- `feature/KAN-31-event-create-edit` → staging ✅
- `feature/KAN-32-event-publish` → staging ✅
- `feature/KAN-33-public-event-page` → staging ✅
