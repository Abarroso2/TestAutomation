@web @ciandt
Feature: Buying a dress remove item
    As an user previously singed in, i want to add some dresses to the cart
    I want to remove one of then from the cart
    Acceptance criteria: i must be able to see the remaining dress or dresses into the cart

    Scenario: Add a dress at the cart
        Given web address "http://automationpractice.com/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to dresses section
        When i add the Printed Dress to cart
        When i add the Printed Chiffon Dress to cart
        When i remove Printed Dress from cart
        When i verify the cart
        Then only the Printed Chiffon Dress should be in the cart
