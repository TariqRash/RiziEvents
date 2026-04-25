# API Specification

## External APIs

### Google Maps API and Places SDK

- Purpose: venue search, address lookup, place selection, and directions support.
- Why chosen: reliable place data, familiar map experience, and direct support for venue-based event workflows.
- Usage in MVP:
  - Organizer chooses a venue during event setup.
  - Event page can expose map and directions information for guests.

## Internal API Endpoints

## `POST /api/auth/register`

- Purpose: create a new organizer account.
- Auth required: No.
- Input format: JSON.
- Request body:
  - `name`
  - `email`
  - `password`
- Success response:
  - `userId`
  - `email`
  - `createdAt`

## `POST /api/auth/login`

- Purpose: authenticate an organizer and start a session.
- Auth required: No.
- Input format: JSON.
- Request body:
  - `email`
  - `password`
- Success response:
  - `accessToken` or session cookie
  - `user`

## `POST /api/events`

- Purpose: create a new event draft.
- Auth required: Organizer session.
- Input format: JSON.
- Request body:
  - `title`
  - `description`
  - `startDate`
  - `endDate`
  - `venue`
  - `capacity`
  - `brandConfig`
- Success response:
  - `eventId`
  - `slug`
  - `status`

## `GET /api/events`

- Purpose: list the authenticated organizer's events.
- Auth required: Organizer session.
- Input format: Query string optional.
- Success response:
  - `items`
  - `total`

## `GET /api/events/{eventId}`

- Purpose: fetch one organizer-owned event for management screens.
- Auth required: Organizer session.
- Input format: Path parameter.
- Success response:
  - `id`
  - `slug`
  - `title`
  - `status`
  - `venue`
  - `capacity`
  - `guestCounts`

## `PATCH /api/events/{eventId}`

- Purpose: update an event draft or editable event fields.
- Auth required: Organizer session.
- Input format: JSON.
- Request body:
  - any editable subset of event fields
- Success response:
  - `id`
  - `updatedAt`
  - `status`

## `POST /api/events/{eventId}/publish`

- Purpose: publish an event and make the public page available.
- Auth required: Organizer session.
- Input format: Path parameter.
- Success response:
  - `id`
  - `slug`
  - `status`
  - `publicUrl`

## `GET /api/public/events/{slug}`

- Purpose: fetch the public event data shown on `/e/[slug]`.
- Auth required: No.
- Input format: Path parameter.
- Success response:
  - `slug`
  - `title`
  - `description`
  - `startDate`
  - `endDate`
  - `venue`
  - `agenda`
  - `speakers`
  - `registrationOpen`

## `POST /api/guests/register`

- Purpose: register a guest for a published event.
- Auth required: No.
- Input format: JSON.
- Request body:
  - `eventId`
  - `fullName`
  - `email`
  - `phone`
- Success response:
  - `guestId`
  - `status`
  - `message`

## `GET /api/events/{eventId}/guests`

- Purpose: list registered guests for organizer operations.
- Auth required: Organizer session.
- Input format: Path parameter with optional search filters.
- Success response:
  - `items`
  - `total`
  - `counts`

## `POST /api/guests/{guestId}/checkin`

- Purpose: mark a registered guest as checked in at the venue.
- Auth required: Organizer session.
- Input format: Path parameter.
- Success response:
  - `guestId`
  - `status`
  - `checkedInAt`

## Common Response Notes

- All API responses are JSON.
- Validation errors return a client error status and a readable error message.
- Authorization failures return an unauthorized or forbidden status.
- Public endpoints expose only published event information.
