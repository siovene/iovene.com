date: 2006-12-29 14:45:21
slug: darcs-the-source-code-management-system-of-the-future
title: Darcs - The source code management system of the future?
category: Software
tags: versioning, darcs

Having already mentioned [some good practices for source code
versioning](http://www.iovene.com/content/view/88/34/) and [how important
versioning is](http://www.iovene.com/content/view/92/34/), in any case, I would
like now to review and comment about what I find the best source code
management system out there: [darcs](http://www.darcs.net/).

Darcs is a source control system written in
[Haskell](http://www.haskell.org/haskellwiki/Haskell) (a functional language),
and feature very solid mathematics bases, being completely engeneered on top of
a "patch theory". Not only darcs is straightforward and very easy to you, not
only it's very interactive and minimizes the chances of mistakes, but it also
gives out features that the popular SVN doesn't have. Here I'm going to show
some use cases, and show how things are easier with darcs.


### A quick intro

Before analyzing the key features, let's have a brief start-up quick tutorial.
The easiest way to get darcs, is to download a [binary
package](http://darcs.net/DarcsWiki/CategoryBinaries). These packages contain a
precompiled release of darcs, with everything needed statically linked inside.
You only need o copy that somewhere in your $PATH, such as /usr/bin,
/usr/local/bin, or whatever you have in your $PATH. Of course you can download
the source code and build it yourself if you want.

Let's now create a simple `Hello World` project, and use darcs to version it.

    $ mkdir $HOME/projects/HelloWorld $ cd !$ $ darcs init

`darcs init` will create all the files necessary to source-control the code.
You will find a new directory named `_darcs`.

Now we can write our `HelloWorld.cc` main file:

    #include <iostream>
    using namespace std;
    int main(void) {
        cout << "Hello World!"<< endl;
    }

Time to add the file to version control.

    $ darcs add HelloWorld.cc

Alright, now we really get into darcs. First of all, in case you didn't notice,
darcs doesn't really need any server at the other end, like SVN would need an
SVN server, or CVS would need a CVS server. This means no hassle in installing
and configuring a server. Later we will see how darcs manages collaboration
with remote users.

Now it's time to _save_ our changes to the repository.

    $ darcs record

    Darcs needs to know what name (conventionally an email address) to use as
    the patch author, e.g. 'Fred Bloggs <fred@bloggs.invalid>'.  If you provide
    one now it will be stored in the file '_darcs/prefs/author' and used as a
    default in the future.  To change your preferred author address, simply
    delete or edit this file.

    What is your email address?  Salvatore Iovene <salvatore@invalid.com>

    addfile ./HelloWorld.cc Shall I record this change?(1/?)[ynWsfqadjkc], or ? for help: y

    hunk ./HelloWorld.cc 1
    +#include <iostream>
    +
    +using namespace std;
    +
    +int main(void) {
    +	cout << "Hello World!" << endl;
    +	return 0;
    +}
    +
    Shall I record this change?(2/?)[ynWsfqadjkc], or ? for help: y
    What is the patch name? First record.
    Do you want to add a long comment? [yn] n
    Finished recording patch 'First record.'

Some points worth inspection here:

 * **Why did darcs what to know my email address?** That's because everything
   you commit (they are named patches) will be known as coming from you. If
   you're working with several people, darcs has to know who is committing
   what. Furthermore, people downloading your repository can, e.g. make some
   changes and improvements, and then issue a `darcs send` which will send you
   the patch via email, and you can evaluate it and decide if apply it.

 * **What is a hunk?** A `hunk`is a piece of a patch, i.e. a certain
   modification in some source file. If you have a large file, `foo.c`, and
   modify a certain function `bar()` at the beginning of the file, and then a
   certain other function `tar()` at the end of the file, this will result in
   two hunks. What's the advantage of all this? Since darcs is so interactive,
   you may decide to either apply both hunks in the same pathc, so answer 'y'
   to both, or realize that they logically belong to two different patches, so
   you will say 'y' to one of them, and 'n' to the other. Then, after
   finishing recording the first patch, you issue a `darcs record` again, and
   record the other hunk in a separate patch, with a separate name, that forms
   a logical unit _per se_.

Now let's make a small change.


    #include <iostream>

    int main(void) {
    	std::cout << "Hello World!" << std::endl;
    	return 0;
    }


As you can see, we have removed the `using namespace std;` declaration, and
added the `std::` namespace prefix to `cout` and `endl`. A very important darcs
command is `whatsnew`, that shows us how the code differs from the repository.

There are two hunks, as expected. Let's record the changes.

    $ darcs record
    hunk ./HelloWorld.cc 3
    -using namespace std;
    -
    Shall I record this change?(1/?)[ynWsfqadjkc], or ? for help: y

    hunk
    ./HelloWorld.cc 4
    -	cout << "Hello World!" << endl;
    +	std::cout << "Hello World!" << std::endl;
    Shall I record this change?(2/?)[ynWsfqadjkc], or ? for help: y
    What is the patch name? Removing the std namespace declaration.
    Do you want to add a long comment? [yn]n
    Finished recording patch 'Removing the std namespace declaration.'

Obviously those two hunks must form one single patch, because we don't want any
patch to leave the repository in a broken state. Now we get to the cool stuff.
Darcs lets you unrecord your changes, i.e. interactively rollout the patches
until you are satisfied. We might change our mind about the last patch, and
think that `using namespace std;` is not tha bad after all. No problem.

    $ darcs unrecord

    Fri Dec 29 12:53:32 EET 2006 Salvatore Iovene <salvatore@invalid.com>
    * Removing the std namespace declaration.
    Shall I unrecord this patch?(1/2)[ynWvpxqadjk], or ? for help: y

    Fri Dec 29 12:37:33 EET 2006 Salvatore Iovene <salvatore@invalid.com>
    * First record.
    Shall I unrecord this patch?(2/2)[ynWvpxqadjk], or ? for help: n

    Finished unrecording

Now there we are again, back as if nothing happened.

Imagine you want to have a copy of your repository, maybe on a different
partition of your disk, or maybe on a USB storage drive:


    $ cd ..
    $ mkdir RepoCopy
    $ cd RepoCopy/
    $ darcs init
    $ darcs pull ../HelloWorld/

    Fri Dec 29 12:37:33 EET 2006 Salvatore Iovene <salvatore@invalid.com>
    * First record.
    Shall I pull this patch?(1/1)[ynWvpxqadjk], or ? for help: y
    Finished pulling and applying.

Another directory is not the only way you can move your repository around, you
can use SSH to copy it to another machine, and HTTP to fetch it. This is
actually the way you handle collaboration. Imagine you have a server somewhere,
named `www.server.com`, and there you want to have your central repository,
with which you can collaborate with your development peers.

    $ darcs push \ username@www.server.com:/var/www/htdocs/HelloWorld/repo

This will ask you which patches you want to `push` to that server, one by one,
in the usual darcs interactive mode. I'm assuming that the directory
`/var/www/htdocs/HelloWorld/` on the server, hosts the
`http://www.server.com/HelloWorld/` website. Everybody can now get a copy of
your project just by doing this:

    $ darcs get http://www.server.com/HelloWorld/repo

And anybody with an account on that server, will be able to push patches, if
they of course have write permission to the directory where the repository is.


### Where to go from here

Here follow some must-read links if you're interested in darcs. Probably in the
future I will write more about it. Thanks for reading.

 * [Download darcs](http://darcs.net/DarcsWiki/CategoryBinaries)
 * [Official Getting-Started guide](http://darcs.net/DarcsWiki/GettingStarted)
 * [Manage a secure repository on the
   Internet](http://darcs.net/DarcsWiki/RepoViaSSH)
 * [Best practice with one main
   developer](http://www.darcs.net/manual/node6.html#SECTION00640000000000000000)
 * [Moving patches
   around](http://www.darcs.net/manual/node4.html#SECTION00450000000000000000)
 * [Theory of patches](http://www.darcs.net/manual/node8.html)

