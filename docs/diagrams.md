# RiziEvents Diagrams

This page collects every Mermaid diagram used in the project documentation so GitHub can render them in one place.

## Story Coverage Matrix

| User Story | Diagram Coverage |
| --- | --- |
| Organizer creates an account and signs in | Organizer Authentication Sequence, Class Diagram, System Architecture |
| Organizer creates an event with title, date, venue, and capacity | Create and Publish Event Sequence, Class Diagram, ER Diagram |
| Organizer publishes an event to a public URL | Create and Publish Event Sequence, System Architecture |
| Guest opens the public event page | Guest Registration Sequence, System Architecture |
| Guest registers for the event | Guest Registration Sequence, Class Diagram, ER Diagram |
| Organizer sees the registered guest list | Offline Check-in Sequence, Class Diagram |
| Organizer checks in guests manually | Offline Check-in Sequence, Class Diagram |
| Organizer adds agenda items | ER Diagram, Class Diagram |
| Organizer adds speakers | ER Diagram, Class Diagram |
| Guest uses venue directions | System Architecture, Class Diagram |

## System Architecture

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
      Prod["Production: www.rizi.app"]
      Stage["Staging: staging.rizi.app"]
    end

    Prod -. deploy .-> Vercel
    Stage -. validate .-> Vercel
```

## Class and Component Diagram

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

## Database ER Diagram

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

## Sequence: Organizer Authentication

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

## Sequence: Create and Publish Event

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

## Sequence: Guest Registration

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

## Sequence: Offline Check-in

```mermaid
sequenceDiagram
    actor Organizer
    participant UI as Guest List and Check-in UI
    participant GuestAPI as GuestService
    participant CheckIn as CheckInService
    participant DB as Supabase Postgres

    Organizer->>UI: Open guest list
    UI->>GuestAPI: GET /api/events/{eventId}/guests
    GuestAPI->>DB: Fetch registered guests
    DB-->>GuestAPI: Guest list
    GuestAPI-->>UI: Guest list response
    Organizer->>UI: Search guest and confirm check-in
    UI->>CheckIn: POST /api/guests/{guestId}/checkin
    CheckIn->>DB: Update guest status and checked_in_at
    DB-->>CheckIn: Updated guest
    CheckIn-->>UI: Check-in success response
    UI-->>Organizer: Attendance updated
```
