# API Specification

## Canonical URLs

- Canonical production URL: `https://www.rizi.app`
- Production apex redirect: `https://rizi.app`
- Staging URL: `https://staging.rizi.app`
- Public event page format: `https://www.rizi.app/e/{slug}`

## External Services

### Supabase Platform Services

- Purpose: organizer authentication, relational data storage, and access control.
- Why chosen: rapid MVP setup with managed authentication, Postgres, and Row Level Security.
- Project usage:
  - Organizer registration and login
  - Event, guest, agenda, and speaker storage
  - Access rules for organizer-owned data

### Google Maps API and Places SDK

- Purpose: venue search, address lookup, place selection, and directions support.
- Why chosen: reliable place data, familiar map experience, and direct support for venue-based event workflows.
- Project usage:
  - Organizer chooses a venue during event setup
  - The system stores `place_id`, address, latitude, and longitude
  - Guests receive map and directions support on the public event page

## Internal API Standards

- Content type: `application/json`
- Authentication: organizer endpoints require a valid organizer session
- Success formats: JSON objects or arrays
- Error format example:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The event title is required."
  }
}
```

## `POST /api/auth/register`

- Purpose: create a new organizer account
- Auth required: No
- Input: JSON body

### Example request

```json
{
  "name": "Tariq Rashid",
  "email": "tariq@example.com",
  "password": "StrongPassword123!"
}
```

### Example success response

Status: `201 Created`

```json
{
  "userId": "5b1a9b62-5c42-4e53-a93b-0cb81d0a28d1",
  "email": "tariq@example.com",
  "createdAt": "2026-04-25T14:40:00Z"
}
```

### Status codes

- `201 Created` account created
- `400 Bad Request` invalid payload
- `409 Conflict` email already exists

## `POST /api/auth/login`

- Purpose: authenticate an organizer and start a session
- Auth required: No
- Input: JSON body

### Example request

```json
{
  "email": "tariq@example.com",
  "password": "StrongPassword123!"
}
```

### Example success response

Status: `200 OK`

```json
{
  "accessToken": "session-or-jwt-token",
  "user": {
    "id": "5b1a9b62-5c42-4e53-a93b-0cb81d0a28d1",
    "name": "Tariq Rashid",
    "email": "tariq@example.com"
  }
}
```

### Status codes

- `200 OK` authenticated
- `400 Bad Request` missing credentials
- `401 Unauthorized` invalid email or password

## `POST /api/events`

- Purpose: create a new event draft
- Auth required: Organizer session
- Input: JSON body

### Example request

```json
{
  "title": "Health Exhibition 2026",
  "description": "A focused health and innovation exhibition for students and startups.",
  "startDate": "2026-06-12T10:00:00Z",
  "endDate": "2026-06-12T18:00:00Z",
  "venue": {
    "name": "Riyadh Front Hall A",
    "address": "Riyadh Front, Riyadh, Saudi Arabia",
    "city": "Riyadh",
    "placeId": "ChIJExamplePlaceId123",
    "latitude": 24.7786,
    "longitude": 46.7386
  },
  "capacity": 500,
  "brandConfig": {
    "primaryColor": "#0F766E"
  }
}
```

### Example success response

Status: `201 Created`

```json
{
  "eventId": "a9bc6b0d-e06d-49c9-944a-1fc0d9ec7e37",
  "slug": "health-exhibition-2026",
  "status": "draft"
}
```

### Status codes

- `201 Created` event draft created
- `400 Bad Request` invalid payload
- `401 Unauthorized` organizer not authenticated

## `GET /api/events`

- Purpose: list the authenticated organizer's events
- Auth required: Organizer session
- Input: optional query parameters

### Optional query parameters

- `status`
- `page`
- `pageSize`

### Example request

`GET /api/events?status=published&page=1&pageSize=10`

### Example success response

Status: `200 OK`

```json
{
  "items": [
    {
      "id": "a9bc6b0d-e06d-49c9-944a-1fc0d9ec7e37",
      "title": "Health Exhibition 2026",
      "slug": "health-exhibition-2026",
      "status": "published"
    }
  ],
  "total": 1
}
```

### Status codes

- `200 OK` events returned
- `401 Unauthorized` organizer not authenticated

## `GET /api/events/{eventId}`

- Purpose: fetch one organizer-owned event for management screens
- Auth required: Organizer session
- Input: path parameter

### Example success response

Status: `200 OK`

```json
{
  "id": "a9bc6b0d-e06d-49c9-944a-1fc0d9ec7e37",
  "slug": "health-exhibition-2026",
  "title": "Health Exhibition 2026",
  "status": "draft",
  "venue": {
    "name": "Riyadh Front Hall A",
    "city": "Riyadh"
  },
  "capacity": 500,
  "guestCounts": {
    "registered": 0,
    "checkedIn": 0
  }
}
```

### Status codes

- `200 OK` event found
- `401 Unauthorized` organizer not authenticated
- `404 Not Found` event not found or not owned by organizer

## `PATCH /api/events/{eventId}`

- Purpose: update an event draft or editable event fields
- Auth required: Organizer session
- Input: JSON body with any editable subset of fields

### Example request

```json
{
  "description": "Updated event description.",
  "agenda": [
    {
      "title": "Opening Session",
      "startTime": "2026-06-12T10:30:00Z",
      "endTime": "2026-06-12T11:00:00Z"
    }
  ],
  "speakers": [
    {
      "fullName": "Dr. Noura Al-Harbi",
      "jobTitle": "Healthcare Innovation Lead"
    }
  ]
}
```

### Example success response

Status: `200 OK`

```json
{
  "id": "a9bc6b0d-e06d-49c9-944a-1fc0d9ec7e37",
  "updatedAt": "2026-04-25T15:20:00Z",
  "status": "draft"
}
```

### Status codes

- `200 OK` event updated
- `400 Bad Request` invalid payload
- `401 Unauthorized` organizer not authenticated
- `404 Not Found` event not found

## `POST /api/events/{eventId}/publish`

- Purpose: publish an event and make the public page available
- Auth required: Organizer session
- Input: path parameter

### Example success response

Status: `200 OK`

```json
{
  "id": "a9bc6b0d-e06d-49c9-944a-1fc0d9ec7e37",
  "slug": "health-exhibition-2026",
  "status": "published",
  "publicUrl": "https://www.rizi.app/e/health-exhibition-2026"
}
```

### Status codes

- `200 OK` event published
- `400 Bad Request` event missing required publish fields
- `401 Unauthorized` organizer not authenticated
- `404 Not Found` event not found

## `GET /api/public/events/{slug}`

- Purpose: fetch the public event data shown on `/e/{slug}`
- Auth required: No
- Input: path parameter

### Example success response

Status: `200 OK`

```json
{
  "slug": "health-exhibition-2026",
  "title": "Health Exhibition 2026",
  "description": "A focused health and innovation exhibition for students and startups.",
  "startDate": "2026-06-12T10:00:00Z",
  "endDate": "2026-06-12T18:00:00Z",
  "venue": {
    "name": "Riyadh Front Hall A",
    "address": "Riyadh Front, Riyadh, Saudi Arabia",
    "city": "Riyadh",
    "directionsUrl": "https://maps.google.com/..."
  },
  "agenda": [],
  "speakers": [],
  "registrationOpen": true
}
```

### Status codes

- `200 OK` event returned
- `404 Not Found` slug not found or event not published

## `POST /api/guests/register`

- Purpose: register a guest for a published event
- Auth required: No
- Input: JSON body

### Example request

```json
{
  "eventId": "a9bc6b0d-e06d-49c9-944a-1fc0d9ec7e37",
  "fullName": "Sara Ahmed",
  "email": "sara@example.com",
  "phone": "+966500000000"
}
```

### Example success response

Status: `201 Created`

```json
{
  "guestId": "c06828fc-bf5c-450f-bb4f-3e40cad1fc25",
  "status": "registered",
  "message": "Registration completed successfully."
}
```

### Status codes

- `201 Created` guest registered
- `400 Bad Request` invalid payload
- `404 Not Found` event not found
- `409 Conflict` duplicate registration detected

## `GET /api/events/{eventId}/guests`

- Purpose: list registered guests for organizer operations
- Auth required: Organizer session
- Input: path parameter with optional filters

### Optional query parameters

- `search`
- `status`
- `page`
- `pageSize`

### Example request

`GET /api/events/{eventId}/guests?search=sara&status=registered&page=1&pageSize=25`

### Example success response

Status: `200 OK`

```json
{
  "items": [
    {
      "guestId": "c06828fc-bf5c-450f-bb4f-3e40cad1fc25",
      "fullName": "Sara Ahmed",
      "email": "sara@example.com",
      "status": "registered",
      "checkedInAt": null
    }
  ],
  "total": 1,
  "counts": {
    "registered": 1,
    "checkedIn": 0
  }
}
```

### Status codes

- `200 OK` guest list returned
- `401 Unauthorized` organizer not authenticated
- `404 Not Found` event not found

## `POST /api/guests/{guestId}/checkin`

- Purpose: mark a registered guest as checked in at the venue
- Auth required: Organizer session
- Input: path parameter

### Example success response

Status: `200 OK`

```json
{
  "guestId": "c06828fc-bf5c-450f-bb4f-3e40cad1fc25",
  "status": "checked_in",
  "checkedInAt": "2026-06-12T09:58:00Z"
}
```

### Status codes

- `200 OK` guest checked in
- `401 Unauthorized` organizer not authenticated
- `404 Not Found` guest not found
- `409 Conflict` guest already checked in

## Out of Scope Endpoints

The current MVP excludes:

- online payment endpoints
- subscription or paid-plan endpoints
- custom-domain management endpoints
- advanced analytics endpoints
