date: 2008-02-14 10:59:46
slug: win32-odyssey-who-needs-documentation
title: Win32 odyssey: who needs documentation?
category: Software
tags: opinion
status: draft

During my coding adventures, I have just found myself having to port an
existing Win32 application to [CMake](http://www.cmake.org/). After writing a
mere 283 lines CMakeLists.txt file, and getting the application successfully
compile, I fired it up to see if it worked, of course. I found it failing when
doing a
[WSAAsyncSelect](http://msdn2.microsoft.com/en-us/library/ms741540(VS.85).aspx),
and failing there didn't seem to make any sense. So, to get to the point, I
decided I'd just carefully compare the compiler's options generated from CMake
with the ones that were in the original Visual Studio project file. After
finding the difference, I decided I was gonna learn what those flags meant, so
I googled for ["visual c++ compiler
flags"](http://www.google.com/search?q=visual+c%2B%2B+compiler+flags) and guess
what? **Nothing useful**. The right string to google would be ["visual c++
compiler
options"](http://www.google.com/search?q=visual+c%2B%2B+compiler+options). But
before getting to it, I had to unsuccessfully go thru ["visual studio compiler
options"](http://www.google.com/search?hl=en&safe=off&q=visual+studio+compiler+options).
You'd think that would cut it, right? Since ["visual c++ compiler
options"](http://www.google.com/search?q=visual+c%2B%2B+compiler+options) did
it. But, surpringly, ["visual studio compiler
flags"](http://www.google.com/search?hl=en&safe=off&q=visual+studio+compiler+flags)
did actually find what I wanted. Interesting combination.

I don't really feel like blaming Google on this. Reproducing the same search
pattern in the internal Help function of Microsoft Visual Studio gave me the
same success/no-success scheme. Besides, the whole point-and-click procedure is
a terribly uncomfortable experience.  Not only I have to get my hands off my
keyboard (inherently a waste of time), but also do I have to (mind: **have
to**) wander my mouse around for a while to get to the information.

So, I wondered, is there an alternative? I went to my
[rxvt](http://www.rxvt.org/) terminal emulator (which I run through
[Cygwin](http://cygwin.com/), can't really be bothered with using the native
Windows Terminal), and tried to get some help from `cl.exe`. No luck. After
some try-and-fail recursion, the least useless thing I would find was `cl.exe
-help` which would give me 106 (one hundred and six!) lines of documentation.
Wow, impressive, isn't it? Comparing, `gcc`'s manual page is 7820 lines, as for
the latest stable.
