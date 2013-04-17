date: 2007-05-14 14:21:33
slug: tabs-vs-spaces-the-end-of-the-debate
title: TABs vs Spaces. The end of the debate.
category: Software
tags: coding

When writing source code, **indenting** is very important. [Having a neat and
clean programming](/posts/2007/01/how-to-write-robust-code/) style, let alone a
_precise and uniform_ one, is probably one of the most important keys when
attaching example source code with a job application. I was myself asked to
show some of my source code in my last two interviews. Nobody ever asked me to
show any _running_ program that I had made, though. Wonder why? A lot can be
understood about the author just by glancing quickly at some source code.

_Indenting_ makes the source code easier to read for us human beings, whereas
the compiler doesn't really care (except for some languages, where indentation
applies as a syntax element). Even if you're not a programmer, you can see the
differences here:


#### Compiler friendly

![Compiler
readable](|filename|/images/2007_indenting_1.jpg)


#### Badly indented

![Badly
indented](|filename|/images/2007_indenting_2.jpg)


#### Properly indented

![Properly
indented](|filename|/images/2007_indenting_3.jpg)

There is, I guess, no question that the last one, labelled as "Properly
indented", is the most readable. Problem arise, though, when people start
wondering what they should use as indenting character. Some prefer TABs, other
prefer blank spaces. A TAB, the key on the left of the Q of most Qwerty
keyboards, is a single character that a text editor can represent whatever way
it wants. This is usually customizable by the user, of course, so she can
decide that a TAB will be shown as 8 spaces, or 4, or 2.

You can hear all the time someone claiming, in turn, that **TABs are evil** or
that **spaces are evil**, but the truth is that none is wrong, as long as you
can indent.

I'll use, as an example, a piece of source code taken from the ext3 module of
the Linux kernel. The Linux programming guidelines recommend using TABs for
indenting, and that they should be 8 spaces wide. Let's have a look at some
code.


#### 8-space TAB

![8-space.jpg](|filename|/images/2007_indenting_4.jpg)


#### 4-space TAB

![4-space.jpg](|filename|/images/2007_indenting_5.jpg)


#### 2-space TAB

![2-space.jpg](|filename|/images/2007_indenting_6.jpg)

As you can see, the original intent of the author, was to have the variable
names aligned. But that alignment gets screwed up as soon as a reader has a
different space-size for her TABs. What's wrong there? Let's use **a very
useful Vim tip**: the **:set list** command.


#### :set list
![set-list.jpg](|filename|/images/2007_indenting_7.jpg)


This way, we can actually _see_ the TABs, as ">-------". Of course there will
be less dashes if part of the TAB area is occupied by some text. So, can you
see what's wrong with that? The author of that source code is using TABs not
only for indenting, but also for aligning! That way his alignment gets messed
up when somebody uses a different TAB size. The solution of this problem is to
simply just **use what ever you want for indenting, but use spaces for
aligning**. Indenting must only be that _left margin_ that you give to some
lines, but it's not to be confused with alignment. If the author of that source
code had used TABs at the beginning of the lines, but just blank spaces between
the _type_ and the _name_ of the variables, his code would be as he meant it
whatever indenting style one's editor would use.

So, in the end, it doesn't matter whether you use TABs or space, for
**indenting**, as long as you use just spaces for **aligning**.


#### Useful Vim/Emacs tip

I like spaces, and add the following to the end of all of my source files:

    /*
    Local Variables: mode:c++ c-basic-offset:2 c-file-offsets:((innamespace .
    0)(inline-open . 0)(case-label . +)) c-tabs-mode:nil End:
    */
    // vim: filetype=cpp:expandtab:shiftwidth=2:tabstop=8:softtabstop=2


This way, if the reader uses Vim or Emacs (and maybe also gedit), her settings
will be temporarily overridden by mine, so, if she's going to change my code,
there are little chances that she'll mess up my indenting.

The **:set line** options I use are the following:

    set listchars=tab:>-,eol:$,trail:.,extends:#

It helps me to also spot trailing spaces. I recommend everybody to use the
**:set list**, as it will prevent you to accidentally mess up other's
indentation.
