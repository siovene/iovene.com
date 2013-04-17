date: 2007-02-19 15:44:55
slug: architecture-of-patching-semantic-versus-logical-content
title: Architecture of patching semantic versus logical content
category: Software
tags: versioning

Inspired by a certain patch that hit a
[darcs](http://www.iovene.com/darcs-the-source-code-management-system-of-the-future/)
repository to which I concur, I would like to talk about one thing that
developers don't seem to get very often, when using revision control systems:
**the structure of your files in the repository should have nothing to do with
the logical units that make your patches, or with the comment of your patches
themselves**.


Yesterday, I saw this patch hit the repository: "_Adding Cloth.h to the repo_".
The patch was adding an empty file, named `Cloth.h`. What's wrong with this? A
couple of things:


 1. The patch adds **no logical value unit** to the repository, but merely a
    **technical value**, i.e. an information about the content of the repository
    itself, which is, then, absolutely redundant, as you could retrieve that
    information in a separate (and more proper way), which of course depends on
    the revision control system you are using. Indeed it was just a technical
    information. Furthermore, the fact that the file was added, would have been
    there and obvious also **without** having to dedicate a single patch to it.

 2. The comment ("_Adding Cloth.h to the repo_"), once again, doesn't make any
    **logical sense** of its own, as adds an information that was already
    available using the revision control system tools.

What is a better way to do that? A patch named "_Preliminary support to
clothes_", which would add the file `Cloth.h` **with its content**, even if not
yet functional, makes perfect sense. It means that you're adding some **logical
value** to the repository, and the value that you're adding has nothing to do
with the way that value is represented (the file `Cloth.h`), or that it's being
actually added to a repository.

In other words, the **form** and **content** of patches should not only
represent single units of implicit logical value, [as discussed
earlier](http://www.iovene.com/5-svn-best-practices/), but should have no
_awareness_ whatsoever of being part of a revision control system, or being
uploaded to repositories, contains file, or even being patches at all!

Read more versioning tips [here](http://www.iovene.com/5-svn-best-practices/).
