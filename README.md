e-Valuate
=========

Inspired by an article about [e-Valuate](http://arxiv.org/abs/1202.0862 "E-Valuate on arXiv"),
a two-player, zero-sum, sequential, perfect information game an arithmetic expressions, this
project is started.

Goals
-----

The goals for this project are two fold.

1. Use [python](http://python.org/ "Python homepage").
2. Study [alpha-beta pruning](http://en.wikipedia.org/wiki/Alpha-beta_pruning "Wikipedia on alpha-beta pruning")

Environment
-----------

Make sure to add the current project to the `PYTHONPATH`. I usually do this by execute the following command.

    export PYTHONPATH=.

Test
----

Run all the test by executing the command:

    python evaluate/test/test_all.py

Executables
-----------

You can determine the optimal value for an expression and domain by using the `evaluate` executable.

for example

    > bin/evaluate "A-B" 4

