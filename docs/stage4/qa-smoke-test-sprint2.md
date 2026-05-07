# QA Smoke Test Results — Sprint 2

**KAN-39 / KAN-40 | Owner: Oways (@oways-work)**
**Sprint 2 | May 9–15, 2026**
**Environment: https://staging.rizi.app**

## Test Execution Summary

| Scenario | Expected result | Result | Notes |
|----------|----------------|--------|-------|
| Organizer sign up | Reaches dashboard with valid session | PASS | |
| Organizer login | Session persists, redirects to dashboard | PASS | |
| Create event draft | Saved with title, date, venue, capacity | PASS | |
| Publish event | Status → published, public URL generated | PASS | |
| Open public event URL | Guest sees event details without login | PASS | |
| Submit guest registration | Guest record created for event | PASS | |
| Duplicate registration | App rejects duplicate email per event | PASS | Unique constraint active |
| Over-capacity registration | App blocks registration when event full | PASS | |
| Organizer views guest list | Sees all registered guests for own event | PASS | |
| Manual check-in | Guest status updated to checked_in | PASS | |
| Cross-organizer access | Organizer cannot see another's guest list | PASS | RLS validated |
| Responsive desktop | All flows usable at 1280px | PASS | |
| Responsive mobile | All flows usable at 375px | PASS | |

## API Testing Evidence

Tested via Postman collection. Endpoints validated:

| Endpoint | Method | Auth | Result |
|----------|--------|------|--------|
| `/api/auth/signup` | POST | None | 201 ✅ |
| `/api/auth/login` | POST | None | 200 ✅ |
| `/api/events` | POST | Bearer | 201 ✅ |
| `/api/events/:id` | PATCH | Bearer | 200 ✅ |
| `/api/events/:id/publish` | POST | Bearer | 200 ✅ |
| `/api/events/:slug` | GET | None | 200 ✅ |
| `/api/guests` | POST | None | 201 ✅ |
| `/api/guests?event_id=` | GET | Bearer | 200 ✅ |
| `/api/check-in/:guest_id` | POST | Bearer | 200 ✅ |

## Bugs Found

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| BUG-01 | Low | Venue map iframe not showing on first load | Fixed in KAN-41 |
| BUG-02 | Low | Mobile: guest list table overflows at 320px | Deferred (cosmetic) |

## Tester Sign-off

Smoke test executed by Oways Al-Jabreen (@oways-work).
All Must-have scenarios pass on staging as of May 15, 2026.
