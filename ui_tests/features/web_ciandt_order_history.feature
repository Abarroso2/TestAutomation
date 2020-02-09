@web @ciandt
Feature: Order History

   As an user logged i want to navigate to Order History page
   Acceptance criteria: the page Order History should display the options 

    Scenario: My account
        Given web address "http://automationpractice.com/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to my account page
        When i navigate to my order history
        Then i should be able to see my order history page