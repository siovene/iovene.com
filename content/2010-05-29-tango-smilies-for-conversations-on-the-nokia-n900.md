date: 2010-05-29 14:36:42
slug: tango-smilies-for-conversations-on-the-nokia-n900
title: Tango smilies for Conversations on the Nokia N900
category: Software
tags: maemo, N900, project

One little known new feature of Maemo5 PR1.2 is the support for custom smilies
in Conversations (<bragging>which I implemented</bragging>).

I have made a smiley theme based on [Tango](http://tango.freedesktop.org/)
icons, but it's not yet in the repositories. Here's what it looks like:

[![][1]][1]

You can install it by downloading this file:
[conversations-tango-smilies_0.1_all.deb][2], and copying it over to your N900.

Then open an X-Terminal, [become root][3] and do:

```bash
cd /home/user/MyDocs; dpkg -i conversations-tango-smilies_0.1_all.deb
```

Once it's finished, switch to Conversation, go to Settings, and you will have a
new button, called _Smileys theme_. You can select your newly installed Tango
theme.

**Note:** the theme will not work with SMSs and Skype chats. All the other
accounts, _and SMSs_, will use the new theme.

After setting the new theme, go to an IM conversation and see if the new icons
are in the smiley picker. If not, a reboot should do.

Enjoy!

[1]: |filename|/images/2010_tango_smilies.png "Tango smilies"
[2]: http://www.iovene.com/wp-content/uploads/2010/05/tango-smilies.png
[3]: http://www.google.com/search?q=N900+become+root
