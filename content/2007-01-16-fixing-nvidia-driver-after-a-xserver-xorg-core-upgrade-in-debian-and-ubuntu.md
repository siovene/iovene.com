date: 2007-01-16 15:02:50
slug: fixing-nvidia-driver-after-a-xserver-xorg-core-upgrade-in-debian-and-ubuntu
title: Fixing NVIDIA driver after a xserver-xorg-core upgrade in Debian and Ubuntu
category: Software
tags: howto, ubuntu, xorg, NVIDIA

Using Debian Testing or Unstable, or a frequently upgraded version of Ubuntu,
when doing an `apt-get update && apt-get upgrade` often will install a slightly
newer version of `xserver-xorg-code`, and this will break the NVIDIA
proprietary drivers, if you, like me, prefer to install them using the official
NVIDIA installer. When this happens, at your next reboot, or next time you
start X, this will crash.

Follow this instructions and you won't need to reinstall the NVIDIA driver from
scratch each time. First of all, stop your login manager (`gdm` assumed here):

    /etc/init.d/gdm stop

Then move to:

    cd /usr/lib/xorg/modules/extensions

Normally it should look like this:

    total 956K
    1 root root  19K 2007-01-09 21:13 libdbe.so
    1 root root  34K 2007-01-09 21:13 libdri.so
    1 root root 145K 2007-01-09 21:13 libextmod.so
    1 root root   18 2007-01-15 20:42 libglx.so->libglx.so.1.0.9742
    1 root root 676K 2007-01-15 20:42 libglx.so.1.0.9742
    1 root root  28K 2007-01-09 21:13 librecord.so
    1 root root  38K 2007-01-09 21:13 libxtrap.so

Notice the symbolic link from `libglx.so` to `libglx.so.1.0.9742`. In your
case, instead, the installation of a newer `xserver-xorg-core` overwrote the
`libglx.so` with the normal one provided by the X Server. What you have to do
is simply restore the previous situation. Remove the `libglx.so` file:

    sudo rm libglx.so

And make the symbolic link again:

    sudo ln -s libglx.so.1.0.9746 libglx.so

Of course the version number, in my case `1.0.9746` may be different in your
case. Now you can simply start the `gdm` login manager again:

    sudo /etc/init.d/gdm start

Everything should be working again.

_Thanks to
[http://osrevolution.wordpress.com/](http://osrevolution.wordpress.com/) for
this._
