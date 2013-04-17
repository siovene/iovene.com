date: 2006-12-15 13:36:12
slug: 5-svn-best-practices
title: 5 SVN best practices
category: Software
tags: versioning

Versioning systems like CVS, [SVN](http://www.iovene.com/please-drop-svn/) or
[Darcs](http://www.iovene.com/darcs-the-source-code-management-system-of-the-future/)
are very important tools, that no serious programmers can omit to use. If you
started a project without using any versioning tools, I really recommend that
you start using one immediately; but I'm not discussing this right now.

I would like to point your attention to some best practices that I recommend
when working in a team.

 1. _**Don't use versioning like it were a backup tool.**_

    I've heard this question too often: "Have you put your code safely on
    SVN?".  That's a bad question. Storing code to an SVN server is not meant
    for safety, i.e. for fear of losing it. You are talking about something
    else, and that's called backup. Take Darcs, a not so popular versioning
    system. It can start without a server, and you can just run it
    locally on your machine without launching any daemon whatsoever. A
    faulty hard drive can still make you lose all your work, of course.
    That's why you have to do backups, of course, but they don't have
    anything to do with versioning. Hence, committing to the repository
    once a day, before taking off home, e.g., is not an acceptable
    practice, _especially_ if you work in a team. Doing that would be
    like making a daily backup. An SVN commit, instead, has to have a
    meaning of some sort, not just "Ok, let's store to the SVN server
    the work of today". Moreover, sometimes, if the schedule is tough
    and the cooperation is tight, you need to commit very often so your
    peer will keep up with you all the time, and not just find out, at
    evening, that he's got dozens conflicts after checking out your
    code.

 2. _**Commit as soon as your changes makes a logical  unit.**_

    How often should you commit? Theres no such thing as committing too often,
    or too rarely. You should commit each time your changes represent a logical
    unit, i.e. something that makes sense. Usually that happens because you're
    following a plan, when coding (because you are, aren't you?). So, you find
    out a bug in the trunk, plan a strategy about how to fix it, fix it, and
    then commit. This makes sense because that's a commit that fixes a bug. So
    that revision X is buggy, while revision X+1 is not. Don't be shy about
    committing too often.  Should you just find an insignificant typo in a
    debug string, or in a comment, don't be afraid of committing just to fix
    that. Nobody will be mad at you for being precise. Consider the extreme
    situation in which, after months and months, you may want to remember "What
    was the revision where I fixed that typo in that debug string?". If you
    dedicated one signle commit for the actual _finite_ logical unit of
    correcting the typo, you can just scroll back your changelog and find it.
    But what often happens, is that people will be doing something else, and,
    while doing that something else, will notice the type, and correct it, and
    basically merge that correction with the rest of the commit, making
    that thing losing visibility. To make it simple: your SVN comments
    shouldn't explain that you did more than one thing. If your SVN comment
    looks like "Fixing bugs #1234 and #1235" or "Fixing bug #4321 and
    correcting typo in debug sting" then you should've used two commits.

 3. _**Be precise and exhaustive in your commit comments.**_

    The second most annoying thing ever is committing with blank comments. If
    you're working in a team, your peer developers will be frustrated about it
    and possibly mad at you, or will label you in a bad way; possibly publicly
    humiliate you. If you're working alone, you will experience what you're
    hypothetical development companions would have: frustration in not being
    able to easily track down what a certain commit did. Comments in commits
    are important. Please be precise and explain in detail everything you did.
    In the optimal case, I shouldn't need to read your code.

 4. _**Never ever break the trunk.**_

    This is probably the most annoying thing when dealing with people who can't
    use versioning. Breaking the trunk is an habit that will quickly earn you
    the hatred of your colleagues. Think about it: if you commit a patch that
    breaks the trunk, and then I check it out, what am I going to do? The
    project won't build so I either have to fix it, or come to your desk and
    complain to you. In both cases I'm wasting some time. And consider the
    first case again: what should I do after fixing your broken code? Commit
    it? Sending you a diff? If I'll commit, chances are that you'll have
    conflicts when you checkout, and you'll have to waste time in resolving
    them. Maybe sending you a patch would be the best way, but still it's a
    waste of time for the both of us. So the thing is: before committing,
    ALWAYS double check! Make a clean build and make sure that it builds. And
    don't forget to add files! It's a very common mistake: committing good
    code, but forgetting to add a file. You won't realize, because the thing
    builds, but when I'll checkout, I'll have troubles, because of missing
    file(s). If you're using Darcs, just make a "darcs get" in a new directory,
    and then build.

 5. _**Branch only if needed.**_

    There are some ways to handle branches, but here's my favorite. The most of
    the work should happen in the trunk, which is always sane, as stated by the
    previous practice, and the patches should always be small, so that they can
    be reviewed very easily. If you find yourself in the situation of needing
    to write a large patch, then you should branch it. In that way you can have
    small patches that will break your branch over the time, but they can be
    easily reviewed. After the process is completed, i.e. you've achieved your
    goal of fixing a bug or implementing a new feature, you can test the branch
    thoroughly, and then merge it to the trunk.
