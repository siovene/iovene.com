date: 2006-12-14 14:58:17
slug: 10-pieces-of-advice-to-write-good-code
title: 10 pieces of advice to write good code
category: Software
tags: coding, design

Having been coding for 16 years now (I started quite young), I have seen a lot
of bad code. Code is not good just because it works. So here's a quick list of
10 advice that you'd better keep in mind while coding.

 1. _**Don't sacrifice code maintainability to performance, unless it's
    strictly necessary.**_

    This happens very often. You have to consider that your code is likely to
    be read by many persons, and some of them will read it after you might have
    parted from that company. Remember that you won't remember what your own
    code does after few weeks. So always try to put things in the most readable
    and obvious form, even if this will require writing more lines of code, or
    having less performing code. Of course this is not so important if
    performance is your number one issue. Try, for instance, to avoid use of
    the `?:` operator in C/C++. Everybody will understand it anyway, but a good
    old `if` statement will do it, so why not going for it?

 2. _**Be precise as a Swiss clock, when it comes to naming conventions.**_

    Nobody wants to read class names or variable names that look like
    gibberish.  Don't be mean on the keyboard: when you type, remember that
    somebody else will have to read it, so be extensive.

    1. Name your variable `NumberOfItems` rather than `items_n`. Don't use
       cryptic prefixes to class name. Name your class
       `ClientMessageOperationsBasicFunctor` rather than `CMOpFunctor`. It's a
       lot more typing for you, but a lot less hassle reading for the ones that
       will come after you.

    2. Don't change your conventions. If you're calling the iterators `i`,
       don't call any of them `n`, _ever_. You will induce confusion to your
       reader. It doesn't seem as important as it actually is. If you call a
       class `ClientMessageBlockContact`, then do not have
       `ServerMessageContactBlock`.  Be perfect, be precise, be obsessed.

 3. _**Use a good and consistent indentation style.**_

    Never ever have more than one blank line. Don't have trailing spaces at the
    end of the lines. Don't have blank spaces or TAB characters in blank lines.
    A blank line must be blank, that is.Be consistent: don't use TABs to indent
    in one file, and spaces in another one. Possibly, use 8-chars wide TABs to
    indent. If you find yourself going beyond 80 rows too often, then that
    could be an indication that there might be some design flaws in your
    program. Tweak your editor to show you the end-of-line character and the
    TABs.

 4. _**One class, one file.**_

    Don't write files like `ServerMessages.h` where you write all the class
    that are `ServerMessages`. One class goes in one file. If you find yourself
    thinking that you can't do it, review your design.

 5. _**In C/C++, project includes use "", dependency includes use <>.**_

    If you're including a file that's local to your project, `use #include
    "file.h"`; if it's an external dependency, do `#include <file.h>`. Why?
    I've seen people including `<file.h>` and then just put things like
    `/usr/includes/my_project` in the inclusions search path, so that nobody
    will be able to compile before installing. That's a bad assumption. And you
    don't want to end up in that error.

 6. _**Always compile with `-ansi -pedantic -Wall -Werror` flags (or similar,
  according to your compiler).**_

    Let's adhere to standards. Let's avoid warnings. A warning might become an
    error in the future.

 7. _**Use TODOs and FIXMEs.**_

    If you know that you, or somebody else, will have to return on a certain piece
    of code to add or modify some functionality, please mark it with a TODO. If
    you know that a piece of code is buggy but you can't fix it right now, add
    a FIXME marker. Later on, it will be easy to grep the source tree for TODOs
    and FIXMEs and analyze them, especially if they're very well commented.

 8. _**Comment your own code. **_

    Seriously: you're going to forget, sooner than you think. Just invest 5% of
    your time in writing commented code. Never assume that code is
    self-explanatory, just write a couple of lines for everything you do.
    Comments are not only meant to generate doxygen documentation. You have to
    assume that somebody else will read your code and need to modify/extend it.

 9. _**Use a versioning system even if you're working alone. **_

    Yes, versioning is not just for working in a team. Use
    [Darcs](http://www.darcs.net/) or [SVN](http://subversion.tigris.org/)
    even if you're working alone: you won't regret it. Commit often and try to
    be professional all the time. Later on somebody else might join you. Or
    then you might find useful to revert to previous versions of your program.
    And it will help you to keep trace of what you're doing.

  10. _**Use a bug tracking system even if you're working alone. **_

    Things like Bugzilla are EXTREMELY useful. Usually you will forget bout a
    bug after less than 2 days. Everytime you find a bug, either fix it
    immediately, or mark it to your personal bugzilla. And always fix bugs
    first, and then write new code.


### Common errors

  * It compiles, so it works.
  * It works here, so it works everywhere.
  * Commenting? We don't have time to waste, we gotta ship!
  * Plan code so that we can reuse it is useless: we'll end up writing
    everything from scratch anyway.
  * Unit tests are a waste of time.
