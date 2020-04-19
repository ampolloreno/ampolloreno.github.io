---
layout: math_default
title: Blog
---
<h1>Posts</h1>

<ul>
  {% for post in site.posts %}
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
  {% endfor %}
</ul>
