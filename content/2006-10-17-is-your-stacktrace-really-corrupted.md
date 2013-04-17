date: 2006-10-17 12:37:26
slug: is-your-stacktrace-really-corrupted
title: Is your stacktrace really corrupted?
category: Software
tags: coding, howto

You may encounter, during your debugging sessions, the `stack corruption'
problem. Usually you will find it out after seeing your program run into a
segmentation fault. Otherwise, it must mean that some very malicious and subtle
code has been injected into your program, usually through a buffer overrun.
What is a buffer overrun? Let's examine the following short C code:

    #include <stdio.h>

    void bar(char* str) {
        char buf[4];
        strcpy( buf, str );
    }

    void foo() {
        printf("Hello from foo!");
    }

    int main(void) {
        bar("This string definitely is too long, sorry!");
        foo();
        return 0;
    }

There's clearly something wrong with it: as you can see, we are copying `str'
to `buf' without first checking the size of `str'. First of all there is a
security issue, because if `str' didn't just come from a fixed string like in
this case, but got inputted from somewhere (maybe on a website), then there
could be a string long enough to overwrite the code of `foo', and run malicious
code on its behalf. What we have here, anyhow, is just a segmentation fault.
Let's debug the program.

    (gdb) file stack
    Reading symbols from /home/siovene/stack...done.
    (gdb) run
    Starting program: /home/siovene/stack

    Program received signal SIGSEGV, Segmentation fault.
    0x6f6c206f in ?? ()
    (gdb) backtrace
    #0  0x6f6c206f in ?? ()
    #1  0x202c676e in ?? ()
    #2  0x72726f73 in ?? ()
    #3  0xbf002179 in ?? ()
    #4  0xb7df9970 in __libc_start_main ()
          from /lib/tls/i686/cmov/libc.so.6
    Previous frame inner to this frame (corrupt stack?)

Obviously something must have gone wrong. In order to better understand what is
going on, let's make a step back, and let's examine a working example instead:

    #include <stdio.h>

    void bar(char* str) {
        char buf[4];
        strcpy( buf, str );
    }

    void foo() {
        printf("Hello from foo!");
    }

    int main(void) {
        bar("abc");
        foo();
        return 0;
    }

This is the same code, but it's been stripped off of the long string that
caused the segmentation fault, and in its place we find a harmless 3 character
string: `abc'. Let's name the program stack.c anc compile it with debug
informaion:

    $> gcc -g -o stack stack.c

Now let's debug it:

    (gdb) file stack
    Reading symbols from /home/siovene/stack...done.
    (gdb) break bar
    Breakpoint 1 at 0x80483ca: file stack.c, line 5.
    (gdb) run
    Starting program: /home/siovene/stack

    Breakpoint 1, bar (str=0x8048545 "abc") at stack.c:5
    5         strcpy( buf, str );

We have entered the bar() function, let's examine the backtrace:

    (gdb) backtrace
    #0  bar (str=0x8048545 "abc") at stack.c:5
    #1  0x0804840e in main () at stack.c:13
    </code>

What is the address of the bar() function?

    (gdb) print bar
    $1 = {void (char *)} 0x80483c4

Let's now be paranoid and check this out producing a dump of our executable:

    $> objdump -tD stack > stack.dis

Open the file with your favorite editor and look for `80483c4′, the address of
bar():

    080483c4 <bar>:
     80483c4: 55                    push   %ebp
     80483c5: 89 e5                 mov    %esp,%ebp
     80483c7: 83 ec 28              sub    $0x28,%esp
     80483ca: 8b 45 08              mov    0x8(%ebp),%eax
     80483cd: 89 44 24 04           mov    %eax,0x4(%esp)
     80483d1: 8d 45 e8              lea    0xffffffe8(%ebp),%eax
     80483d4: 89 04 24              mov    %eax,(%esp)
     80483d7: e8 0c ff ff ff        call   80482e8
     80483dc: c9                    leave
     80483dd: c3                    ret


Perfect, that's our function. But now let's get curious. Where's the stack
pointer in the CPU registers?

    (gdb) info registers
    eax            0x0      0
    ecx            0xb7ed11b4       -1209200204
    edx            0xbff04f60       -1074770080
    ebx            0xb7ecfe9c       -1209205092
    esp            0xbff04f10       0xbff04f10
    ebp            0xbff04f38       0xbff04f38
    esi            0xbff04fd4       -1074769964
    edi            0xbff04fdc       -1074769956
    eip            0x80483ca        0x80483ca
    eflags         0x282    642
    cs             0x73     115
    ss             0x7b     123
    ds             0x7b     123
    es             0x7b     123
    fs             0x0      0
    gs             0x33     51

