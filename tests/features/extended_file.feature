# language: en

Feature: Extended file usage
    Acidfile must behave like any other file-like object so all the
    not implemented method must be passed to de inner memory file.

    Scenario: Seek the file
        Given an example acidfile
        When I write some data
        And seek to the start of the file
        Then I can read the same data
