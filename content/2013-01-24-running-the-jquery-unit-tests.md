date: 2013-01-24 12:32:01
slug: running-the-jquery-unit-tests
title: Running the jQuery unit tests
category: Software
tags: jquery, nginx, tutorial, unit-testing

I'm about to start contributing the [jQuery](http://www.jquery.org/) project,
and one thing they left out in their
[documentation](https://github.com/jquery/jquery#running-the-unit-tests), is
how to get your testing environment up. You need to be able to serve
[PHP](http://php.net), because of the AJAX testing.

This post shows you how to configure [nginx](http://nginx.org/), PHP5, and
[FastCGI](http://fastcgi.com/) on a Debian based system. It's been tested only
on Ubuntu 12.10.

First, install the required software:

```bash
sudo apt-get install nginx php5-cgi
```

Then create the file `/etc/nginx/sites-available/jquerytest` with the following
content (but remember to change the `root` path):

```
server {
        root /path/to/jquery;
        index index.php index.html index.htm;

        # Make site accessible from http://jquerytest/
        server_name jquerytest;

        location / {
                try_files $uri $uri/ /index.php =404;
                # A little workaround to allow POSTing to static files
                error_page 405 = $uri;
        }

        fastcgi_index   index.php;

        location ~ \.php {
                # Workaround PHP vulnerability:
                # http://forum.nginx.org/read.php?2,88845,page=3
                try_files $uri =404;
                # Alternatively you can set
                # cgi.fix_pathinfo = false
                # in php.ini

                include /etc/nginx/fastcgi_params;
                keepalive_timeout 0;
                fastcgi_param   SCRIPT_FILENAME  $document_root$fastcgi_script_name;
                fastcgi_pass    127.0.0.1:9000;
        }
}
```

Link this file in `sites-enabled`:

```bash
sudo ln -s /etc/nginx/sites-available/jquerytest /etc/nginx/sites-enabled/
```

We have configured nginx so it can use FastCGI to serve files, so now we need
to run the FastCGI daemon. Create the file `/etc/init.d/php-fastcgi` with the
following content:

```bash
#!/bin/bash
BIND=127.0.0.1:9000
USER=www-data
PHP_FCGI_CHILDREN=15
PHP_FCGI_MAX_REQUESTS=1000

PHP_CGI=/usr/bin/php-cgi
PHP_CGI_NAME=`basename $PHP_CGI`
PHP_CGI_ARGS="- USER=$USER PATH=/usr/bin PHP_FCGI_CHILDREN=$PHP_FCGI_CHILDREN PHP_FCGI_MAX_REQUESTS=$PHP_FCGI_MAX_REQUESTS $PHP_CGI -b $BIND"
RETVAL=0

start() {
      echo -n "Starting PHP FastCGI: "
      start-stop-daemon --quiet --start --background --chuid "$USER" --exec /usr/bin/env -- $PHP_CGI_ARGS
      RETVAL=$?
      echo "$PHP_CGI_NAME."
}
stop() {
      echo -n "Stopping PHP FastCGI: "
      killall -q -w -u $USER $PHP_CGI
      RETVAL=$?
      echo "$PHP_CGI_NAME."
}

case "$1" in
    start)
      start
  ;;
    stop)
      stop
  ;;
    restart)
      stop
      start
  ;;
    *)
      echo "Usage: php-fastcgi {start|stop|restart}"
      exit 1
  ;;
esac
exit $RETVAL
```

Make the file executable and start the daemon:

```bash
sudo chmod +x /etc/init.d/php-fastcgi
sudo /etc/init.d/php-fastcgi start
```

Edit your `/etc/hosts` so that you'll be able to access your jQuery test page,
served by nginx:

```
127.0.0.1 localhost jquerytest
```

Finally, restart nginx:

```bash
sudo service nginx restart
```

You are now ready to run the unit tests by visiting:
[http://jquerytest/test/](http://jquerytest/test/)
