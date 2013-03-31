date: 2012-02-06 17:39:29
slug: manipulating-the-url-query-string-with-django-and-multiplechoicefields
title: Manipulating the URL query string with Django and MultipleChoiceFields
category: Software
tags: Django

## The problem


Sometimes you want to add and remove URL parameters without knowing what's
already there. Say you are currently generating this URL:

```
/search/?q=foo&filter=bar&page=2
```

and, in that page, you have a button called _Remove filters_ that should link
to:

```
/search/?q=foo&page=2
```


## The solution

[This Django snippet](http://djangosnippets.org/snippets/2237/) implements a
template tag called _query_string_ that works like this:

```
{% query_string '' '' %}
```

where the first argument contains URL parameters that you want to add or
modify, and the second one includes URL parameters that you want to remove.


## Examples

```html
<a href="{% query_string '' 'filter' %}">
    Remove filters
</a>

<a href="{% query_string 'page=3' '' %}">
    Go to page 3
</a>
```


## The problem with this approach

While this approach has worked great for me for a while, I eventually hit a
stumbling block: if you have a form for a group of checkboxes, and are
submitting said form via GET, you will end up with an URL that looks like:

```
/search/?q=foo&opts=1&opts=2&opts=3
```

See how the `opts` parameter repeats several times? That's a design flaw if you
ask me, but that's how HTTP seems to work.

When the URL parameters are pulled out of Django's `QueryDict`, only the last
one is preserved, i.e. `opts=3`, so you'd lose the tick on some checkboxes.

To prevent that, I have modified the `query_string` snippet. Here's a version
that works with `MultipleChoiceFields`, and multiple occurrences of the same
URL parameter in general (I have replaced only the functions I modified. Please
refer to the original snippet for the rest.)

```python
class QueryStringNode(Node):
    def __init__(self, add,remove):
        self.add = add
        self.remove = remove

    def render(self, context):
        p_list = []
        p_dict = {}
        query = context["request"].GET
        for k in query:
            p_list.append([k, query.getlist(k)])
            p_dict[k] = query.getlist(k)

        return get_query_string(
            p_list, p_dict,
            self.add, self.remove,
            context)

def get_query_string(p_list, p_dict,
                    new_params, remove,
                    context):
    """
    Add and remove query parameters.
    From `django.contrib.admin`.
    """
    for r in remove:
        p_list = [[x[0], x[1]]\
            for x in p_list if not x[0].startswith(r)]
    for k, v in new_params.items():
        if k in p_dict and v is None:
            p_list = [[x[0], x[1]]\
                for x in p_list if not x[0] == k]
        elif k in p_dict and v is not None:
            for i in range(0, len(p_list)):
                if p_list[i][0] == k:
                    p_list[i][1] = [v]

        elif v is not None:
            p_list.append([k, [v]])

    for i in range(0, len(p_list)):
        if len(p_list[i][1]) == 1:
            p_list[i][1] = p_list[i][1][0]
        else:
            p_list[i][1] = mark_safe(
                '&'.join(
                    [u'%s=%s' % (p_list[i][0], k)
                        for k in p_list[i][1]]))
            p_list[i][0] = ''
        try:
            p_list[i][1] = template.Variable(
                p_list[i][1]).resolve(context)
        except:
            pass

    return mark_safe(
        '?' +
        '&'.join(
            [k[1] if k[0] == ''
                  else u'%s=%s' % (k[0], k[1])
                  for k in p_list]).replace(' ', '%20'))
```

Hope this helps.
