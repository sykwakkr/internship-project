# Created by jkwak at 9/30/24
@task @continue
Feature: Secondary-listings Page Verification
  In this feature, we will verify all the elements on the page.

  Scenario: User can filter the Secondary deals by "want to sell" option
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on "Secondary" option at the left side menu
    Then Verify the right page opens
    When Click on Filters
    And Filter the products by "want to sell"
    And Click on Apply Filter
    Then Verify all cards have "for sale" page
