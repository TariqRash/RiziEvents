# RiziEvents Technical Documentation

## 1. Project Summary

RiziEvents is a reduced MVP for event publishing and registration. The documented product scope is intentionally limited to the features needed for a phase-three academic review and for a small four-member student team.

The platform allows an organizer to sign in, create an event, publish it under a slug-based public URL, accept guest registrations, and manage offline check-in at the venue. The official MVP architecture uses Next.js on Vercel for the web application and Supabase for authentication, database, and backend platform services.

### Official URLs

- Main application: `https://rizi.app`
- Staging environment: `https://staging.rizi.app`
- Public event page pattern: `https://rizi.app/e/[slug]`

## 2. MVP Scope

### In scope

- Organizer authentication
- Event creation and editing
- Event publishing
- Public event landing page
- Guest registration
- Guest list viewing
- Offline/manual guest check-in
- Venue location selection using Google Maps API and Places SDK

### Out of scope

- Online payment gateways
- Premium subscriptions and monetization
- Custom domains and subdomains
- White-label branding
- Developer API exposure beyond the documented internal endpoints
- Advanced analytics and platform administration features
- Marketplace-style modules
- AI-assisted content generation as an official MVP capability

## 3. User Stories and Priority

### Must Have

- As an organizer, I want to create an account and sign in, so that I can manage my events securely.
- As an organizer, I want to create an event with its title, date, venue, and capacity, so that I can publish it for guests.
- As an organizer, I want to publish an event to a public URL, so that guests can access the event page.
- As a guest, I want to open the public event page, so that I can learn about the event details.
- As a guest, I want to register for the event, so that I can reserve my place.
- As an organizer, I want to see the registered guest list, so that I can manage attendance.
- As an organizer, I want to check in guests manually at the venue, so that I can track who attended.

### Should Have

- As an organizer, I want to add agenda items, so that guests can understand the event schedule.
- As an organizer, I want to add speakers, so that the event page looks complete and informative.
- As a guest, I want venue directions from Google Maps, so that I can reach the location easily.

### Could Have

- As an organizer, I want lightweight brand customization, so that each event page matches the event identity.
- As a guest, I want a clearer registration confirmation experience, so that I know my registration was received.

### Won't Have in This MVP

- As an organizer, I want to accept online payments, so that I can sell tickets online.
- As an organizer, I want to attach a custom domain, so that my event uses a branded URL.
- As a team owner, I want advanced roles, plans, and monetization controls, so that I can manage a commercial platform.

## 4. Mockups

Mockups and user-story drafts were completed earlier by the team and are reused as the visual basis for this submission. The expected main screens covered by those mockups are:

- Organizer sign in and sign up
- Organizer dashboard
- Create/edit event form
- Public event landing page
- Guest registration form
- Guest list
- Offline/manual check-in screen

This repository focuses on the technical documentation and architecture that align with those mockups.

## 5. System Architecture

The high-level architecture is documented in `docs/diagrams/system-architecture.mmd`.
GitHub-rendered diagrams are also collected in `docs/diagrams.md`.

### Architecture overview

- The browser loads the Next.js web application from Vercel.
- Organizer and guest interactions are handled through the web UI.
- The application uses Supabase Auth for organizer sign-in.
- Event, guest, agenda, and speaker data are stored in Supabase Postgres.
- Row Level Security protects organizer-owned data.
- Google Maps API and Places SDK are used for venue search, map display, and directions.
- Production and staging share the same overall architecture but use separate deployment environments.

### Mermaid: System Architecture

```mermaid
flowchart LR
    Guest["Guest User"] --> Browser["Web Browser"]
    Organizer["Organizer"] --> Browser

    Browser --> Vercel["Vercel / Next.js Web App"]
    Vercel --> Auth["Supabase Auth"]
    Vercel --> DB["Supabase Postgres"]
    Vercel --> Storage["Supabase Storage"]
    Vercel --> Maps["Google Maps API and Places SDK"]

    Auth --> DB
    DB --> RLS["Row Level Security Policies"]

    subgraph Environments
      Prod["Production: rizi.app"]
      Stage["Staging: staging.rizi.app"]
    end

    Prod -. deploy .-> Vercel
    Stage -. validate .-> Vercel
```

