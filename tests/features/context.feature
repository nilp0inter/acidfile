# language: en

Feature: Use acidfile as a context manager.
    As a programmer i'd like to use the acidfile as a context
    manager as the open can.

    Scenario: Read in context
        Given an example acidfile
        When I write some data
        And I close the file
        Then I can open in a with statement and read the same data

    Scenario: Write in context
        Given an acidfile written in a with statement
        Then I can open in a with statement and read the same data 
