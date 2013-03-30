date: 2013-01-25 15:19:53
slug: jumpy-touchpad-on-lenovo-x230-and-ubuntu-12-10
title: Jumpy touchpad on Lenovo X230 and Ubuntu 12.10
category: Technology
tags: hardware, laptop, Lenovo X230, touchpad

I got a Lenovo X230 for work, and I wanted to quickly report on the only issue
I've had after a mint installation of Ubuntu 12.10. The touchpad was jumpy,
meaning that even the slightest touch would make it jerk 20 or 30 pixels, so it
was impossible to move exactly where you wanted to, with fine-grained
precision.

A quick search got me on [a bug reported on
Launchpad](https://bugs.launchpad.net/ubuntu/+source/xserver-xorg-input-synaptics/+bug/1042069),
and the solution was very simple.

Simply create a file called `/etc/X11/xorg.conf.d/50-touchpad.conf` (create the
`xorg.conf.d` directory if it doesn't exist), with the following content:

```
Section "InputClass"
        Identifier "touchpad"
        MatchProduct "SynPS/2 Synaptics TouchPad"
        Driver "synaptics"
        # fix touchpad resolution
        Option "VertResolution" "100"
        Option "HorizResolution" "65"
        # disable synaptics driver pointer acceleration
        Option "MinSpeed" "1"
        Option "MaxSpeed" "1"
        # tweak the X-server pointer acceleration
        Option "AccelerationProfile" "2"
        Option "AdaptiveDeceleration" "16"
        Option "ConstantDeceleration" "16"
        Option "VelocityScale" "32"
EndSection
```

You will then most likely have to configure the Acceleration and Sensitivity
using Ubuntu's Settings application.