## 6. Components and Classes

The class and component relationships are documented in `docs/diagrams/class-diagram.mmd`.

### Frontend modules

- `Auth UI`
  - Handles organizer sign up and sign in.
- `Event Management UI`
  - Handles event creation, editing, publishing, and guest list access.
- `Public Event Page`
  - Displays event details, agenda, speakers, and venue information at `/e/[slug]`.
- `Guest Registration UI`
  - Collects guest details and submits registration requests.
- `Guest List UI`
  - Shows registered guests and their attendance status.
- `Offline Check-in UI`
  - Allows an organizer to mark guests as checked in on-site.

### Backend service classes

- `AuthService`
  - Responsibilities: organizer registration, login, session validation.
  - Key methods: `registerOrganizer()`, `loginOrganizer()`, `getCurrentOrganizer()`.
- `EventService`
  - Responsibilities: create, update, publish, and fetch events.
  - Key methods: `createEvent()`, `updateEvent()`, `publishEvent()`, `getPublicEventBySlug()`.
- `GuestService`
  - Responsibilities: register guests and list guests per event.
  - Key methods: `registerGuest()`, `listGuestsByEvent()`, `getGuestById()`.
- `VenueLocationService`
  - Responsibilities: process venue selection data from Google Maps.
  - Key methods: `saveVenueLocation()`, `buildDirectionsUrl()`.
- `CheckInService`
  - Responsibilities: mark guests as checked in and prevent duplicate check-in actions.
  - Key methods: `checkInGuest()`, `getAttendanceStatus()`.

### Mermaid: Class and Component Diagram

```mermaid
classDiagram
    class AuthUI {
        +renderLoginForm()
        +renderRegisterForm()
        +submitCredentials()
    }

    class EventManagementUI {
        +renderEventForm()
        +saveDraft()
        +publishEvent()
        +viewGuestList()
    }

    class PublicEventPage {
        +loadEventBySlug()
        +renderEventDetails()
        +showVenueDirections()
    }

    class GuestRegistrationUI {
        +renderRegistrationForm()
        +submitRegistration()
        +showConfirmation()
    }

    class GuestListUI {
        +renderGuestList()
        +filterGuests()
        +openCheckInScreen()
    }

    class OfflineCheckInUI {
        +searchGuest()
        +confirmCheckIn()
        +showAttendanceStatus()
    }

    class AuthService {
        +registerOrganizer()
        +loginOrganizer()
        +getCurrentOrganizer()
    }

    class EventService {
        +createEvent()
        +updateEvent()
        +publishEvent()
        +getPublicEventBySlug()
    }

    class GuestService {
        +registerGuest()
        +listGuestsByEvent()
        +getGuestById()
    }

    class VenueLocationService {
        +saveVenueLocation()
        +buildDirectionsUrl()
        +mapPlaceToVenueFields()
    }

    class CheckInService {
        +checkInGuest()
        +getAttendanceStatus()
        +preventDuplicateCheckIn()
    }

    class User {
        +uuid id
        +string email
        +string name
        +string role
    }

    class Event {
        +uuid id
        +uuid organizerId
        +string slug
        +string title
        +string status
        +int capacity
        +string placeId
        +float latitude
        +float longitude
    }

    class Guest {
        +uuid id
        +uuid eventId
        +string fullName
        +string email
        +string phone
        +string tier
        +string status
        +datetime checkedInAt
    }

    class AgendaItem {
        +uuid id
        +uuid eventId
        +uuid speakerId
        +string title
        +datetime startTime
        +datetime endTime
    }

    class Speaker {
        +uuid id
        +uuid eventId
        +string fullName
        +string jobTitle
        +string bio
    }

    AuthUI --> AuthService : uses
    EventManagementUI --> EventService : uses
    EventManagementUI --> GuestService : reads guests
    PublicEventPage --> EventService : loads event
    PublicEventPage --> VenueLocationService : gets map data
    GuestRegistrationUI --> GuestService : registers guest
    GuestListUI --> GuestService : lists guests
    OfflineCheckInUI --> CheckInService : checks in guest
    CheckInService --> GuestService : reads guest

    User "1" --> "many" Event : creates
    Event "1" --> "many" Guest : contains
    Event "1" --> "many" AgendaItem : schedules
    Event "1" --> "many" Speaker : features
    Speaker "0..1" --> "many" AgendaItem : presents
```

