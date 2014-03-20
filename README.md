# Profiling Python

Why is my code so darn slow?!?!

By Hans Lawrenz on 2014-03-20

---

# The Problem

You've just finished writing an awesome program, but it's slow as a molasses.
What do you do now?

Your first instinct might be to dig in and start slicing and dicing your code.
Making possibly-educated guesses about what might be slowing things down. In
most cases, you’re better off stifling this instinct.

---

# The Solution

The smarter thing to do is to find out exactly what parts of your program are
taking so long. This is where profiling comes in. Profiling your program will
produce several metrics for each function in your program which you can use to
find out where you need to focus your optimization efforts.

---

# Optimization Ground Rules

 * Don't do it if you don't need to.
 * Don't do it too early.
 * Be reasoned and deliberate, not arbitrary.


---

# First Steps

If you’re dealing with a simple program, you might be happy with just running
the your program cProfile and looking over the results it prints out. For example:

       python -m cProfile radscript.py


       198526 function calls (198520 primitive calls) in 0.153 seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            2    0.000    0.000    0.000    0.000 _abcoll.py:98(__subclasshook__)
            2    0.000    0.000    0.000    0.000 _weakrefset.py:16(__init__)
            2    0.000    0.000    0.000    0.000 _weakrefset.py:20(__enter__)
            2    0.000    0.000    0.000    0.000 _weakrefset.py:26(__exit__)
            2    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
            2    0.000    0.000    0.000    0.000 _weakrefset.py:52(_commit_removals)
            4    0.000    0.000    0.000    0.000 _weakrefset.py:58(__iter__)
        20071    0.006    0.000    0.006    0.000 _weakrefset.py:68(__contains__)
            2    0.000    0.000    0.000    0.000 _weakrefset.py:81(add)
        10035    0.012    0.000    0.020    0.000 abc.py:128(__instancecheck__)
          2/1    0.000    0.000    0.000    0.000 abc.py:148(__subclasscheck__)
        .
        .
        .



---

or if you wanted to sort the results:

        python -m cProfile -s tottime radscript.py

         198526 function calls (198520 primitive calls) in 0.155 seconds

       Ordered by: internal time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        10036    0.042    0.000    0.079    0.000 collections.py:495(update)
        10035    0.037    0.000    0.037    0.000 {method 'split' of '_sre.SRE_Pattern' objects}
            1    0.021    0.021    0.150    0.150 wordcounts.py:5(count_words)
       108029    0.014    0.000    0.014    0.000 {method 'get' of 'dict' objects}
        10035    0.012    0.000    0.020    0.000 abc.py:128(__instancecheck__)
        20071    0.006    0.000    0.006    0.000 _weakrefset.py:68(__contains__)
        10035    0.006    0.000    0.050    0.000 re.py:170(split)
        10035    0.005    0.000    0.007    0.000 re.py:232(_compile)
        10044    0.005    0.000    0.024    0.000 {isinstance}
            1    0.003    0.003    0.003    0.003 {_heapq.nlargest}
        10037    0.002    0.000    0.002    0.000 {getattr}
        .
        .
        .

---

Here’s what we’re looking at:

ncalls
: for the number of calls,

tottime
: for the total time spent in the given function (and excluding time made in calls to sub-functions)

percall
: is the quotient of tottime divided by ncalls

cumtime
: is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.

percall
: is the quotient of cumtime divided by primitive calls


---

# Visualizing Profiling

A better option, especially when you're working with a more complex program, is to use a tool to visualize
the program's profile. There are a few different tools you can use to do that, we're going to focus on
RunSnakeRun. To get started, we need to have the profile data in a format that RunSnakeRun can use:

    python -m cProfile -o radscript.prof radscript.py

After you’ve got that file you can open it up with our next tool,
[RunSnakeRun](http://www.vrplumber.com/programming/runsnakerun/). Whit it you'll be able to see the same basic
information that we looked at earlier, but with a graphical visualization, and the ability to drill down into
the call tree.

    runsnake radscript.prof


---

# What Now?

Now you hopefully know what parts of your program could use some work. The next step is to work out what
you can do, if anything, to speed things up. Here again, there are some tools to help you along the way:

  * [timeit](http://docs.python.org/2/library/timeit.html)
  * time (unix command)
  * [line_profiler](http://pythonhosted.org/line_profiler/)
  * Information
    * [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips) (some of this is a bit crusty)
    * [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
    * [BigO](http://science.slc.edu/~jmarshall/courses/2002/spring/cs50/BigO/) to help with time complexity.


---

# timeit

timeit is a simple module that allows you to time little bits of code. It can be useful if you're trying
to determine whether or not a different way of doing things might be quicker. For example:

        In [1]: import timeit
        In [2]: s = """\
           ...: x = []
           ...: for i in xrange(0, 10000):
           ...:     x.append(i)
           ...: """

        In [5]: timeit.timeit(stmt=s, number=10000)
        Out[5]: 7.790654897689819

        In [7]: timeit.timeit("x = [i for i in xrange(0, 10000)]", number=10000)
        Out[7]: 2.991128921508789


---

# Resources:




---

Examples:
Bulk loading data into the database
Different types of dict keys
Using more appropriate data structures
Using list comprehensions


Other topics:
Memory profiling


