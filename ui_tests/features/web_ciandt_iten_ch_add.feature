@web @ciandt
Feature: Buying a dress
    As an user previously singed in, i want to add a dress to the cart
    Acceptance criteria: i must be able to see the chosen dress into the cart

    Scenario: Add a dress at the cart
        Given web address "http://automationpractice.com/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to dresses section
        When i add the Printed Dress to cart
        When i verify the cart
        Then the dress should be in the cart