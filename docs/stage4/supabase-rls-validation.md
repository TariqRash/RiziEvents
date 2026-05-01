# Supabase Staging Environment and RLS Validation

**KAN-29 — Confirmed by: Ilyas (@illo888)**
**Sprint 0 | May 1, 2026**

## Environment Confirmation

| Item | Value |
|------|-------|
| Supabase project | rizi-staging |
| Region | eu-central-1 |
| Auth provider | Supabase Auth (email/password) |
| Storage | Supabase Storage (event assets) |

## Core Tables Confirmed

| Table | RLS enabled | Notes |
|-------|------------|-------|
| profiles | Yes | Read own row only |
| events | Yes | Organizer owns event rows |
| guests | Yes | Organizer sees guests for own events |
| check_ins | Yes | Linked to guest and event ownership |

## RLS Policy Summary

### events
- `SELECT`: public rows where `status = 'published'`; organizer sees own drafts
- `INSERT`: authenticated users only, `organizer_id = auth.uid()`
- `UPDATE`: organizer owns the row
- `DELETE`: organizer owns the row

### guests
- `SELECT`: organizer of the event or the guest themselves
- `INSERT`: open for published events (guest registration)
- `UPDATE`: organizer only (check-in status)

### check_ins
- `SELECT`: organizer of the parent event
- `INSERT`: organizer only

## Migration Status

All core migrations applied to staging. Schema matches Stage 3 ER diagram.

## Env Variables Confirmed

- `NEXT_PUBLIC_SUPABASE_URL` — set in Vercel staging environment
- `NEXT_PUBLIC_SUPABASE_ANON_KEY` — set in Vercel staging environment
- `SUPABASE_SERVICE_ROLE_KEY` — set as secret, not exposed to client

No secret values stored in this repository.