## 7. Database Design

The ER diagram is documented in `docs/diagrams/database-er.mmd`.

### Core tables

- `users`
  - Stores organizer profile data linked to authentication records.
- `events`
  - Stores event metadata, slug, capacity, branding, and venue details.
- `guests`
  - Stores guest registration data and check-in status.
- `agenda_items`
  - Stores schedule entries for an event.
- `speakers`
  - Stores speaker details associated with an event.

### Reduced schema decisions

- Public event routing is slug-based under `/e/[slug]`.
- Payment-related tables are excluded from the MVP design.
- Subscription or premium-plan tables are excluded from the MVP design.
- Venue location data may include `place_id`, `address`, `latitude`, and `longitude`.
- Guests are treated as free-tier participants by default.

### Mermaid: Database ER Diagram

```mermaid
erDiagram
    USERS ||--o{ EVENTS : creates
    EVENTS ||--o{ GUESTS : registers
    EVENTS ||--o{ AGENDA_ITEMS : includes
    EVENTS ||--o{ SPEAKERS : features
    SPEAKERS o|--o{ AGENDA_ITEMS : may_present

    USERS {
        uuid id PK
        string email
        string name
        string role
        datetime created_at
    }

    EVENTS {
        uuid id PK
        uuid organizer_id FK
        string slug
        string title
        string status
        datetime start_date
        datetime end_date
        string venue_name
        string venue_address
        string city
        string place_id
        float latitude
        float longitude
        int capacity
        json brand_config
        datetime created_at
    }

    GUESTS {
        uuid id PK
        uuid event_id FK
        string full_name
        string email
        string phone
        string tier
        string status
        datetime checked_in_at
        datetime created_at
    }

    AGENDA_ITEMS {
        uuid id PK
        uuid event_id FK
        uuid speaker_id FK
        string title
        string item_type
        datetime start_time
        datetime end_time
        string location_name
    }

    SPEAKERS {
        uuid id PK
        uuid event_id FK
        string full_name
        string job_title
        string bio
    }
```

## 8. Sequence Diagrams

The key interaction diagrams are stored in:

- `docs/diagrams/sequence-organizer-auth.mmd`
- `docs/diagrams/sequence-create-publish.mmd`
- `docs/diagrams/sequence-guest-registration.mmd`
- `docs/diagrams/sequence-offline-checkin.mmd`

### Covered scenarios

- Organizer registration and sign in.
- Organizer creates and publishes an event.
- Guest opens the event page and registers.
- Organizer performs offline/manual check-in.

### Sequence coverage note

Together, the sequence diagrams cover the full MVP flow from organizer authentication to event publishing, guest registration, guest list retrieval, and offline check-in. The create/publish and guest-registration sequences also cover the Should Have stories around agenda, speakers, and venue directions at the level expected for this MVP.

### Mermaid: Organizer Authentication

```mermaid
sequenceDiagram
    actor Organizer
    participant UI as Auth UI
    participant API as AuthService
    participant Auth as Supabase Auth
    participant DB as Supabase Postgres

    Organizer->>UI: Open sign up or sign in screen
    alt New organizer registration
        Organizer->>UI: Submit register form
        UI->>API: POST /api/auth/register
        API->>Auth: Create auth account
        Auth->>DB: Create organizer profile record
        DB-->>Auth: Profile saved
        Auth-->>API: Account created
        API-->>UI: Registration success
    else Existing organizer login
        Organizer->>UI: Submit login form
        UI->>API: POST /api/auth/login
        API->>Auth: Validate credentials
        Auth-->>API: Session returned
        API-->>UI: Authenticated session
    end
```

### Mermaid: Create and Publish Event

