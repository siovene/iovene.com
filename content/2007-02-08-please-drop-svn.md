date: 2007-02-08 14:05:09
slug: please-drop-svn
title: Please drop SVN
category: Software
tags: opinion, versioning

[SVN](http://subversion.tigris.org/) might be stable, it might be mature, it
might be successful, and it might be the winning source control system of the
moment. There's always a big risk of resulting unpopular, when criticizing
something that actually did find its way to success, but I have to say that
**SVN sounds terribly _antique_** sometimes.

I have already given [a brief introduction to the Darcs source control
system](http://www.iovene.com/darcs-the-source-code-management-system-of-the-future/),
and I would like here to talk about **a very strong point** it's got against
SVN.

Just yesterday, at work, I needed to commit certain modification to SVN. As I
examined the diff of my local copy with:

    svn diff

I realized that one of the file also contained some other modifications that I
didn't want to commit. After using [Darcs](http://www.darcs.net/) for several
months, I was suddenly hit by the shocking truth: **SVN doesn't allow
interactive and partial patches**, which Darcs names _hunks_.

What do you do in that case? Provided that there are people who actually [abuse
the _Save as..._ function of their
editor](http://svn.haxx.se/users/archive-2006-11/0197.shtml) by saving multiple
copies of the same file according to the logical patch they contain (which I
find absolutely horrible), the quickest way I could find was to:

 1. Making a diff: `svn diff > logical_patch_1.diff`
 2. Edit the diff _manually_, until I had two files, which represented the two
    logical diffs
 3. Revert the pristine: ` svn -R revert .`
 4. Apply the first diff: `patch -p0 < logical_patch_1.diff``
 5. Commit: `svn commit`
 6. Apply the second diff: `patch -p0 < logical_patch_2.diff``
 7. Commit: `svn commit`

With Darcs, all you have to do is issue the `darcs record` command (which
records your changes):

 1. Record: `darcs record -m "First logical patch (fixes bug 1234)"`
 2. Answer "yes" to the first hunk, and "no" to the second.
 3. Record again: `darcs record -m "Second logical patch (fixes bug 5555)"`
 4. Answer "yes" to the only hunk

Can you see the difference? It's not just about the number of operations
needed, but the **quality** of them, and the fact that Darcs is perfectly
oriented to this kind of flexibility. Please consider switching to Darcs for
your projects and work, as it's a mature and **better** system.