The `esp` register, on the architecture this article is written on, is the
stack pointer. Its address is 0xbff04f10. Let's examine the memory at that
point:

    (gdb) x/20xw 0xbff04f10
    0xbff04f10:  0x00000000   0x08049638   0xbff04f28   0x080482b5
    0xbff04f20:  0xb7ecfe90   0xbff04f34   0xbff04f48   0x0804843b
    0xbff04f30:  0xbff04fdc   0xb7ecfe9c   0xbff04f48   0x0804840e
    0xbff04f40:  0x08048545   0x08048480   0xbff04fa8   0xb7db3970
    0xbff04f50:  0x00000001   0xbff04fd4   0xbff04fdc   0x00000000

With this command we have told GDB to examine 20 words in exadecimal format at
the address 0xbff04f10. That's because the value of the stack pointer is the
address of the back-chain pointer to the previous stack frame. So address
0×00000000 is the address of the previous stack frame. But 0×00000000 is put in
the stack frame in concurrence of the program entry point, i.e. the main()
function. This agrees with the fact that we know bar() was called by main()!

Everything looks ok and in place, since the program works perfectly we weren't
expecting anything different. Let's now do the same with the faulty program. At
the moment of the segmentation fault, the backtrace looked like this:

    (gdb) backtrace
    #0  0x6f6c206f in ?? ()
    #1  0x202c676e in ?? ()
    #2  0x72726f73 in ?? ()
    #3  0xbf002179 in ?? ()
    #4  0xb7df9970 in __libc_start_main ()
          from /lib/tls/i686/cmov/libc.so.6
    Previous frame inner to this frame (corrupt stack?)

To see exactly what goes on, it would be better to debug it more carefully:

    (gdb) file stack
    Reading symbols from /home/siovene/stack...done.
    (gdb) break bar
    Breakpoint 1 at 0x80483ca: file stack.c, line 5.
    (gdb) run
    Starting program: /home/siovene/stack

    Breakpoint 1, bar (str=0x8048580
                        "This string definitely is too long, sorry!")
                      at stack.c:5
    5         strcpy( buf, str );
    (gdb) next
    6       }
    (gdb) next
    0x6f6c206f in ?? ()
    (gdb) next
    Cannot find bounds of current function

Let's then try to follow back the stacktrace, as we did previously:

    (gdb) backtrace
    #0  0x6f6c206f in ?? ()
    #1  0x202c676e in ?? ()
    #2  0x72726f73 in ?? ()
    #3  0xbf002179 in ?? ()
    #4  0xb7e9b970 in __libc_start_main ()
          from /lib/tls/i686/cmov/libc.so.6
    Previous frame inner to this frame (corrupt stack?)

    (gdb) info registers
    eax            0xbfeed1e0       -1074867744
    ecx            0xb7ea4c5f       -1209381793
    edx            0x80485ab        134514091
    ebx            0xb7fb7e9c       -1208254820
    esp            0xbfeed200       0xbfeed200
    ebp            0x6f742073       0x6f742073
    esi            0xbfeed294       -1074867564
    edi            0xbfeed29c       -1074867556
    eip            0x6f6c206f       0x6f6c206f
    eflags         0x246    582
    cs             0x73     115
    ss             0x7b     123
    ds             0x7b     123
    es             0x7b     123
    fs             0x0      0
    gs             0x33     51

    (gdb) x/20xw 0xbfeed200
    0xbfeed200:  0x202c676e   0x72726f73   0xbf002179   0xb7e9b970
    0xbfeed210:  0x00000001   0xbfeed294   0xbfeed29c   0x00000000
    0xbfeed220:  0xb7fb7e9c   0xb7fee540   0x08048480   0xbfeed268
    0xbfeed230:  0xbfeed210   0xb7e9b932   0x00000000   0x00000000
    0xbfeed240:  0x00000000   0xb7feeca0   0x00000001   0x08048300

    (gdb) x/20xw 0x202c676e
    0x202c676e:     Cannot access memory at address 0x202c676e

There's only one explanation to that: the stack memory has been overwritten and
now contains gibberish. We have been very unlucky with our example, but this
gave us the tools to imagine another case. Let's assume the stack got actually
corrupted not because it was overwritten accidentally, but because GDB was
failing to build it. In this case you are still able to navigate it backwards.
All you need to do it keep following the value of the stack frames, starting
from the `esp` register, until you reach 0×000000. Write all the addresses
down, and then use `objdump' to obtain the disassembly and symbols information
from the binary. All is left, now, is to check the names of the symbols
matching the pinned up addresses.

If you can actually do that, than you have successfully reconstructed your
stacktrace. It wasn't really corrupted by a bug in your program, but simply GDB
missed to keep it up with it.
