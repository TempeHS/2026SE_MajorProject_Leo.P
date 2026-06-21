# Sprint Backlog

---

## SPRINT 1: Skeleton

### Sprint Goal

Develop a base skeleton layout for OneLink and map basic feature locations to support future development.

### Committed Items

- PB1: [User story title]
- PB2: [User story title]

### Sprint Plan

1. Create the layout for the homepage of the website
2. Add cards to the homepage for easy navigation
3. Create a navbar and footer across all the site's pages
4. Ensure all links and buttons work as intended and take you to the correct page
5. Add basic functionality that is apart of the layout

### Unit Test Summary Table

| Feature       | Test                                                   | Expected Result               | Actual Result                                                     | Pass/Fail |
| ------------- | ------------------------------------------------------ | ----------------------------- | ----------------------------------------------------------------- | --------- |
| Site loading  | Send GET request to http://localhost:8000              | Server responds with HTTP 200 | Server responded with HTTP 200 (pytest: [100%] 1 passed in 0.13s) | Pass      |
| Pages loading | Send GET request to all listed routes (see list below) | Server responds with HTTP 200 | Server responded with HTTP 200 (pytest: [100%] 9 passed in 0.28s) | Pass      |

Routes tested:

- /
- /about
- /resources
- /privacy
- /login.html
- /signup.html
- /past_papers
- /useful_websites
- /personal_dashboard

### Sprint Review

In sprint 1, I was able to complete a base skeleton for my website to support future development. The navigation between the main pages functioned properly and worked as intended, as well as page loading and basic functional features related to the layout such as the offcanvas.

- Items delivered: Website skeleton, linked base pages, functionality related to layout

### Sprint Retrospective

- **What went well:**
  - The overall development of each page went well and as expected, with minimum issues throughout the process
- **What didn’t go well:**
  - Minor issues such as typos in files which caused runtime errors, or code not behaving as expected due to logic issues
- **What to improve next sprint:**
  - Time management and pace of development

---

## SPRINT 2: Base Navigation and Functionality

### Sprint Goal

Develop the website's navigation and implement base level functionality.

### Committed Items

- PB2: [User story title]
- PB3: [User story title]

### Sprint Plan

1. Implement client feedback from Sprint 1 demo
2. Develop base necessary functionality
3. Flesh out general website navigation including more page creation
4. Develop an initial prototype subject page structure
5. Create a reusable resource card component that can be adapted for future development

### Unit Test Summary Table

| Feature                                       | Test                                                   | Expected Result                        | Actual Result                                                     | Pass/Fail |
| --------------------------------------------- | ------------------------------------------------------ | -------------------------------------- | ----------------------------------------------------------------- | --------- |
| Pages loading                                 | Send GET request to all listed routes (see list below) | Server responds with HTTP 200          | Server responded with HTTP 200 (pytest: [100%] 5 passed in 0.19s) | Pass      |
| Signup (Manual test)                          | POST valid new email/password                          | Redirect to /login.html, success flash | Redirected to /login.html                                         | Pass      |
| Duplicate signup (Manual test)                | POST existing email                                    | Redirect to /signup.html, error flash  | Redirected to /signup.html                                        | Pass      |
| Login correct (Manual test)                   | POST valid credentials                                 | Redirect to /2fa.html                  | Redirected to /2fa.html                                           | Pass      |
| Login with wrong email/password (Manual test) | POST wrong email or password                           | Redirect to /login.html, error flash   | Redirected to /login.html                                         | Pass      |
| 2FA invalid OTP (Manual test)                 | POST invalid OTP                                       | Remain in 2FA, error flash             | Remained in 2FA, error flash                                      | Pass      |

Routes tested:

- /subject/hsie/business-studies
- /subject/hsie/business-studies/past-papers
- /resources
- /login.html
- /signup.html

### Sprint Review

In sprint 2, I was able to successfully delivered / completed my sprint plan and have everything working, including implementing client feedback from the sprint 1 demo, developing the base necessary functionality and general website navigation, as well as an initial prototype subject page structure with a reusable resource card component that can be adapted for future development.

### Sprint Retrospective

- **What went well:**
  - Overall development of the website went as expected and I ran into little hiccups along the way
- **What didn’t go well:**
  - Ran into repetitive issues with navigation, as it was a struggle trying to create unique paths and not duplicate ways to get to the same page, which was improved by reworking site layout
- **What to improve next sprint:**
  - Time management and pace of development

---

## SPRINT 3: Content population and expansion

### Sprint Goal

Expand and structure the demo subject (Business Studies) resource system + home page cards using reusable components

### Committed Items

- PB2: [User story title]
- PB3: [User story title]

### Sprint Plan

1. Implement client feedback from sprint 2
2. Build demo subject (Business studies) page structure with 1 or more functioning cards
3. Populate demo subject (Business studies) page with placeholder resource cards to simulate real content
4. Improve overall layout consistency
5. Populate home page cards with placeholder resource cards to simulate real content
6. Check all navigation paths work correctly

### Unit Test Summary Table

| Feature                                | Test                                                   | Expected Result                        | Actual Result                                                     | Pass/Fail |
| -------------------------------------- | ------------------------------------------------------ | -------------------------------------- | ----------------------------------------------------------------- | --------- |
| Pages loading                          | Send GET request to all listed routes (see list below) | Server responds with HTTP 200          | Server responded with HTTP 200 (pytest: [100%] 2 passed in 0.28s) | Pass      |
| Resource card opening (Manual testing) | Open various resource cards (see list below)           | Cards redirect to respective resources | Cards redirected to respective resources                          | Pass      |

Routes tested:

- /subject/hsie/business-studies/notes/operations
- /subject/hsie/business-studies/videos/operations

Resource cards tested:

- Past Papers
- Notes
- Videos

### Sprint Review

In sprint 3, I was able to implement client feedback from sprint 2, as well as working on the demo subject (Business studies) and adding some functioning cards in past papers, notes and videos. I populated Business studies a with a few placeholder resource cards (specifically in past papers) to simulate real content and what a page would look like when full. The overall layout consistency was improved and all navigation paths were checked to make sure they worked correctly.

### Sprint Retrospective

- **What went well:**
  - The use of a card template and moulding it to the different pages in order to develop a cohesive card layout look across the demo subject pages
- **What didn’t go well:**
  - The scope of the sprint was a bit too large considering the time I had, meaning that population of the home page had to be cut, meaning there was a shift in focus from fully populating the demo subject page to a focus on delivering an example of each type of card that will be seen throughout the website in future enhancements.
- **What to improve next sprint:**
  - Time management

---

## SPRINT 4: Visual design and styling

### Sprint Goal

Improve visual design and user experience of OneLink.

### Committed Items

- PB2: [User story title]
- PB3: [User story title]

### Sprint Plan

1. Apply a consistent colour palette and styling theme site wide
2. Add images and information across the site
3. Improve header design
4. Implement visual feedback with cards
5. Enhance offcanvas navigation with background blur

### Unit Test Summary Table

| Feature      | Test            | Expected Result    | Actual Result | Pass/Fail |
| ------------ | --------------- | ------------------ | ------------- | --------- |
| Feature name | What you tested | What should happen | What happened | Pass/Fail |
| Feature name | What you tested | What should happen | What happened | Pass/Fail |

### Sprint Review

Write what was completed, what worked, and what was delivered.

### Sprint Retrospective

- **What went well:**
- **What didn’t go well:**
- **What to improve next sprint:**

---
