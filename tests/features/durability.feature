# language: en

Feature: Acidfile must be durable
    The acidfile data must survive even if one of the inner files that
    support it is deleted.

    Scenario: Inner-file deleted
        Given an example acidfile
        When I write some data
        And I close the file
        And I remove one of the inner files
        And I open it again
        Then I can read the same data

    Scenario: All inner-files deleted
        Given an example acidfile
        When I write some data
        And I close the file
        And I remove all the inner files
        And I open it again
        Then I can't read any data
