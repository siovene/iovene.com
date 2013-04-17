date: 2006-12-27 21:39:33
slug: getting-a-project-done-using-clever-design
title: Getting a project done using clever design
category: Software
tags: design

Sometimes, when coding a one-person-project at work or for fun, each one of us
has found himself stuck at some point, and then the project eventually died
out. Let's have a look at some design and discipline recommendations that can
help us achieving our goal.

Who doesn't have a dream hidden in a drawer? Some of us coders have dreams
about programs about which we've been thinking for a long time and perhaps
never found the time to write. Now that we finally decide to settle down with
it and write the thing down, we better not hurry. There are several
complications that might arise during the creation of the project and most of
them can be faced dealing with two issues: design and discipline. Let's examine
some of the possible issues.


### Technical difficulties.

Not very unlikely, at some point of the development, we might find some obscure
obstacles, impersonated by a very tough technical issue. I.e., we might think
that _it just can't be done_. Well sometimes it really can't, but usually it's
a matter of technologies and the proper use of them. To address this kind of
problem, there are basically two ways.

  1. **Read up.**

    Once you've determined what technologies you're going to use, and what
    libraries, read up about them. _"I'm going to learn them as I build up my
    project"_ is not a good strategy. You will probably realize that those are
    not the right technologies after all, or that you're not using the right
    libraries.  Or, most commonly, that you're using your things in the wrong
    way. And that could be too late. This is a very common case of project
    failure. This is when you get to face an obstacle that seems insuperable,
    so you'll waste a lot of time, and eventually get unmotivated. Start
    reading the websites of the technologies and libraries you want to involve,
    then read their documentation.  You don't need to read all the APIs of
    course, but at least you ought to read the technical overviews, the white
    papers and the general design perspectives.  Possibly, buy a book about
    them and read it. Of course this will delay the start off of your project,
    but that's better than investing 2 months in it and then have to trash
    everything. Typical case involve starting a new language, or a new
    framework. If you're new to [Hibernate](http://www.hibernate.org/) don't
    expect to just starting using it reading the Quick Start Tutorial. Most
    things, especially nowadays, aren't just about using them. It's mostly
    about understanding the big picture and knowing what the right angle from
    which approach them. The details will always come afterwards. Never ever
    underestimate the importance and the power of a good book on a certain
    matter.  After having read up enough, you're ready to start thinking about
    your application.


  2. **Design.**

    Never fail or omit to design your application (thoroughly) before hands. It
    might seem silly for small applications, but it never is. Draw down a
    scheme of the main components of the system, and remember: always _divide
    and conquer_.  Start by drawing off a very big picture of the system. Ask
    yourself what components are involved, what technologies you're going to
    use, what libraries you're going to integrate. Once you have a _clear and
    state-of-the-art_ idea of what the big picture is, you can start adding
    details. You can plan your database, for instance. Start that by
    individuating what the main components are, and how they interact with each
    other. Then you're ready to design the database in more detail, i.e.
    specifying each field and relation. That will also help you entering more
    detail into the big picture of your application design. Start now
    considering all the components and their interactions. Define the objects
    you need and the way they communicate. Draw models and objects, possibly
    using [UML](http://www.uml.org/). Be very careful and see to it that your
    model makes sense. Glitches and problems might (and should) already come up
    at this point. If your application takes less than 6-12 hours to be
    designed, than it's either very simple, or you're being superficial. Of
    course if we're talking about `Hello World`, then you don't need that much
    design, but this should be clear already!


If you've taken care of all this, the odds are with you and there are very
little chances of failing for technical issues. Now it should just be about
writing the actual code and you already know that _it can be done_, because you
read up and designed the thing properly.


### Scattered code

Although _Spaghetti Code_ was The Way, some long time ago, Object Oriented
Programming has now been out there long enough so that we all should be able to
write decent Object Oriented code. Seriously, if you're still writing
procedural Spaghetti Code, you should really read some Object Oriented
Programming books and start living in the present. If you don't even know what
Spaghetti Code is, chances are that it's what you do, so [Google it
up](http://www.google.com/search?q=spaghetti+code&ie=utf-8&oe=utf-8&rls=Swiftfox:en-US:unofficial&client=firefox-a).
Having well structured, layered and maintainable code will help you write less
code, write better code, and finish your project sooner. This should come out
automatically from a good design, but it's worth spending some words. The more
you are able to do the following, the better your project will go on: write a
class, double-check it, test it, never touch it again. This is the _divide and
conquer_ paradigm. Once you have some parts of your project that are actually
_finished_, you will find a lot more motivation in continuing. Having to
continuously modify parts of your code, going back and forth on those changes
again and again, is not only frustrating, but damaging the very structure of
your project. I'm sure you have run through more that one session of
"refactoring" your code. Moving pieces around, redesign classes, putting order,
etc. This means that you're wasting time that you could've used on adding new
features or getting close to something that's releasable.


### Lack of deadlines

Even if you're working alone on an hobby project, set yourself deadlines and a
roadmap. Reserve yourself some time each day in which you can work at your
project. If you already know what version 0.3 will have, and what version 0.4
will look like, it's more likely that you will stick to that. Give yourself
small objectives and follow them, one after the other. Don't push yourself too
much, though.


### Lack of professionalism

This is a very important point, even though you may think it's not. Even if
you're working all by yourself, whether it is a work project or a hobby one,
always be professional. Remember the following rules.

  * **Use a source versioning system.**

    I don't care if it's CVS, SVN, Darcs, GIT or one of the many out there. Use
    one. Commit your work and keep track of the changes. This will not only
    help you not lose important code, and keep your work traced down correctly:
    it will also give you discipline and motivation. Read some best practices
    for SVN and other versioning systems.

  * **Use a bug tracker.**

    There's a vast choice: [bugzilla](http://www.bugzilla.org/),
    [trac](http://trac.edgewall.org/) and [the Bug
    Genie](http://bugs-bug-genie.sourceforge.net/) are only few of them. Bug
    tracking is terribly important. Maybe not in the very initial phase of your
    project, but as it becomes usable, bug tracking can't be neglected. Even if
    you're working alone. Track the bugs scrupulously and like you were working
    on the most important project of the World. Bugs tend to be forgotten of
    after few hours. Few days in the best case. This is also something that
    will keep you motivated. Acting professionally.

  * **Keep a website and build up a community.**

    I assume that your project would be interesting to someone. The most
    motivating thing ever, is receiving encouragement and feedback from
    strangers. Keep a website of your project and let the community know what's
    going on. Release it as soon as it's ready and you'll get feedback,
    eventually help. This is really highly motivating.


### Lack of discipline

Another big hit for unfinished projects. Stay away from it for more than 1
months, and it's over. Most of the times. After one month, you will have
forgotten a lot of things about it, and just can't get the focus again. Just
can't find your way through it again. The more the time goes by, the more
you'll get detached from it, and it will eventually end up in the well of the
forgotten and unfinished projects. To find the right discipline, force yourself
to keep an eye on it at least two times a week, for 2 hours each time. Of
course, this depends highly on how much you care about finishing your project,
but of course we're discussing this assuming that you care a lot.

Keep all of these hints in mind, and with a good dose of determination you can
accomplish everything.
