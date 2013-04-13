date: 2007-03-06 21:03:15
slug: the-ultimate-guide-for-utf-8-in-irssi-and-gnuscreen
title: The ultimate guide for UTF-8 in irssi and GNU/Screen
category: Software
tags: howto, irssi, screen

I've been having quite a lot of trouble, lately, configuring
[irssi](http://www.irssi.org) to work well with UTF-8. Irssi's documentation
was quite incomplete, on the matter, or discouraging, and there wasn't much on
the Internet, so, after figuring out what the way is, I'll share it here.

First of all, **you've got to make sure that your system is configured for
UTF-8 locales**:

    bash-3.1$ locale LANG=en_GB.utf8 LANGUAGE=en_GB.utf8 LC_CTYPE="en_GB.utf8"
    LC_NUMERIC="en_GB.utf8" LC_TIME="en_GB.utf8" LC_COLLATE="en_GB.utf8"
    LC_MONETARY="en_GB.utf8" LC_MESSAGES="en_GB.utf8" LC_PAPER="en_GB.utf8"
    LC_NAME="en_GB.utf8" LC_ADDRESS="en_GB.utf8" LC_TELEPHONE="en_GB.utf8"
    LC_MEASUREMENT="en_GB.utf8" LC_IDENTIFICATION="en_GB.utf8"
    LC_ALL=en_GB.utf8

If the output of the `locale` doesn't look like that, you want to reconfigure
your locales. On Debian, wha you have do is:

    sudo dpkg-reconfigure locales

Here's some screenies of what to expect:

[![][1]][1]
[![][2]][2]
[![][3]][3]

    Generating locales (this might take a while)...  en_GB.ISO-8859-1... done
    en_GB.ISO-8859-15... done en_GB.UTF-8... done en_US.ISO-8859-1... done
    en_US.ISO-8859-15... done en_US.UTF-8... done Generation complete.

Perfect, now that our system is configured for UTF-8, we want to configure our
terminal emulator. If you're using **xterm**, you can invoke it with the `-u8`
switch, or just do `uxterm`, and that's all that's needed. If you're using the
**gnome-terminal**, go to  the _Terminal_ menu, then choose _Set Character
Encoding_ and then _UTF-8_. If UTF-8 doesn't appear in the list, you may
want to try to logout and login again. While you're at it, in the **GDM**
login manager, go to the _Language_ option and choose UTF-8 there too, so
that it will be default.

Now let's take care of **GNU/Screen**. In order to enable UTF-8, all you have
to do is launch it with the `-U` switch:

    screen -U -S irc

_irc_ is just the name I want to assign to that `screen` session. Notice that
if you want to switch a living `screen` session to UTF-8, you could do it for
    each window, using the command _CTRL-a : utf8 on_.

Once your GNU/Screen is configured for UTF-8, you have to finally set up your
**irssi** client. This was, for me, the tricky part, since the documentation is
a bit unclear, and I didn't realize that my irssi wasn't built with **recode
support**. To make sure that your irssi is, fire it up and give the command

    /recode

If you get something like

    Target                         Character set

then everything is alright, otherwise, if you get a **No such command** error,
you will have to reinstall irssi with **recode support**.

Irssi UTF-8 support is made so that you are able to recode to different
charsets, depending on the server or channel you're chatting in. First let's
set up some general options:

    /set term_charset UTF-8 /set recode_autodetect_utf8 ON /set recode_fallback
    UTF-8 /set recode ON /set recode_out_default_charset UTF-8 /set
    recode_transliterate ON

These options will be the default, unless overridden for specific servers or
channels. What do they mean?

  * **term_charset**: this is the character set of your terminal emulator

  * **recode_autodetect_utf8**: irssi will recognize UTF-8 input automatically
    and treat it consequentially

  * **recode_fallback**: when we get some non-UTF-8 text from a chat peer, the
    text should be converted to this character set

  * **recode**: this enables the whole recode thing

  * **recode_out_default_charset**: this is very important: this is the default
    charset that you send out, unless differently specified by a server/channel
    rule (we will see that shortly)

  * **recode_transliterate**: this enables transliteration of the closest
    match: i.e. if someone sends you a character that's not in your charset, it
    will be transliterate to the closest possible one, or with a question mark,
    if none found

Now, you probably need different recodes on different channels, because you may
speak different languages on different channels. For example, I send out UTF-8
when typing on English speaking channels, and ISO-8859-1 or ISO-8859-15 when
typing on Finnish or Italian speaking channels, so people on the other end will
always get my characters right.

You need to add rules with the `/recode` command:

    /recode add ircnet/foo ISO-8859-15 /recode add ircnet/bar ISO-8859-1
    /recode add freenode/gee ISO-8859-1

Those command will make you "speak" ISO-8859-15 on #foo on IRCNet, and
ISO-8859-1 on #bar and #gee in freenode. Everywhere else you will "speak"
UTF-8.

And this is what we get: here I'm typing (er... I'm copy-pasting from
Wikipedia) some text:

[![][4]][4]

If you connect via SSH to a remote machine, where you run irssi inside screen,
all you have to do is to set both systems to use UTF-8, as explained in the
beginning of this article, and then set the terminal of the machine _from
which_ you SSH, to use UTF-8, as explained earlier.

[1]: |filename|/images/2007_irssi_utf8_1.png
[2]: |filename|/images/2007_irssi_utf8_2.png
[3]: |filename|/images/2007_irssi_utf8_3.png
[4]: |filename|/images/2007_irssi_utf8_4.png
