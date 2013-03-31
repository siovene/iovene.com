date: 2010-11-21 22:32:18
slug: my-remote-controlled-astrophotography-setup
title: My remote controlled astrophotography setup
category: Astronomy

Ever since I have gifted my patio with a [beautiful zinc coated steel
pier](/314), thus gaining the ability to have a permanently polar aligned
mount, it's got easier to remotely control my whole setup with minimal effort.
Of course, by _minimal_, I still mean considerable. You will understand if you
are an astrophotographer too.

The pier is located only a few meters from the windows in my living room, and
that means that I can use 5 meter long USB extensions to reach my laptop which
is comfortably sitting, as it should, in my lap. Does that spell r-e-m-o-t-e to
you? It certainly does not to me.

I would be constrained to stay on the couch, and there would be three cables
running to my laptop: one COM cable that's used to connect to the SynScan
controller of my HEQ5, one USB cable that comes from the Canon EOS 450D camera,
and one USB cable that comes from the QHY5 guide camera. Luckly, the laptop I'm
using has a dock that has a COM port, or else I would have to use a COM-to-USB
adapter, bringing the number of needed USB ports to three. And aren't we
forgetting the external hard drive? Four. And how about the mouse? Five.  I
have only two USB ports on this old T43 laptop, and the one USB powered hub I
have tried ended up causing a lot of problems, with annexed nerve wreckage.

Yeah, that was certainly not remote.

Right next to the pier, there's a certain tools/storage room, whose secret
agenda is to come between my lenses and some astronomical object many light
years away. When it's not too busy doing that, it serves as a place for a lot
of junk. In this room I also have an old computer which turned out to be
perfect as a dedicated astrophotography box. It's got two Intel Core 2 Duo
processors, and 2GB RAM. Plenty for my purposes.

The problem? The room does not have wired connectivity (I find that odd, as it
certainly has power and the rest of my house if littered with CAT5 sockets) and
the wireless signal coming from the router inside is too weak to reach the
utterly underpowered antenna sticking out from the back of the computer, alone
in a corner, covered by a ton of dusty cables.  Luckily I had a Linksys WAP56G
wireless access point sitting around, and that would've made an excellent
wireless repeater! Except that the stock software would only let it work, as a
repeater, with some other Linksys router (namely, the WRT56G, i.e. something in
the same family).

And that's where Open Source comes to the rescue, thanks to what I have learned
to appreciate as the immense power and usefulness of
[DD-WRT](http://www.dd-wrt.com/). I even [tweeted my love for
it.](http://twitter.com/#!/siovene/status/6278578031296512) DD-WRT is a
replacement firmware compatible with lots of routers and access points, and it
will definitely enrich the capabilities of your device. Give it a try. It has
been quite easy to set it up as a wireless repeater for my main wireless
network, and my mind was (figuratively, you just need to specify, these days)
blown away when I learned that it could simply configure the LAN port on the AP
as a switch port. That means that I can have the astrophotography box wired to
the AP, the AP linked to my main wireless network, and my laptop anywhere in
the house, linked to the same network, remote controlling the astrophotography
box!

To achieve the actual remote controlling, I have resorted to the even so
popular VNC. Some networking magic and a little port forwarding later, I can
now literally see the content of the screen of the remote computer right in the
screen of my laptop; wirelessly and efficiently.

So my astrophotography routine can now be broken up in the following steps:

 1. Look at the sky.
 2. It's cloudy.
 3. GOTO 1.

Just kidding. Here it is:

 1. Remove the Telegizmos Series 365 cover from my pier, uncovering the HEQ5
    mount.
 2. Mount the optics on top of it.
 3. Turn on the computer in the tools room. Note that the cables to the
    cameras and mount, whose ends belong to the computer, are already connected.
 4. Connects the cables to the appropriate ends in the cameras and mount.
    Connect the power of course.
 5. Go inside and connect to the astrophotography box from the laptop, via
    VNC.

Considering that the mount is already polar aligned, and that, thanks to the
brilliancy of EQMOD, as long as I remember to _park the scope_ after each
session, I won't need to repeat any 3-star alignment or anything, everything
should be ready to start imaging.

I probably need to focus at this point, so I can just go outside with the
laptop in hand, have a look at Live View from Canon EOS Utility, and adjust the
knobs accordingly.

I can now simply go inside, program the shooting, and I can continue using my
laptop without worrying that I might do something that interferes with the
imaging.

Neat, isn't it?
