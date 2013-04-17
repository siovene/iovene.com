date: 2007-01-13 23:54:40
slug: how-to-write-robust-code
title: How to write robust code
category: Software
tags: coding, design

_As software is one of the most important issues in our era, writing good
robust programs is essential. This article is an in-depth essay focused on
Object Oriented software and large projects. Everything said here, though,
scales well to good directives for small projects as well._

Our time is dominated by software. There is basically software everywhere
around us; most of the object you can see right now around you, have something
to do with software, probably because they were created using some sort of
machine. Given the importance of software nowadays, I just have to find bugs
unacceptable. Of course you might argue that a small and rare bug is a minor
software won't harm anyone, and is not nearly as important as a bug that could
affect the software of an airplane, and I'm going to agree with that. But as
time goes by, everything has to be going towards perfection, and current trends
about software seem to be going nowhere: there were bugs in software 30 years
ago, and there are today. There was a time, in the beginning, where scientists
thought that it would be relatively easy to write bug free programs right away,
but then they realized pretty soon that it wasn't quite so. After all, software
is written by us human beings, and we are doomed to make mistakes or omissions.
The point of this article is not that software should be always bug free, but
that we, coders, should always get them to the minimum, and here I'm going to
present some ways to deal with programming in general.

One huge problem, as I've faced quite often, is that as a program grows in size
and dependencies, its developers start losing trace of its components, get
further away from the big picture, and ease the introduction of bugs. Note, I'm
not talking here about bugs caused by a single human error that can be labeled
as a cheap error by anyone who would look at the code. I'm talking about the
sort of nasty bugs that nobody can spot right away with a glance at the code.
I'm talking about system wide bugs, usually emerging as a result of hardly
related subsystems of the program. Usually connections between dependencies and
libraries.

Anyway, the path to write bug free code, is the one you step when you write
_robust code_. What do I mean by that? Robust code has some features:

  * Well designed
  * Neat and tidy
  * Well named
  * Well commented
  * Well tested
  * It **never** segfaults

As a result of some of these, robust code is also:

  * Exstensible
  * Reusable
  * Lasting in time


### Well designed.