```mermaid
sequenceDiagram
    actor Organizer
    participant UI as Event Management UI
    participant API as EventService
    participant Maps as VenueLocationService
    participant DB as Supabase Postgres

    Organizer->>UI: Open create event form
    Organizer->>UI: Enter title, dates, capacity, branding
    Organizer->>UI: Search venue
    UI->>Maps: Resolve place data from Google Maps
    Maps-->>UI: place_id, address, latitude, longitude
    Organizer->>UI: Save draft
    UI->>API: POST /api/events
    API->>DB: Insert draft event with slug and venue data
    DB-->>API: Event created
    API-->>UI: Draft event response
    Organizer->>UI: Add optional agenda and speakers
    UI->>API: PATCH /api/events/{eventId}
    API->>DB: Update event content
    DB-->>API: Event updated
    API-->>UI: Updated event response
    Organizer->>UI: Publish event
    UI->>API: POST /api/events/{eventId}/publish
    API->>DB: Update event status to published
    DB-->>API: Published event
    API-->>UI: Public URL returned
```

### Mermaid: Guest Registration

```mermaid
sequenceDiagram
    actor Guest
    participant UI as Public Event Page
    participant API as GuestService
    participant Maps as VenueLocationService
    participant DB as Supabase Postgres

    Guest->>UI: Open /e/{slug}
    UI->>API: GET /api/public/events/{slug}
    API->>DB: Read published event by slug
    DB-->>API: Event details, agenda, speakers, venue
    API-->>UI: Event page payload
    UI->>Maps: Build directions link from venue data
    Maps-->>UI: Directions URL
    Guest->>UI: Review details and submit registration form
    UI->>API: POST /api/guests/register
    API->>DB: Validate event and create guest
    DB-->>API: Guest record created
    API-->>UI: Registration success response
    UI-->>Guest: Confirmation shown
```

### Mermaid: Offline Check-in

```mermaid
sequenceDiagram
    actor Organizer
    participant UI as Guest List and Check-in UI
    participant GuestAPI as GuestService
    participant API as CheckInService
    participant DB as Supabase Postgres

    Organizer->>UI: Open guest list
    UI->>GuestAPI: GET /api/events/{eventId}/guests
    GuestAPI->>DB: Fetch registered guests
    DB-->>GuestAPI: Guest list
    GuestAPI-->>UI: Guest list response
    Organizer->>UI: Search guest and confirm check-in
    UI->>API: POST /api/guests/{guestId}/checkin
    API->>DB: Update guest status and checked_in_at
    DB-->>API: Updated guest
    API-->>UI: Check-in success response
    UI-->>Organizer: Attendance updated
```

## 9. API Specifications

The detailed endpoint definitions are documented in `docs/api-spec.md`.

### MVP endpoint set

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/events`
- `GET /api/events`
- `GET /api/events/{eventId}`
- `PATCH /api/events/{eventId}`
- `POST /api/events/{eventId}/publish`
- `GET /api/public/events/{slug}`
- `POST /api/guests/register`
- `GET /api/events/{eventId}/guests`
- `POST /api/guests/{guestId}/checkin`

## 10. SCM and QA

The full plan is documented in `docs/scm-qa-plan.md`.

### SCM summary

- `main` is the protected branch.
- Each task is developed in a short-lived feature branch.
- Pull requests are reviewed before merge.
- Commits stay small and tied to one task or fix.

### QA summary

- Manual smoke tests cover the main organizer and guest flows.
- Targeted component and API tests are added where feasible.
- Staging is used for validation before production release.

## 11. Technical Justifications

The full rationale is documented in `docs/technical-justifications.md`.

### Main decisions

- Supabase reduces backend setup overhead and provides Auth, Postgres, and access control quickly.
- Vercel is a practical fit for Next.js deployment, preview environments, and fast iteration.
- Google Maps is the most useful external integration for accurate venue location and directions.
- Online payments are intentionally deferred to keep the MVP realistic and deliverable for a small student team.

## 12. Acceptance Criteria

- The repository documents only the reduced MVP scope.
- The diagrams match the documented architecture and database design.
- The API specification aligns with the user stories and sequence diagrams.
- The SCM and QA plan is realistic for a four-member student team.
- The `.docx` submission file is generated from the repo content and ready to upload.
