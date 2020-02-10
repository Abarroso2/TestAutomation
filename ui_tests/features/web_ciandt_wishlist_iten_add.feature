@web @ciandt
Feature: Wishlist
    As a user i want to create a Wishlist
    Acceptance criteria I should able to create a wishlist

    Scenario: Wishlist add iten
        Given web address "http://automationpractice.com/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to dress session
        When i select a dress and add it to wishlist
        When i select a second dress and add it to wishlist
        When i navigate to the wishlist
        Then the itens should be in the wishlist