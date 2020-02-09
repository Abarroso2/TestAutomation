@web @ciandt
Feature: Reorder 

   As an user logged i want to navigate to Order History page
   As i select an order in the history i ante to see the details
   I want to select an order in the history to reorder itself
   Acceptance criteria: the page Order History should display the orders at list and i should be able to se it's details 

    Scenario: My account
        Given web address "http://automationpractice.com/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to my account page
        When i navigate to my order history
        When i select an iten in the list and click on it datails
        When i proceed a reorder of an iten
        Then the order complete page should be displayed