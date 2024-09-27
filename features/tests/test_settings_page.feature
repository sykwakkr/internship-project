# Created by jkwak at 9/24/24
Feature: Setting page verification
  In this feature, we will verify if Setting page appears with correct elements and connections

  Scenario: User can save and close after editing information in th input field on profile.
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on settings option
    Then Verify the right settings page opens
    And Verify there are 12 options for the settings
    And Verify "Connect the company" button is available