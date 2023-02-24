# Test-driven development

TDD operates in loop known as "red-green-refactor" and is driven by the following rules:

1. Only write production code in order to make a test pass.
2. Only write enough of a unit test to fail.  "Doesn't compile" is a failure.
3. Don't write more production code than you need to make the test pass.

It works in three phases:

1. [RED] - Write a minimal failing unit test.
2. [GREEN] - Write just enough production code to make the test pass.
3. [REFACTOR] - Refactor your production code AND your test code.  Run the tests during this process


# Pair programing

You can couple TDD with pair programming.

1. Dev 1 and Dev 2 discuss the overall design.
2.  Dev 1 and Dev 2 discuss what bit of functionality they want to address first, and how it's going to be built.
3.  Dev 1 writes a failing unit test
4.  Dev 2 writes the code to make the test pass.  
5.  Dev 1 is responsible for "navigating" as needed.  This includes:
  * Keeping track of the design
  * Looking for opportunitites to refactor the design
6.  After the Red-Green-Refactor loop, the partners switch roles and go to step 2 above.


# Bowling game:

* https://github.com/ardalis/kata-catalog/blob/main/katas/Bowling%20Game.md
* Rules and Calculator - http://www.fryes4fun.com/Bowling/scoring.htm
