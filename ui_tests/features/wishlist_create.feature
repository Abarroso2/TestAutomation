@web
Feature: Wishlist
    As a user i want to create a Wishlist
    Acceptance criteria I should able to create a wishlist

    Scenario: Wishlist
        Given web address "http://automationpractice.pl/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to wishlist
        When i create a new wishlist
        Then the wishlist should be created