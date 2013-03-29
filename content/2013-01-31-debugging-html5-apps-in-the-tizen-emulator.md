date: 2013-01-31 22:47:52
slug: debugging-html5-apps-in-the-tizen-emulator
title: Debugging HTML5 apps in the Tizen Emulator
category: Software
tags: Tizen

The Tizen SDK comes with an emulator based on [QEMU](http://www.qemu.org/). The
default configuration doesn't allow you to connect from the host machine to the
guest OS, other than using `sdb`.

While developing HTML5 frameworks and apps, I find the need to use the Chrome
debugger by attaching it to the remote session running within the emulator, and
to do that I need to establish a TCP connection from the host machine to the
guest OS.

QEMU comes with a way to forward ports, but to use it, we must activate the
`QEMU monitor`. Edit your
`~/tizen-sdk-data/emulator-vms/vms/YOUR_VM_NAME/vm_config.xml` file, and add
the following tag inside the `<usability>`tag:

```xml
<advancedOptions>-monitor unix:/tmp/qemu.sock,server,nowait</advancedOptions>
```

The following script will install your HTML5 widget, launch it, and connect a
remote Chrome debugging session to it:

```bash
#!/bin/sh
LOCAL_PORT=11223
SOCKET='unix:/tmp/qemu.sock'

echo "Building..."
# This script simply create a zip file with the content of the HTML5 app
./make-wgt.sh my_app.wgt >/dev/null

echo "Pushing the widget file..."
# This copies the file over to the emulator
sdb push my_app.wgt /home/developer

echo "Installing the widget file..."
# The following line does, in order:
#  - Remotely kill an instance of the app if it's running
#  - Uninstall it
#  - Install the new version that we previously copied
#  - Launch it
#  - Get the port number where we can attach our remote debugging session
# We are hardcoding the app's id here (123456790).
REMOTE_PORT=`sdb shell 'wrt-launcher -k 1234567890; sleep 2; wrt-installer -un 1234567890; wrt-installer -i /home/developer/my_app.wgt; wrt-launcher -d -s 1234567890' | awk '/port:/ { print $2 }'`

echo "Enabling forwarding to port $PORT..."
# This removes previous port forwarding rules. We are using 'socat' to
# connect to the UNIX socket that QEMU opened thanks to the XML changes in the
# Tizen VM config.
echo "hostfwd_remove ::$LOCAL_PORT" | socat $SOCKET -
# This creates the new forwarding rule.
echo "hostfwd_add ::$LOCAL_PORT-:$REMOTE_PORT" | socat $SOCKET -

echo "Starting debugging..."
# Now we can connect for some remote debugging.
google-chrome http://localhost:$LOCAL_PORT
```

Hope this helps.

*[OS]: Operating System
*[HTML5]: HyperText Markup Language
