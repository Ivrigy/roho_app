# Roho Booking Service

A sass-free booking system for event agencies, art directors, galleries, fairs — and anyone else who needs to *hire awesome people* without the carrier pigeons, smoke signals, or frantic last-minute phone calls.
![Intro](static/images/docs/responsive.png)

## Table of Contents
- [Overview](#overview)  
- [UX Design](#ux-design) 
- [Agile Methodologies](#agile-methodologies) 
- [Features](#features)   
- [User Flows](#user-flows)  
- [Pages](#pages)  
- [Technologies Used](#technologies-used) 

## Overview

Roho Booking Service is the secret weapon for event managers and creative agencies who need to book staff — and book them *fast*. Whether you’re curating a gallery opening, orchestrating a fair, or just trying to fill seats at your next big show, Roho’s got your back. Think of it as Tinder for top-notch event staff (minus the awkward swiping).

**Target Audience:**  
- 🏢 Agencies that organize events  
- 🎨 Art directors and gallery curators  
- 🎉 Fair and festival coordinators  
- ‍💼 Anyone who has ever said, “Why is booking people so complicated?”  

## UX Design

### Strategy plane
I originally designed Roho as a full talent marketplace with multi-service booking, profiles, ratings, messaging, and availability calendars. Because of the timeline, I applied Agile scoping and shipped an MVP that solves the essential job end-to-end: discover the service, submit a booking, review or edit or delete it, and let an admin triage entries. The larger concept stays on the roadmap.

### Site goals
- Deliver a fast, low-friction path from landing to confirmed booking
- Keep the interface predictable and consistent on mobile, tablet, and desktop
- Use high contrast and clear hierarchy for easy reading
- Give admins simple oversight to keep data clean
- Leave room for growth without redesigning the core

### Scope and Agile decisions (MVP)
- Kept: authentication, Offer → Booking flow, My Bookings with CRUD, basic admin visibility
- Deferred: staff profiles, messaging, calendar availability, quotes, multi-tenant agencies
- Process: very small user stories with acceptance criteria, Kanban flow, demoable increments

### User Stories

### Admin / business owner
- As an admin, I want to view all bookings so that I can manage schedules and data integrity.
- As an admin, I want to edit or delete any booking so that I can correct mistakes or remove duplicates.
- As an admin, I want to manage service categories so that I can adjust the offer.

### Visitor / guest
- As a visitor, I want to understand the service at a glance so that I know if this solves my problem.
- As a visitor, I want to see clear navigation to Book Now and Register so that I can start immediately.
- As a visitor, I want responsive pages on mobile, tablet, and desktop so that I can use the site anywhere.

### New user
- As a new user, I want to register an account so that I can submit bookings.
- As a new user, I want helpful form hints and validation so that I can complete registration without confusion.

### Logged-in user
- As a user, I want to log in and out reliably so that my account stays secure.
- As a user, I want to choose a service from the Offer page and go straight to the correct booking form so that I don’t get lost.
- As a user, I want to submit a booking with event details, dates, and number of people so that the team can staff my event.
- As a user, I want the form to prevent past dates and enforce start before end so that my booking is valid.
- As a user, I want a clear confirmation after submitting so that I know it worked.
- As a user, I want to see my bookings in My Bookings so that I can review the status at any time.
- As a user, I want to edit an existing booking with the form prefilled so that I can fix small mistakes quickly.
- As a user, I want to delete a booking I no longer need so that I don’t clutter the system.

### UX research and market scan
  
I wanted to understand how event-staffing and booking platforms set expectations: what fields they ask for, how fast you can submit a request, how they communicate availability and pricing, and where users typically drop off.

sample and method  
I did a comparative teardown of agency sites, self-serve booking tools, and marketplace job boards across Germany/EU/US. I captured flows, forms, copy, and visual patterns, then tagged everything by friction level, clarity, and mobile behavior.  
![Competitive scan](static/images/docs/comparison.png)

key patterns I saw
- most “contact us” flows ask for too many fields, especially before trust is built
- mobile usability varies a lot; some forms are cramped and error handling is vague

what I adopted
- one clear path: Offer → Booking form → confirmation
- minimal required fields with strong hints and inline validation

### Information architecture
- Navbar: Home • Book Now • My Bookings • Login or Logout
- Primary flows:
  1) Offer → Booking form → confirmation
  2) My Bookings → edit or delete
  3) Admin at /admin → review and clean up
- Copy: short action labels and one clear CTA per section

### Wireframes and design evolution
- Wireframes: a simple path from Home to Book to My Bookings with centered forms and visible CTAs  
  ![Wireframes](/static/images/docs/wireframes.png)

- Early MVP screens: Offer cards, Booking form, Sign-up/Sign-in, and My Bookings list  
  ![MVP Screens](/static/images/docs/Booking.png)

- First large landing concept (pre-scope cut): editorial hero blocks, multiple service areas, and a banner callout  
  ![Initial Landing Concept](/static/images/docs/rohohomepage.png)

I trimmed the large landing to keep speed and clarity for the MVP while keeping the visual language ready for future expansion.

### Visual design and color system

I chose a modern, high-contrast palette so actions are easy to notice and the interface works well for users who need more contrast.
- Pitch black: application background for maximum contrast
- White: primary text on dark
- Electric or mint green: primary CTAs, focus rings, active accents
- Soft violet: secondary accents, icons, card tints
- Brand accent: highlights, badges, emphasis states
- Dark greys: elevated panels and form surfaces over black

Contrast and accessibility
- Body text on dark meets WCAG 2.2 AA targets; large CTAs exceed minimums
- Focus rings are clearly visible on all interactive elements
- Icons are always paired with text or an aria-label to avoid color-only cues

### Interaction and validation
- Date pickers block past dates and enforce start not after end on both client and server
- Required fields are validated inline and errors are announced to assistive tech
- After submit, the confirmation keeps context and offers a clear next step

## Agile methodology
I worked in a simple Kanban flow (To do → In progress → Done) using GitHub Issues and a GitHub Projects board. I kept stories small with acceptance criteria, merged related work into epics, and aimed for a fast MVP, then iteration.

process
- planned user stories on the board (To do → In progress → Done)
- wrote acceptance criteria first, then adjusted tasks after the first implementation spike
- shipped in short increments to Heroku and noted a tiny retro each time (keep, change, try)
- used MoSCoW to keep scope honest

epics I used
- auth and sessions
- booking flow (offer cards, form, validation, confirmation)
- my bookings (list, edit, delete)
- admin operations (manage bookings via Django admin, cleanup, light exports)
- accessibility and performance (contrast, focus rings, asset sizing)
- platform setup and deployment (installation, project setup, Heroku deploy)
- foundational UI (home/landing page and navigation)

example user story and acceptance criteria
- as a user I can select a booking service, fill the form, and send my inquiry so that I can receive the service I need
  - acceptance criterion 1: the booking offer is visible and reachable
  - acceptance criterion 2: the form validates and submits correctly
  - acceptance criterion 3: after submit, the booking appears in My Bookings

prioritisation (MoSCoW)
- must have: authentication, Offer → Booking flow, My Bookings CRUD, basic admin visibility
- should have: category management in admin, clearer field hints, high-contrast theme and keyboard navigation
- could have: quick quotes, saved organizations, better exports, richer empty states
- won’t have in this release: messaging, staff profiles/ratings, availability calendars, multi-tenant features


I track work on a GitHub Projects Kanban here: [roho_project – Kanban board](https://github.com/users/Ivrigy/projects/3/views/1)

## Features

### 🔐 Authentication  
- **User sign-up / log-in / log-out**  
- Passwords safely tucked away behind Django’s fortress walls  

### 📝 Booking Service  
- Fill out a slick, no-drama booking form  
- Pick dates, times, and the number of staff needed  
- A **Submit** button that actually works (we promise)  

### 🔄 CRUD Operations  
- **Create** new bookings (duh)  
- **Read** your upcoming “glorious staff deployments”  
- **Update** mind-blowing changes on the fly  
- **Delete** — because sometimes plans change (or budget cuts happen)  

### 🎛️ Admin Dashboard  
- Superusers can view and manage **all** bookings  
- Cull duplicates, banish inappropriate entries, or just admire your own organizational prowess  


## User Flows

1. **User A – Newbie**  
   - Visits homepage → registers (quick as a flash) → logs in  
   - Clicks the “Book” card → fills in the booking request → 🎉 Confirmed!  
   - Edits or deletes bookings on the **My Bookings** page → logs out  

2. **User B – The Return Visitor**  
   - Logs in → lands on **My Bookings** (because we love you)  
   - Edits or deletes an existing booking → logs out  

3. **Admin User – The Overlord**  
   - Logs in to `/admin/` → surveys all bookings at a glance  
   - Deletes duplicates, flags shady requests, or just sips coffee while watching it all  

## Pages

### 1. Intro / Homepage  
![Intro](static/images/docs/intro.png)
- **Where you land:** Bold header asks, “LOOKING FOR SHARP, STYLISH, AND UNSHAKABLY RELIABLE STAFF?”  
- **Quick links:**  
  - **Home** | **Book Now** | **My Bookings** | **Logout** (once you’re in)  
- **Why it rocks:** You see the pitch, you see the logo, you know exactly where to click. No scrolling safari required.

### 2. Service Categories (“Offer” Page)  
![Choose Category](static/images/docs/offer.png) 
- **URL/Shortcut:** Click **Book Now** → land here instantly.  
- **Cards on display:**  
  - **POWER HANDS** (💪 heavy-lifting heroes)  
  - **SECURITY** (🛡 keep the drama off your premises)  
  - **PROMOTERS** (📣 hype machines on demand)  
- **CTA:** Each card has its own **Book** button — click one and BOOM, you’re off to the form.

### 3. Login Page  
![Login Page](static/images/docs/login.png) 
- **URL/Shortcut:** Navbar → **Login**  
- **Fields:** Username, Password  
- **Magic moment:** Hit **Enter** (that glowing green button) and you’re in.  
- **Pro tip:** If you forget your creds, you *may* have to create a new account... or consult your password manager.

### 4. Sign Up Page  
![Sign Up Page](static/images/docs/signup.png) 
- **URL/Shortcut:** Navbar → **Register**  
- **Fields:**  
  - Username (150-char limit, no emojis — sorry)  
  - Password + confirmation (must be > 8 chars, not “12345678”)  
- **UX treat:** Real-time hints below each field keep you honest. No post-submit surprises!

### 5. Book a Service (Booking Form)  
![Booking Form](static/images/docs/bookingform.png)
- **URL/Shortcut:**  
  - From **Offer** card **Book** → direct jump  
  - Or Navbar → **Book Now**  
- **Form bits:**  
  - Name, Email, Company, Event Name  
  - Service Type dropdown (what you chose on the Offer page)  
  - Number of People, Hours, Budget  
  - Start Date/End Date (date picker prevents past dates)  
  - Additional Notes (“We need coffee ASAP!”)  
- **Validation shortcuts:**  
  - 🔒 Start/End date locked to the future  
  - 🔢 “Number of People” ≥ 1  
  - ✏️ All required fields are enforced

### 6. My Bookings  
![My Bookings](static/images/docs/mybookings.png)  
- **URL/Shortcut:** Navbar → **My Bookings**  
- **What you see:** A dark-mode list of your gigs — each card shows:  
  - Event title & service type  
  - Dates & notes  
  - **Edit** (green) and **Delete** (red) buttons  
- **One-click fixes:**  
  - **Edit** reloads the form pre-filled  
  - **Delete** vanishes unwanted bookings faster than your inbox spam

### 7. Edit Booking  
*(Same form as “Book a Service,” but with your old info pre-filled. No extra screenshots needed — just you, channeling your inner event-planner zen.)*

### 8. Admin Panel  
*(Not shown here, but imagine the ultimate CRUD dashboard at `/admin/` where you can view, edit, or obliterate any booking. Capes optional.)*

## Technologies used

languages
- HTML5
- CSS3
- JavaScript (ES6)
- Python 3.12

frameworks and libraries
- Django 5.2 (templates, built-in auth, forms, admin)
- Bootstrap 5 (responsive layout and components)
- Gunicorn (WSGI server for production on Heroku)
- WhiteNoise (serving static files in production)
- psycopg2-binary (PostgreSQL adapter)

database
- PostgreSQL in production
- SQLite for local development

hosting and deployment
- Heroku (app hosting, config vars, logs)
- Heroku CLI for deploys

version control and project management
- Git and GitHub (source control, pull requests)
- GitHub Projects Kanban board for user stories and epics  
  roho_project – Kanban board: https://github.com/users/Ivrigy/projects/3/views/1

quality and testing
- flake8 (Python linting in VS Code)
- JSHint (JavaScript linting)
- W3C Markup Validator and W3C CSS Validator
- Lighthouse and axe DevTools for accessibility and performance checks

developer tools
- VS Code
- Chrome DevTools
- Responsively App (responsive previews)
- GitHub Actions (optional, for CI)
- environment variables via .env locally and Heroku config vars

design and assets
- Figma (wireframes and UI)
- Google Fonts
- image optimization tools (e.g., TinyPNG) when needed


## Testing

Testing was woven into every step of Roho’s development — because “it works on my machine” isn’t a QA strategy. While we didn’t write Django `TestCase` unit tests (yet), **manual testing drove the project to rock-solid reliability**.

### Manual Testing Overview

- **Authentication Workflow**  
  - Registration, login, logout, and session persistence  
  - Navbar links updating correctly for logged-in vs. guest users  
- **Booking System**  
  - Create, read, update, and delete bookings  
  - Date-picker validation (no time machines allowed — past dates are blocked)  
- **Form & UX Validation**  
  - JavaScript checks for required fields, valid staff counts, and future dates  
  - Backend re-validation in Django to catch anything that slipped past the client  
- **Navigation & Layout**  
  - Consistent header/footer across all pages  
  - Responsive behavior on desktop, tablet, and (lightning-fast) mobile

### 🐍 Python (PEP 8)
- **Linting:** Used **flake8** and VS Code’s built-in linter to enforce style.  
- **Checks performed:**  
  - Maximum line length  
  - Proper function/class names (snake_case & CamelCase)  
  - Consistent indentation and whitespace  
  - Removal of unused imports and variables  

### 📜 JavaScript (ES6+)
- **Validation:** Ran **JSHint** (configured with `esversion: 6`) on all custom scripts.  
- **Checks performed:**  
  - No undefined variables  
  - Required semicolons (where needed)  
  - Logical flow and syntax correctness  

### 🌐 HTML5 & CSS3
- **HTML:** Passed through the **W3C Markup Validator** — only minor warnings about self-closing tags.  
- **CSS:** Verified with the **W3C CSS Validator** — zero errors; responsive media queries all clear.  
- **Responsive rules:** Ensured flexible layouts using CSS Grid and Flexbox across desktop, tablet, and mobile.

![Testing](static/images/docs/testingpy.png)
![Testing](static/images/docs/testingcss.png)

## Kanban Board

- **Why it matters:**  
  - Keeps the team aligned on what’s next  
  - Highlights bottlenecks (“Why is nothing in Review?!”)  
  - Turns project madness into a satisfying card shuffle  

Not really satisfied with it.

## Credits

https://github.com/bitlabstudio/django-booking  
https://github.com/DeanA1985/Restaurant-Booking-System?tab=readme-ov-file  
https://getbootstrap.com/  
https://code.visualstudio.com/  
https://www.youtube.com/watch?v=opjyyXoqrxg  
https://www.djangoproject.com/  
https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started  

And RORY for having patience with an ADHD person.
