# RiziEvents

RiziEvents is a lightweight event publishing and guest registration platform built by a four-member student team. The MVP covers the complete flow from organizer sign-up to guest check-in at the venue.

## Team

| Name | GitHub | Role |
| --- | --- | --- |
| Tariq Rashid | [@TariqRash](https://github.com/TariqRash) | Project lead, architecture and API design |
| Ilyas | [@illo888](https://github.com/illo888) | Database design and backend services |
| Oways | [@oways-work](https://github.com/oways-work) | Diagrams, sequence flows, and QA plan |
| Nawal Samer | [@Nawalsamer04](https://github.com/Nawalsamer04) | Technical documentation and deliverables |

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

### Out of scope for this MVP

- Online payment gateways
- Premium plans and monetization
- Custom domains and event subdomains
- White-labeling
- Public developer API
- Advanced analytics
- Modules marketplace
- Large-team administration features

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
└── src
    └── README.md
```

## Core User Flows

1. Organizer creates an account and signs in.
2. Organizer creates an event with title, dates, venue, capacity, and branding.
3. Organizer publishes the event.
4. A guest opens `https://www.rizi.app/e/[slug]`.
5. The guest submits a registration form.
6. The organizer views the guest list and checks in attendees offline at the venue.

## Simplified Domain Model

The MVP documentation is based on these core entities:

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

