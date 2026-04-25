# Technical Justifications

## Supabase

Supabase is justified for this MVP because it reduces backend setup time while still providing the core services required by the product. The team needs authentication, a relational database, and practical access control without spending the project budget and schedule on custom infrastructure.

### Reasons

- Built-in authentication for organizer accounts
- Managed Postgres for structured event and guest data
- Row Level Security to protect organizer-owned records
- Fast setup for a small student team
- Lower operational overhead than building and hosting a custom backend stack from scratch

## Vercel

Vercel is justified because the documented frontend is based on Next.js and the team needs fast deployment, preview capability, and a simple path for staging and production environments.

### Reasons

- Strong fit for Next.js deployment
- Fast iteration and redeployment
- Suitable workflow for staging and production
- Easy preview-style validation during development
- Minimal platform overhead for a small team

## Google Maps API and Places SDK

Google Maps is justified as the only core external integration in the MVP because event products depend on clear venue information. The team needs a reliable way to let organizers choose a location and help guests navigate to it.

### Reasons

- Accurate place search and structured venue data
- Familiar guest experience for directions
- Practical venue workflow for event creation
- Supports address, place identifier, and coordinates for future enhancement

## Offline Payment Decision

The project intentionally excludes online payment gateways from the MVP. This is a scope-control decision, not a product limitation statement for the long term.

### Reasons

- Payment integration would add security, compliance, and testing overhead
- The current team size is small and time-constrained
- The academic deliverable can be defended without commercial payment flows
- Offline/manual payment handling is enough for the MVP phase

## Reduced Scope Decision

The team chose a focused MVP scope to deliver a complete, well-documented product within the project timeline.

### Reasons

- The team consists of four members, most of them students
- A smaller MVP is more likely to be completed, explained, and validated
- A reduced architecture is easier to document clearly
- Simpler scope improves demo readiness and lowers delivery risk

## Path-Based Event URLs

The documentation standardizes on `https://www.rizi.app/e/[slug]` instead of custom domains or subdomains.

### Reasons

- Easier routing model for the MVP
- Lower operational complexity
- No dependency on custom DNS configuration
- Easier to document, test, and present

