# Created by jkwak at 8/27/24
@task
Feature: Profile Edit Input Function Test
  # Test the function to edit input information on profile.

  Scenario: User can save and close after editing information in th input field on profile.
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on settings option
    And Click on Edit profile option
    And Enter some test information in the input fields
    Then Check the right information is present in the input fields
    Then Check “Close” and “Save Changes” buttons are available and clickable