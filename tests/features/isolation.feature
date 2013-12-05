# language: en

Feature: Acidfile must be isolated
    The latest version of the data must be retrieved if two valid inner-files
    were found.

    Scenario Outline: First inner-file not updated
        Given an example acidfile
        And an auxiliary acidfile
        When I write some auxiliary data
        And I close the auxiliary file
        And I write some data
        And I close the file
        And replace example inner-file number <number> with auxiliary one
        And I open it again
        Then I can read the same data

    Examples:
        | number |
        | 0      |
        | 1      |