Having already talked about this [somewhere
else](http://www.iovene.com/content/view/92/34/), I'll be brief on this
section. Writing a complex program, a program made of hundreds of thousands
lines of code, is a _damn complicated thing_: it takes many people and a
lot of time. Usually, the more people you involve in the project, the less
robust code you'll get in the end. People will use different conventions
and different styles. For this reason, not only it's crucial to hire the
right developers, but it's essential to have a _very strict_ and detailed
specification of the project. Programming is a creative work, no doubt, and
coders need to have freedom so they can breathe. A constrained coder is a
chained coder, hence a dead coder and a threat to the quality of the end
product. But, in spite of how much we care for the freedom and openness of
initiative from the developers, we have to be aware that loosing control
means lowering the quality. A large project must be designed thoroughly and
carefully, in every single details. Even though programmers love freedom,
most of them also love exhaustive documentation. If you want to make a good
coder happy, and get the best out of him, flood him with docs and specs.
Nothing pisses off the good coder as the lack of documentation: it tears
his motivation apart. "Why should I start to read their minds and run by
guesses" - he thinks, "when they didn't even get the time to write good
specs?". Furthermore, a project without good specs looks superficial,
destined to failure and without a future. A very good coder is hardly going
to stay in a company that doesn't make good design for the projects. He
will think that it's a loser company, and start looking around.

But what does _good design_ mean? A good design is:

  * Exhaustive
  * Non redundant
  * Non contradictory
  * Easy to understand
  * Related 1:1 to the implementation

We want to cover every possible outcome in our specification, let be them
**exhaustive** so that nothing will be left to case. We don't want to repeat
the same information more than once, and be **redundant** for several reasons,
e.g. information should be retrievable in exactly one place, and it would ease
up **contradictions**. Documentation should be _for the developers_, i.e.
written in the most straightforward way for the right audience: **simplicity**
of language and straightforwardness of tables and schemes will spare some
curses from the developers. Furthermore, as a specification is just a way to
put a program in words before it's written, developers should be easily able to
translate what they see on paper to code. Think about a shopping list: when I
get one, I just go to the shop and take care of _translating_ each item on the
list to a physical item in my shopping cart. Direct and easy.


### Neat and tidy

A good definition of [neat](http://dictionary.reference.com/browse/neat) is:
_in a pleasingly orderly and clean condition_. How does that apply to software?
What is neat software? One nice word that I like in that definition is
"pleasingly". Neat software pleases the eye and the mind. Don't want to be
cocky here, but neat software is something written by a good programmer, and
will be appreciated by another good programmer. If somebody known as a good
programmer points at some software and says "That's neat" and you find yourself
looking at it and replying "Huh? That's just code", I'm sorry but chances are
that you are not a good programmer. A good programmer appreciates the beauty of
some code, both on a small scale and on a large scale. Neatness of software on
a small scale means that you're able to look at one function and appreciate the
simplicity of it. Neat pieces of code are easily readable and use good name
conventions. Please [read this
article](http://www.iovene.com/content/view/87/34/) if you want to know more
about good code on a small scale. Neat code on a larger scale, on the other
hand, means neat integration between components and subsystem of a project. A
_**bad**_ integration would mean, e.g., having a project-wide global variable
that points to a certain subsystem, and using it everywhere in the project. Or
having two subsystems that, in a messed and intertwined way, mutually call each
other's methods [violating several layers of
abstraction](http://www.iovene.com/content/view/89/34/). Proving what neat code
is, turns up to be very difficult. It's a bit like the opposite of what happens
with common logic: if I want to prove you that, say, lions exist, I can just go
to Africa, pick one and show it to you, then say "That's a lion, ergo lions
exist". But how can I prove that unicorns or dragon don't exist? You probably
agree that it's much more difficult. It's just the opposite with neat code. I
can show you bad code, and you will easily agree that it's bad. But looking at
neat code doesn't it prove it neat right away. It takes probably years and
years of experience, writing a lot of code and reading a lot.


### Well named

This topic [has already been discussed
here](http://www.iovene.com/content/view/87/34/), but _repetuta juvant_. As
code is managed by possibly dozens or more people, being understood is an
important key to increase robustness of the code. Writing robust code also
means writing code that will easily _stay_ robust when other people will modify
of expand it, unless they have no clue, of course. The most your code is
understood by others, the most likely they will not break your ideas, and keep
the code robust. There are several ways of making own code easily understood,
and having a good, consistent and solid naming convention is one of them. Of
course, as discussed later, code needs to be well documented also.


### Well commented

I know, I know. Everybody says that you should comment your code. That's what I
say and that's what I've been told. Still I'm now comment my own code enough as
I should. Before you can then tell me "Who are you, then, to tell me to comment
my code, if you don't do it enough with yours?" let me remind you that we learn
from mistakes. What they don't tell you about the importance of commenting
code, is some subtle and psychological little thing. If you are a bad
programmer, you'll never produce good code. But if you are a good programmer,
sometimes being in a hurry will make you produce really bad code. There are two
reasons why this can happen: 1) you are in a hurry because you're late with
your deadlines. With this, there's nothing to do. 2) you are in a hurry because
you're just coding fast, on the rush of some ideas that flashed you. In this
case, commenting your code a lot will improve drastically the quality of your
code. Always write your comments _before_ writing the actual code. This will
make you realize it, if your function is not really going to do what it's
supposed to do. Writing the comment will also help you think more about what
you're doing, and being more conscious about it. It will keep your state of
mind clear and precise. I **strongly** recommend using [Doxygen](
http://www.stack.nl/~dimitri/doxygen/) to generate a browseable HTML  version
of your comments, especially if you're writing a library. Otherwise, it's still
going to keep you on a [professional
line](http://www.iovene.com/10-advice-to-write-good-code/), which is always a
good thing.


### Well tested

Write and use unit tests. If your code is well designed, there are good chances
that each function in your code, or each class, performs a specific task in a
certain way, and nothing more. Given a certain input, it will reliably return
the same output. Right? You have to make sure of that, by writing test cases.
Testing the smallest units of your program doesn't ensure that the whole is
working perfectly, but helps. Possibly, append a hook to your Source Code
Versioning System ([SVN](http://subversion.tigris.org/)?
[Darcs](http://www.darcs.net/)?) so that the automatic testing suite will run
automatically on the server that hosts your repository, before it accepts your
patch. This is [quite easy with
Darcs.](http://darcs.net/DarcsWiki/BestPractices#head-48bc026efc0313f4a3889860012a3cfbcb8af484)


### It never segfaults

Of course this point applies to the languages that allow segmentation fault, or
NullPointerException (in Java). It's easy to get: if your code segfaults, there
are no excuses. No matter how stupid the provided input was, your program
should not segfault. A good practice, is that each and every function/method
would check it's argument before doing anything. A solid exception handling
structure is required. Again, you can object that I'm not really saying
anything useful here: "Of course programs shouldn't segfault, I knew it!", but
think about it: it's a matter of attitude. You want to write a _perfect_
program, and there are some things you have to keep in mind. Be **paranoid**
with segfaults will implicitly and secretly improve the general quality of your
code, without you even noticing.


### Conclusion

Writing perfect code is impossible. Especially as the code grows in size and
number of programmers. Achieving the impossible, then, is beyond any good
intentioned coder. What we can do, though, is just _try_ to have the right
attitude, which is about precision, care and, sometimes, paranoia. Writing
complex programs is not an easy thing, and, as such, should be handled with
extreme care.
