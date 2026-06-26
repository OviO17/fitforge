$gh = "C:\Program Files\GitHub CLI\gh.exe"
$repo = "OviO17/fitforge"

$issues = @(
    @{
        Title = "[User Story] Account registration and profile setup"
        Body = @"
## User story
As a visitor, I can register, log in, log out, and complete my profile so that I can access FitForge member features.

## Priority
Must Have

## Acceptance criteria
- User can register from the frontend.
- User can log in and log out without errors.
- User can update profile details from the frontend.
- Completing profile details awards points once.

## Status
Implemented and documented in TESTING.md.
"@
    },
    @{
        Title = "[User Story] Product browsing, bag, and checkout"
        Body = @"
## User story
As a customer, I can browse products, add items to my bag, and checkout so that I can purchase fitness products.

## Priority
Must Have

## Acceptance criteria
- Product list and detail pages display active products.
- Bag supports add and remove actions.
- Checkout creates paid orders and line items.
- Prices display in euros.

## Status
Implemented and documented in TESTING.md.
"@
    },
    @{
        Title = "[User Story] Daily challenges and reward points"
        Body = @"
## User story
As a member, I can complete daily challenges so that I can earn reward points and improve my rank.

## Priority
Must Have

## Acceptance criteria
- Daily challenges display on the frontend.
- Completing a challenge awards points once.
- Completed challenges move behind available challenges.

## Status
Implemented and covered by automated tests.
"@
    },
    @{
        Title = "[User Story] Workout library and premium membership"
        Body = @"
## User story
As a member, I can complete workouts and unlock premium workouts with membership so that I can progress my training.

## Priority
Should Have

## Acceptance criteria
- Workout library displays active workouts.
- Workout completion awards reward points.
- Premium workouts require active membership.
- Advanced premium workout exists for progression.

## Status
Implemented and documented in TESTING.md.
"@
    },
    @{
        Title = "[User Story] Community progress CRUD"
        Body = @"
## User story
As a member, I can create, edit, and delete progress posts so that I control my community updates.

## Priority
Must Have

## Acceptance criteria
- Member can create progress posts from the frontend.
- Member can update their own posts.
- Member can delete their own posts without admin access.
- Other users cannot delete posts they do not own.

## Status
Implemented and covered by automated tests.
"@
    },
    @{
        Title = "[User Story] Product reviews CRUD"
        Body = @"
## User story
As a customer, I can leave, update, and delete product reviews so that I can share feedback about FitForge products.

## Priority
Should Have

## Acceptance criteria
- Logged-in users can create or update a review from the frontend.
- Review owners can delete their review without admin access.
- Product pages show submitted reviews.

## Status
Implemented and documented in TESTING.md.
"@
    },
    @{
        Title = "[User Story] SEO and digital marketing evidence"
        Body = @"
## User story
As the site owner, I can support SEO and marketing so that FitForge can be discovered and promoted.

## Priority
Must Have

## Acceptance criteria
- Meta descriptions exist in templates.
- robots.txt and sitemap.xml are available.
- Custom 404 page exists.
- Newsletter signup form exists.
- Facebook business page mockup evidence exists.

## Status
Implemented and documented in README.md.
"@
    },
    @{
        Title = "[User Story] Responsive forge-themed navigation"
        Body = @"
## User story
As a mobile user, I can navigate FitForge easily so that the app works well on phone and desktop.

## Priority
Should Have

## Acceptance criteria
- Header uses a burger menu on mobile.
- Profile links are grouped into a profile dropdown.
- Bag is shown as a cart icon.
- Current rank badge is visible in navigation and dashboard.

## Status
Implemented and documented in TESTING.md.
"@
    }
)

foreach ($issue in $issues) {
    $url = & $gh issue create --repo $repo --title $issue.Title --body $issue.Body
    $number = ($url -split "/")[-1]
    & $gh issue close $number --repo $repo --comment "Implemented during FitForge development and recorded in the project documentation/testing evidence."
    Write-Host "Created and closed $url"
}
