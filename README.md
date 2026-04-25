# RiziEvents

RiziEvents is a reduced MVP for the Holberton phase-three technical documentation review. This repository intentionally reflects the simplified product baseline, not the larger experimental codebase used earlier in development.

The MVP positions Rizi as a lightweight event publishing and guest registration platform built for a small student team. Organizers can create and publish an event, guests can open a public event page under `/e/[slug]`, register, and be checked in manually on-site.

## URLs

- Canonical production URL: [https://www.rizi.app](https://www.rizi.app)
- Production apex redirect: [https://rizi.app](https://rizi.app)
- Staging target for team validation: [https://staging.rizi.app](https://staging.rizi.app)
- Public event route model: `https://www.rizi.app/e/[slug]`

## MVP Scope

### In scope

- Organizer sign up and sign in
- Event creation and publishing
- Public event landing page
- Guest registration
- Guest list management
- Offline/manual check-in
- Google Maps API and Places SDK for venue selection and directions

### Out of scope for the Holberton MVP

- Online payment gateways
- Premium plans and monetization
- Custom domains and event subdomains
- White-labeling
- Public developer API
- Advanced analytics
- Modules marketplace
- Large-team administration features
- AI-assisted content generation in the formal project scope

## Architecture Summary

- Frontend: Next.js deployed on Vercel
- Backend platform: Supabase Auth, Postgres, Storage, and Row Level Security
- External integration: Google Maps API and Places SDK
- Environments: Production and staging

## Repository Layout

```text
.
├── README.md
├── docs
│   ├── technical-documentation.md
│   ├── diagrams.md
│   ├── api-spec.md
│   ├── scm-qa-plan.md
│   ├── technical-justifications.md
│   └── diagrams
│       ├── system-architecture.mmd
│       ├── class-diagram.mmd
│       ├── database-er.mmd
│       ├── sequence-organizer-auth.mmd
│       ├── sequence-create-publish.mmd
│       ├── sequence-guest-registration.mmd
│       └── sequence-offline-checkin.mmd
├── deliverables
│   └── RiziEvents-Technical-Documentation.docx
```

## Core User Flows

1. Organizer creates an account and signs in.
2. Organizer creates an event with title, dates, venue, capacity, and branding.
3. Organizer publishes the event.
4. A guest opens `https://www.rizi.app/e/[slug]`.
5. The guest submits a registration form.
6. The organizer views the guest list and checks in attendees offline at the venue.

## Simplified Domain Model

The reduced MVP documentation is based on these core entities:

- `users`
- `events`
- `guests`
- `agenda_items`
- `speakers`

All accounts are treated under a single free MVP tier in this phase. No billing or payment logic is part of the documented baseline.

## Deliverables

- Main technical document: [docs/technical-documentation.md](docs/technical-documentation.md)
- Combined diagrams page: [docs/diagrams.md](docs/diagrams.md)
- API specification: [docs/api-spec.md](docs/api-spec.md)
- SCM and QA plan: [docs/scm-qa-plan.md](docs/scm-qa-plan.md)
- Technical justifications: [docs/technical-justifications.md](docs/technical-justifications.md)
- Submission file: [deliverables/RiziEvents-Technical-Documentation.docx](deliverables/RiziEvents-Technical-Documentation.docx)

## Diagram Rendering Note

The Mermaid diagrams are stored both as standalone `.mmd` source files in `docs/diagrams/` and embedded directly inside [docs/technical-documentation.md](docs/technical-documentation.md) so they render on GitHub.
