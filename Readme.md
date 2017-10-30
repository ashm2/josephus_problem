Josephus Problem
================

This app takes in 2 parameters: the number of people in the circle (n) and the step rate (k).
For example, if k is the step rate, then you skip k-1 people and eliminate the kth person.
The output of the program shows the place(index) to stand in the circle
where the last person is left.


Run the following commands to get started
=========================================

Set up a virtual environment
https://virtualenv.pypa.io/en/stable/

$ cd josephus_problem

$ virtualenv env

$ source env/bin/activate

$ python setup.py develop

Start the app
=============

Type the following command for help
$ run [-h]

$ run n k
n is the number of people in circle and k is the step rate

Example:
$ run 12 2

should produce an output
$ The index position of the survivor is 8


Run tests
=========

$ pytest


