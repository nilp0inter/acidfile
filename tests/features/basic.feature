# language: en

Feature: Basic file usage
    In order to use the package as developer I need to write and read
    data from the file.

    Scenario: Read and Write
        Given an example acidfile
        When I write some data
        And I reopen it
        Then I can read the same data
