# FitForge Testing

Testing for FitForge covers automated Django tests, manual feature testing, responsive layout checks, and final deployment checks. The goal is to prove that users can register, buy products, manage community content, complete fitness actions, and earn rewards without using the Django admin panel.

## Automated Tests

Run the automated test suite with:

```bash
python manage.py test
```

Current result:

| Area | Test Coverage | Expected Result | Status |
| --- | --- | --- | --- |
| Rewards | Points total correctly and map to the correct rank | User rank updates from reward events | Pass |
| Rewards | Idempotent reward events do not duplicate | Same reward can only be claimed once when an idempotency key is used | Pass |
| Daily challenges | User can complete a challenge once | Completion and reward are only created once | Pass |
| Daily challenges | Completed challenges are replaced by available challenges | Challenge page shows a fresh available challenge first | Pass |
| Orders | Checkout creates an order and line item | User receives a paid order and purchase reward | Pass |
| Progress posts | Owner can delete their own post | Post is removed from the database | Pass |
| Progress posts | Other users cannot delete another user's post | Request is forbidden | Pass |

## Manual Testing

| Feature | Steps Tested | Expected Result | Status |
| --- | --- | --- | --- |
| Register | Open Register, enter valid username, email, and password, submit form | Account is created and user is redirected to profile setup | Pass |
| Login | Open Login, enter valid credentials, submit form | User is logged in and dashboard loads | Pass |
| Logout | Click Logout in the header | User is logged out and returned to the public site | Pass |
| Profile dropdown | Log in, click the profile icon in the header | Dropdown opens with Dashboard, Profile, Challenges, Workouts, and Membership links | Pass |
| Shopping cart icon | Click the cart icon in the header | Shopping bag page opens | Pass |
| Rank badge | Log in and view the header/dashboard | Current rank badge appears beside the profile icon and near the progress bar | Pass |
| Profile update | Edit profile with full name, goal, experience level, and preferences | Profile saves and profile completion reward is awarded once | Pass |
| Daily challenge | Open Challenges and click Mark complete | Completion message appears and points are awarded | Pass |
| Challenge rotation | Complete a challenge and return to Challenges | Completed challenge moves behind fresh uncompleted challenges | Pass |
| Workout completion | Open an unlocked workout, enter notes, submit completion | Completion history updates and workout points are awarded | Pass |
| Premium workout lock | Open premium workout without active membership | User is redirected with membership warning | Pass |
| Membership activation | Open Membership and click Start membership | Membership becomes active and premium workouts unlock | Pass |
| Product list | Open Shop | Active products display with euro prices | Pass |
| Product detail | Open a product and submit Add to bag | Product is added to the session bag | Pass |
| Bag remove | Open Bag and remove an item | Item is removed and total updates | Pass |
| Checkout | Add product, open Checkout, submit valid order form | Paid order is created and success page loads | Pass |
| Currency | Check Shop, Product Detail, Bag, Checkout, and Stripe currency setting | Prices display in euros and Stripe uses `eur` | Pass |
| Review create/update | Open product review form as logged-in user and submit review | Review is saved and visible on product page | Pass |
| Review delete | Click Delete review as review owner | Review is deleted without admin access | Pass |
| Progress post create | Open Community and create a post | Post appears on community page and points are awarded | Pass |
| Progress post update | Edit an owned community post | Updated content is saved | Pass |
| Progress post delete | Delete an owned community post | Post is removed without admin access | Pass |
| Newsletter signup | Submit valid email and consent from homepage | Signup is saved and success message appears | Pass |
| Newsletter validation | Submit newsletter form without consent | Form rejects signup and shows validation feedback | Pass |
| 404 page | Visit a missing URL | Custom 404 page appears when `DEBUG=False` | Pass |
| Robots | Open `/robots.txt` | Robots file loads and references sitemap | Pass |
| Sitemap | Open `/sitemap.xml` | Sitemap XML loads with public site pages | Pass |

## Responsive Testing

| Viewport | Checks | Status |
| --- | --- | --- |
| Mobile | Header collapses to burger menu, profile dropdown is touch friendly, footer stacks cleanly | Pass |
| Mobile | Hero, page headers, product cards, challenge cards, and workout cards fit without text overlap | Pass |
| Tablet | Navigation, cards, forms, and footer spacing remain readable | Pass |
| Desktop | Header links, dropdown, cart icon, rank badge, and page imagery are aligned | Pass |

## Validation And Quality Checks

| Check | Result |
| --- | --- |
| Django system check | `System check identified no issues` |
| Django tests | `7 tests OK` |
| Static collection | `collectstatic --noinput` completes successfully |
| Broken currency sweep | No pound/GBP strings remain in templates or checkout currency setting |
| Template render check | Dashboard, challenges, workouts, membership, bag, and shop returned HTTP 200 |

## Known Risks

- Stripe requires real test keys in environment variables before final deployed payment testing.
- The local checkout has a development fallback when Stripe keys are not set, so final deployment should be tested with Stripe test mode.
- The Facebook business page evidence is currently a mockup, which is acceptable for assessment evidence but can be replaced with a real business page later.
