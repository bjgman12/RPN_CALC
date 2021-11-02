# RPN_CALC

> Most Recent Pull Here 

#### Authors : Brandon Gonzalez
#### Created 29 October 2021
#### Version 0.1


## Description 

> This module is an implementation of a RPN Calculator ( Reverse Polish Notation), a calculator in which operators follow their operands

> RPN calculator info [RPN WIKI](https://en.wikipedia.org/wiki/Reverse_Polish_notation)


## Features and Requirements

- Calculator should use standard input and output

- implement 4 standard arithmetic operators

- handle errors and recover gracefully

- exit on `q` , or end of input ie `Ctrl+C`

# Approach

> This calculator uses a CALC class to instatiate an Actor as well as start whichever calculator the actor wants to use RPN only for now but room to add different type of caclulators or even differenc command line tools.

> method start_math_engine starts up a recursive loop of tkaing in inputs and running them through basic arithmetic functions until explicitly told to exit.

## USE

- clone repository
- install dependencies
- run calc.py

## ChangeLog

- currently takes all single input queries
- takes 2 operands then one operator
- takes 2 operands and one operator


## Testing


- [x] Arithmetic functions testes
- [x] Mock input testing 
