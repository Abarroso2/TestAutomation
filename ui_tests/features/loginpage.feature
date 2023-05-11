@web
Feature: Login page
    As a user i want to login in the website http://automationpractice.pl/index.php,
    User login "allan.barroso@outlook.com" and password newstar1541,
    The user was previously added at the system,
    Acceptance criteria the system must show the Username Allan Barroso at My Account page.

    Scenario: Login
        Given web address "http://automationpractice.pl/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        Then the site should show my account page and user name
