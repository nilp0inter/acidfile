# language: en

Feature: The number of copies of inner-files must be configurable
    As a programmer i'd like to configure the number of inner-copies of the data
    that would be written.

    Scenario: One inner file is not possible
        Given an example acidfile with no copies must raise on init
        
    Scenario Outline: Inner-file copies
        Given an example acidfile with <number> copies
        When I write some data
        And I close the file
        Then I can see <number> inner-files

    Examples:
        | number |
        | 1      |
        | 2      |
        | 3      |
        | 4      |
