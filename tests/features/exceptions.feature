# language: en

@openfail
Feature: Acidfile should survive a write error
    When one or more copies of the inner files fail at write, acidfile
    should fail silently.

    Scenario Outline: Some write errors
        Given the following fail schema <errors>
        And an example acidfile with 2 copies
        When I write some data
        And I close the file
        And I open it again
        Then I can read the same data

    Examples:
        | errors |
        | O O X  |
        | O X O  |
        | O X X  |
        | X O O  |
        | X O X  |
        | X X O  |

    Scenario: All files fail
        Given the following fail schema X X X
        And an example acidfile with 2 copies
        When I write some data
        Then I close the file and get an OSError
