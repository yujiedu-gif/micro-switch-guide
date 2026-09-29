---
title: Micro Switch Guides
description: Browse practical micro switch guides by topic, from basic operating principles to selection, waterproofing, troubleshooting, and applications.
permalink: /guides/
---

<section class="page-hero compact-hero">
  <div class="container">
    <p class="eyebrow">Knowledge library</p>
    <h1>Micro switch guides</h1>
    <p>Find clear explanations organized around the decisions engineers, buyers, and product teams make most often.</p>
  </div>
</section>

<div class="container guide-directory">
  {% for topic in site.data.topics %}
    {% assign topic_posts = site.posts | where: 'category', topic.name %}
    <section class="guide-topic" id="{{ topic.slug }}" aria-labelledby="{{ topic.slug }}-heading">
      <div class="topic-intro">
        <p class="topic-number">0{{ forloop.index }}</p>
        <h2 id="{{ topic.slug }}-heading">{{ topic.name }}</h2>
        <p>{{ topic.description }}</p>
      </div>
      {% if topic_posts.size > 0 %}
      <div class="post-grid">
        {% for post in topic_posts %}
          {% include post-card.html post=post %}
        {% endfor %}
      </div>
      {% else %}
      <p class="empty-note">Guides for this topic will appear here as they are published.</p>
      {% endif %}
    </section>
  {% endfor %}
</div>

