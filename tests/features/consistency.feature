# language: en

Feature: Acidfile must be consistent
    The acidfile data must be discarded if the inner-file was modified
    or damaged.

    Scenario: One inner-file damaged
        Given an example acidfile
        When I write some data
        And I close the file
        And I corrupt one of the inner files
        And I open it again
        Then I can read the same data

    Scenario: All inner-files damaged
        Given an example acidfile
        When I write some data
        And I close the file
        And I corrupt all the inner files
        And I open it again
        Then I can't read any data
