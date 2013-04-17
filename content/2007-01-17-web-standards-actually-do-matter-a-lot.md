date: 2007-01-17 16:40:04
slug: web-standards-actually-do-matter-a-lot
title: (Web) Standards actually do matter a lot
category: Software
tags: design, web

A week ago I stumbled upon [this
article](http://www.modernlifeisrubbish.co.uk/article/web-standards-dont-matter-as-much-as-you-think)
from [Stuart Brown](http://stua.rtbrown.org/), which actually even got a fair
amount of [Diggs](http://www.digg.com/). As soon as I read it, I felt obliged
to reply extensively to it, as I think it mostly represent everything which is
wrong in the current web design trends (or should I say _all time_ web design
trends?).

Something that really annoyed me about the article, was the lack of serious
points and the abundance of useless words like "some standards evangelist",
"Obsessing over semantically correct markup", "a few standards zealots",
"zealotry accomplishes nothing but a collection of smug faces and a collection
of 'XHTML 1.1 Compliant' bylines". Those were only fruitless diversions and not
real arguments.

The authors gets one thing right, though, and it's that

> your users don't care about XHTML, they care about how your site appears.

Alright, we all can agree that most of the average Internet users completely
ignore everything about words like HTML, CSS, JavaScript, PHP and so on. We
can't, at these point blame the users: I don't know anything about the inner
workings of most of the things I use on a dally basis myself, so no big deal.
In spite of this, serving the user is not quite equivalent to _fooling_ him.
Giving the user something that actually works, but whose inner workings are
totally crippled, is absolutely wrong. The author of the mentioned article
furthermore says:

> If you can satisfy the usability needs of 100% of your users, yet your code
> doesn't validate, then arguably you need do no more.

I'm really strong about my disagreement here. Validation serves a purpose: that
is to minimize differences when rendering the website in different browsers. A
well validated page doesn't need any guess-based correction by the browser. And
Stuart talks about _usability_, whereas a website that doesn't validate will
have a harder time in meeting usability requirements for impaired persons. On
February 2006 there was a story about [Target](http://www.target.com/) (a
retailer), being sued because its pages were unaccessible by visually impaired
users. The retailer was accused of violating the California Unruh Civil Rights
Act, the California Disabled Persons Act and the Americans with Disabilities
Act. Needless to say, the website [still doesn't
validate](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.target.com) (it
doesn't even have a DOCTYPE).

So, why else standards (and especially web standards) are needed?

 1. **Standards make it easier for your browsers to render the pages.**

    HTML or CSS are, in a way, standards. I.e. a set of rule, meant as a markup
    language specification, to be followed in order to design a web page. On
    top of these specifications, people who write browsers have done their
    work.  Unfortunately, though, not all developers are able to, or care to,
    be strict regarding standards. That means that the browsers must have a way
    to correctly interpret some code even though it's fundamentally incorrect.
    What's the result of this? Browsers developers have to waste time into
    taking care of correcting the mistakes of web developers. This, in turn,
    gives web developers the chance to relax and write worse and worse code.
    And this makes browsers developers' life worse, and their work slower. In
    the end the users get nothing but worse

 2. **Standards make life easier for users.**

    We can take this off the Web Standards examples, and move to some "real
    life" cases. Ironically enough, the other day I was staring at my toilet
    seat for a while, and noticed that the holes in the toilet in which you can
    screw your seat in, are at a fixed distance, and just slightly larger than
    longer, so to give a little margin: i.e. if you want to buy a new toilet
    seat, the distance between the screws with which you attach it to the
    toilet must be between X and X+1 cm. So, when I went to the shop to get a
    new toilet seat, I didn't have to worry about the size. Vendors of toilets
    and vendors of seat had just agreed on a standard size. The result? No
    hassle for the user (me).

 3. **Search engines like standards.**

    Search engines don't like finding errors. If they have trouble parsing your
    pages, they may not get to your carefully chosen keywords, won't be able to
    find all those tightly focused meta tags. Your site will be crippled on any
    search engine results page. This is not good. A well designed website
    creates a clear channel, a road map, for search engines, so they know to go
    exactly where you want them to go and see exactly what you want them to
    see.

End of the list? Yes. This is all that matters, in the end, to the final user.
He doesn't care how, but in the end he gets better products. Of course there
are lots of side effects, e.g.:

 * Standards minimize the differences in the way your pages appear in
   different browsers.
 * Standards improve the quality of your code, hence the quality of your
   product.
 * Code that adheres to standards is easier to maintain.
 * Validating your code during the development process eases the discovery of
   flaws and mistakes.
 * Standards increase your value.

Before anyone could say that nobody needs a new article about web standards,
let me remind you that the following websites won't validate:

  * [www.google.com](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.google.com)
  * [www.yahoo.com](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.yahoo.com)
  * [www.microsoft.com](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.microsoft.com)
  * [www.aol.com](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.aol.com)
  * [www.digg.com](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.digg.com)
  * I could go on for hours...

This means that the standards-aware developer are just a tiny minority. The
rest, obviously, don't think that quality is a good asset for their websites.
Writing non-validating code is a big step backwards, on the path of perfection.

_Bibliography_

  * [http://www.modernlifeisrubbish.co.uk/article/web-standards-dont-matter-as-much-as-you-think](http://www.modernlifeisrubbish.co.uk/article/web-standards-dont-matter-as-much-as-you-think)
  * [http://validator.w3.org/docs/why.html](http://validator.w3.org/docs/why.html)
  * [http://next-design.com/resources/validation.htm](http://next-design.com/resources/validation.htm)

*[XHTML]: Extensible HyperText Markup Language
*[HTML]: HyperText Markup Language
*[PHP]: PHP: Hypertext Preprocessor
*[CSS]: Cascade Style Sheet
