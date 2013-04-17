date: 2006-12-19 16:20:09
slug: common-mistakes-when-approaching-oo-design
title: Common mistakes when approaching OO design
category: Software
tags: coding, design

Today I want to talk about Object Oriented practices, and 3 commonly made
mistakes. Very often, when reviewing code written by other people, I find
violations of common OO practices, that make the code a lot less maintainable.
Here follows a list of the most common ones, and, of course, some explanations
about them.

### Layer violation

While not the most common, this appears to me as the most dangerous. What is
layer violation? Let's show it with an example. Assume we have a GUI driven
application that reads data from a database and shows the results on the
display. We might consider having some upper level Controller class, and
managers for each component, e.g. `GuiManager`, `DbManager`, `ReportManager`.
Assume that the `Controller` class runs a loop, and in that loop we take care
of refreshing the GUI. What I'm going to write now is really wrong:

    this->guiManager().reportTable().update(this->reportManager().populate(
        this->dbManager().query(someSqlString)));

Well, there are many horrible thing here, but the _layer violation_ happens in
this->guiManager().reportTable().update(...). Imagine the various components of
this scheme as layers on top of each other. We have the `Controller`, the
`GuiManager` and a certain `ReportTable`.

What we're doing, is accessing the `ReportTable` layer from the `Controller`
one. Why is this bad? Having layer violations will fill your code up with
disturbance. You will rapidly lose track of what does what (e.g., who is
updating the `ReportTable`? The `Controller` or the `GuiManager`?), and this
will end up into an intertwined mess commonly known as Spaghetti Code.
Doing that, you are performing actions from parts of the code to which those
actions do not belong. Classes shouldn't care about what other classes _are_,
but only about what other classes _do_. Think about it: do you really want to
let the `Controller` know that the `GuiManager` has a `ReportTable`, inside?
Shouldn't the `Controller` tell the `GuiManager` just _what to do_, rather than
_how to do it_? Having classes access inner functioning of other classes will
lead you to messy code, especially when there's more than one people working on
a project, as discussed later in this article. Having all the communication
happening between adjacent layers will help us keeping the project consistent
even in case of changes to components. Imagine if one day I will decide that
the `GuiManager` doesn't need a `ReportTable`, but a `ReportChart`. My ideal
scenario is the one where all the changes I need to make are only within the
`GuiManager`. But if there was a layer violation, such as the mentioned one, I
would have to modify the `Controller` as well. When people in a group work on
different components of a system, they don't want to make a change that will
break everything else. In order to avoid broken code, it would be a good
practice to keep layers commnicate with the adjacent ones, according to well
known interfaces.


### Information hiding

This brings us to our next point. What does the `Controller` need to know about
the members of the `GuiManager`? Ideally, nothing. Ideally, there would be no
getters or setters, since the `Controller` doesn't need to know anything about
the `GuiManager`'s inner functioning. What needs to be done, in fact, is
designing a well known interface for the `GuiManager` that the `Controller` can
use. Once designed, such interface should never be changed, in order to ensure
maximum compatibility within the components. Imagine you have just a certain
`GuiManager::update() `method, the `Controller` would just need to call
`this->guiManager().update()` and, whatever the `GuiManager` does, is none of
the `Controller`'s business. Inside, the `GuiManager` might do something like
`this->reportTable().update()`, but in case this would change to a
`ReportChart`, it wouldn't break the `Controller`, and keep the people that
work with it happy.


### Abusing singleton pattern

`Singleton`s are not a way to get yourself some global variables. Think
thoroughly about the reasons why you really need a `Singleton` in your program.
Is it just a way to access some variables from everywhere in the code? If the
answer is yes, you should consider refactoring your code to get rid of the
`Singleton` class. Keep also in mind that `Singleton`s are enemies of unit
testing. Have a `Singleton` class _do_ something, rather than _contain
_something. A typical example of a class suitable to be a `Singleton` is a
`Logger` class. You need to access it from everywhere in the code; the class
doesn't need to be aware of the application it's in; the class _does_ (logs)
and doesn't just _contain_. If you write a `Singleton` class like the
following, you're doing something wrong:

    class AccessData : public Singleton<AccessData> {
        friend class Singleton<AccessData>;
        public:
            std::string username;
            std::string password;
    };

This class seems to have the sole purpose of easing the access to a certain
`username` and `password` from everywhere in the code, without the need of
passing them around. You should consider passing references and data around
only when needed, or adopting some signaling framework.
