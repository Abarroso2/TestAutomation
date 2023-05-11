@web
Feature: Buying a dress
    As an user previously singed in, i want to add a dress to the cart
    I want to proceed with the order
    Acceptance criteria: i must be able to finish the order and see the order finish page

    Scenario: Add a dress at the cart
        Given web address "http://automationpractice.pl/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to dresses section
        When i add the Printed Dress to cart
        When i verify the cart
        When i proceed with the shopping order
        Then i should see the order confirmation page