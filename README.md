#Python Parsing Shenanigans

Do you want to do Python-based DSLs? Well, here's a nice way to implement it:


    # coding: my-dsl
    "ih" tnirp

You implement a Python string codec called "my-dsl" which parses your DSL and
emits Python source code. Now, instead of having to deal with import hooks to
use your DSLs, you only need to care about the source-to-source translation.
