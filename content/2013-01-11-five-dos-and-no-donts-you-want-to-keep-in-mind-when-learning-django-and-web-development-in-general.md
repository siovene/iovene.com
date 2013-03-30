date: 2013-01-11 00:05:17
slug: five-dos-and-no-donts-you-want-to-keep-in-mind-when-learning-django-and-web-development-in-general
title: Five dos (and no don'ts) you want to keep in mind when learning Django and web development in general
category: Software
tags: Django, web

Two years ago I had an idea for a site, and I embarked myself in what turned
out to be a task of behemothic size. Twelve months later, I released to the
public the initial incarnation of [AstroBin](http://www.astrobin.com/), a
website dedicated to the hosting of astrophotographs.

Alas, it was my first complex and feature rich website, and I learned several
frameworks and libraries on the go, such as
[Django](http://www.djangoproject.com/) and [jQuery](http://www.jquery.com/).
Here are some pieces of advice for somebody starting out on a similar path.


#### 1. Do split your project into multiple apps


Django projects can be split in multiple apps, to reduce complexity and allow
the application of the One Responsibility principle. Neglect to do that and you
will end up with a 6,000 line long `views.py`, and a shaggy mess of spaghetti
code.


#### 2. Do make your project easy to setup and deploy


A project that can be deployed quickly will make your life easier if you have
to migrate to a new server, if you have to quickly create a sandboxed server
for testing purposes, if you want to get people to collaborate with you.

To do that, try to stay away from things that live outside Django's sphere of
influence, like bash scripts, cron jobs, or other third party code that has
nothing to do with your Django app.

I recommend that you start your app on [Heroku](http://www.heroku.com/),
because if you get it working there, it'll work everywhere.


#### 3. Do write a comprehensive set of unit tests


Do it if your app is small, do it if your app is large. But especially if it's
large. Do it for your Django code, and do it for your JavaScript code. The time
spent doing it will be totally worth it when you have to deploy new features to
thousands of users and you can have a piece of mind knowing that there are no
regressions.


#### 4. Never, ever assume that your users will use your website the way you
intended it


They will break it, they will abuse it, they will find holes, they will do
everything that can be done to fill your database with inconsistent data. Spend
a considerable effort to keep things as tight as possible, so that no
unexpected input can reach your code.


#### 5. Do keep your third party dependencies at a minimum


Dependencies must be tracked and upgraded, and often things will break in the
most mysterious of ways (see point #3 if you want to prevent that.) It's really
imperative that you keep your ecosystem as small as possible.
