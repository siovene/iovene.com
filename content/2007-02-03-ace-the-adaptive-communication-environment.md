date: 2007-02-03 14:44:35
slug: ace-the-adaptive-communication-environment
title: ACE: The Adaptive Communication Environment
categories: Software
tags: ACE, review

For some time, in the last months, I have been using, both for work and leisure
purposes, the [ACE](http://www.cs.wustl.edu/%7Eschmidt/ACE.html) library. ACE
is a very powerful, useful and portable framework, oriented to networking, but
that can be used for abstracting nearly any system dependent task. In my case,
I'm using it for two client-server architecture projects, one of which is the
[MMORPG I'm working on](http://www.opengameonline.com/).

ACE has had, for me, a pretty nasty learning curve: at first there are some
good tutorial, and plenty of examples and test in the installation directory,
but after a while you are probably going to need to purchase the books, to
master it. I really can't blame the author(s) for that, as ACE is an
_impressive_ (I mean it) work, and deserves some revenue.

Using ACE for my projects has turn out into an incredibly useful outcome: I do
all my development on GNU/Linux machines (Debian Sarge at work, and Debian
Unstable at home), but the code I write needs to be ported to the Win32
platform as well. I'm no Windows programmer, and no Windows user, and there are
other people in my company who take care of integration with Win32 systems.
After writing my client/server project for about two months, it started to get
usable, and we decided to port it to Win32, and, to some extent, we were
expecting some trouble in porting to Win32 an application that went on for two
months and was made of roughly 10 thousands lines of code. The project is a
server process plus a dynamic library communicating with it, that a UI client
can use. Well, the porting to Win32 took no more than half an hour, and just a
few changes needed to be made. Of course, during the development, I've been
caring of not using any system dependent code, but the facts that it took so
little to port, was simply amazing.

The ACE library has provided for me lots of platform independent things: a way
to manage sockets and TCP connections, a way to manage loading of external
programs, a way to manage threads (and related mutexes or locks), a way to
manage logging, a way to manage tracing, and many more.

You can check [this
address](http://www.huihoo.org/ace_tao/ACE-5.2+TAO-1.2/ACE_wrappers/docs/tutorials/online-tutorials.html)
for some good ACE tutorials, especially regarding the client/server
communication. In my cases, I've gone for an approach orientated to a
system that would handle one client connection in a dedicated thread.
Thanks to ACE, this has been very easy and controllable. By _controllable_,
I mean that I'm quite sure that the code I've produced, to that regard, is
practically bug free. ACE helps you very well in taking care of all the
errors and reacting accordingly. Due to the vast number of platforms ACE
supports, it lacks exception handling, which can be considered a bad point,
although necessary. To some extent, though, ACE can support exception
handling, even if, for portability and integrity reasons, it's advisable to
let it go and rather use the classic return value checking approach.
Nothing will anyway impede you in creating your own exception handling
layer on top of your classes which manage ACE.

ACE is really strongly Object Oriented, which makes it perfectly suitable for
large (but well engineered) projects. Needless to say, that ACE is not advised
for very simple projects, unless you just want to take advantage of the system
abstraction it provides. For larger projects, instead, you'd better be very
careful and plan in advance. If you don't know the system very well, you
might end up making some wrong choices and wasting time. To this concern, I
advise to
[read](http://www.amazon.com/exec/obidos/tg/detail/-/0201699710/qid=1066085869/sr=1-1/ref=sr_1_1/104-9830255-9245533?v=glance&s=books)
[the](http://www.cs.wustl.edu/~schmidt/ACE/book1/)
[books](http://www.cs.wustl.edu/~schmidt/ACE/book2/).

ACE is also very useful when it comes to logging, as it provides some really
simple but powerful macros that can be used in debug mode, and that will
produce no code at all if disabled. You can check [this
website](http://www.awprofessional.com/articles/article.asp?p=169524&rl=1) for
an introduction to the ACE logging facilities.

I will end this short article with a list of pros and cons about ACE, as I've
found out during my experiences.


### Pros

 * _Very_ portable.
 * _Very_ powerful.
 * Good initial learning curve.
 * _Huge_ list of features.
 * Many examples.
 * Great mailing list support (even though they remind to reading the books
   too often).


### Cons

 * API are not very well documented.
 * You need to purchase the books to master it.
 * No free binary releases.


## What I advice it for

Any large project that need to manage networking and multithreading.

*[TCP]: Transfer Control Protocol
