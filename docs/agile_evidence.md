# FitForge Agile Evidence

FitForge was developed using an agile approach with user stories, MoSCoW prioritisation, small iterations, regular testing, and small Git commits.

## Project Goal

Build a fitness subscription and e-commerce application where users can buy fitness products, start a membership, complete challenges and workouts, earn rank rewards, and manage community content.

## MoSCoW Priorities

| Priority | User Story | Acceptance Criteria | Status |
| --- | --- | --- | --- |
| Must Have | As a visitor, I can register for an account so that I can access member features. | Registration form creates an account and redirects the new user into the member flow. | Complete |
| Must Have | As a user, I can log in and log out so that my account is secure. | Login and logout work from the frontend without errors. | Complete |
| Must Have | As a customer, I can browse products so that I can choose fitness content or merchandise. | Shop page lists active products with prices and product detail pages. | Complete |
| Must Have | As a customer, I can add products to my bag so that I can prepare a purchase. | Bag stores selected items in the session and shows a correct total. | Complete |
| Must Have | As a customer, I can checkout so that I can complete an order. | Checkout creates a paid order, line items, and order success page. | Complete |
| Must Have | As a member, I can complete daily challenges so that I can earn reward points. | Challenge can be completed from the frontend and points are awarded once. | Complete |
| Must Have | As a member, I can complete workouts so that I can track training activity. | Workout completion form creates a completion record and awards points. | Complete |
| Must Have | As a member, I can create, edit, and delete progress posts so that I control my community content. | CRUD actions work from the frontend without admin access. | Complete |
| Must Have | As a site owner, I can support SEO and marketing so that the business can be discovered. | Meta descriptions, sitemap, robots, newsletter, and Facebook mockup exist. | Complete |
| Should Have | As a member, I can view my rank badge so that progress feels rewarding. | Header and dashboard show the current rank badge. | Complete |
| Should Have | As a member, I can access premium workouts after activating membership. | Premium workouts are locked until membership is active. | Complete |
| Should Have | As a customer, I can leave and delete reviews so that I can share product feedback. | Reviews can be created, updated, and deleted from the frontend. | Complete |
| Should Have | As a mobile user, I can navigate with a burger menu so that the site works on my phone. | Mobile menu opens and profile links remain accessible. | Complete |
| Could Have | As a member, I can receive varied challenges so that the app feels fresh. | Completed challenges move behind random available challenges. | Complete |
| Could Have | As a returning member, I can complete advanced workouts so that the app supports progression. | Advanced premium workout is available in the workout library. | Complete |

## Iteration Notes

| Iteration | Focus | Outcome |
| --- | --- | --- |
| 1 | Project setup | Django project, apps, settings, templates, and repository created. |
| 2 | Core user flow | Registration, login, logout, dashboard, and profile flow added. |
| 3 | Rewards and fitness content | Rank points, daily challenges, workouts, and membership logic added. |
| 4 | E-commerce | Products, bag, checkout, orders, and purchase rewards added. |
| 5 | Community CRUD | Progress posts and reviews added with frontend create/update/delete actions. |
| 6 | Marketing and SEO | Newsletter, robots.txt, sitemap.xml, custom 404, and Facebook mockup added. |
| 7 | Responsive UI | Forge theme, generated imagery, mobile navigation, footer, and social links added. |
| 8 | Reward polish | Profile dropdown, cart icon, rank badges, challenge rotation, and advanced workout added. |
| 9 | Testing evidence | Automated and manual testing evidence added to `TESTING.md`. |

## Definition Of Done

A feature is considered complete when:

- The feature works from the frontend without requiring Django admin access where user CRUD is expected.
- The feature has user feedback such as messages, redirects, or visible updates.
- The feature is responsive on mobile and desktop.
- The feature is covered by automated tests where the behaviour has meaningful risk.
- The change is committed in a small Git commit with a clear message.

## Retrospective Notes

- The project began with the core Django structure first, then added fitness-specific models and business rules.
- The reward system was kept points-based so rank progress stays easy to understand.
- Later UI iterations moved less important links into a profile dropdown to make the mobile layout cleaner.
- Testing evidence was separated into `TESTING.md` so the README remains readable while still meeting assessment expectations.
