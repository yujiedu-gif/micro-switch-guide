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
  {% if site.posts.size > 0 %}
    {% for topic in site.data.topics %}
      {% assign topic_posts = site.posts | where: 'category', topic.name %}
      {% if topic_posts.size > 0 %}
      <section class="guide-topic" id="{{ topic.slug }}" aria-labelledby="{{ topic.slug }}-heading">
        <div class="topic-intro">
          <p class="topic-number" aria-hidden="true">0{{ forloop.index }}</p>
          <h2 id="{{ topic.slug }}-heading">{{ topic.name }}</h2>
          <p>{{ topic.description }}</p>
        </div>
        <div class="guide-topic-content" data-guide-list>
          <div class="post-grid">
          {% for post in topic_posts limit: 6 %}
            {% include post-card.html post=post %}
          {% endfor %}
          </div>
          {% if topic_posts.size > 6 %}
          <div class="guide-list-actions" data-guide-actions hidden>
            <button
              class="guide-list-toggle"
              type="button"
              aria-controls="{{ topic.slug }}-more"
              aria-expanded="false"
              data-guide-toggle
              data-collapsed-label="View all {{ topic_posts.size }} guides"
              data-expanded-label="Show fewer guides"
            >
              <span data-guide-toggle-label>View all {{ topic_posts.size }} guides</span>
              <span class="guide-list-toggle-icon" aria-hidden="true">+</span>
            </button>
          </div>
          <div class="post-grid guide-overflow" id="{{ topic.slug }}-more" data-guide-overflow>
          {% for post in topic_posts offset: 6 %}
            {% include post-card.html post=post %}
          {% endfor %}
          </div>
          {% endif %}
        </div>
      </section>
      {% endif %}
    {% endfor %}
  {% else %}
  <section class="library-launch" aria-labelledby="library-launch-heading">
    <div class="library-launch-heading">
      <p class="eyebrow">Building the library</p>
      <h2 id="library-launch-heading">Five focused collections, published carefully.</h2>
      <p>We are preparing the first guides now. This directory will switch to the published article library automatically as content is added.</p>
    </div>
    <ol class="library-topic-list">
      {% for topic in site.data.topics %}
      <li id="{{ topic.slug }}">
        <span class="topic-number" aria-hidden="true">0{{ forloop.index }}</span>
        <div><h3>{{ topic.name }}</h3><p>{{ topic.description }}</p></div>
      </li>
      {% endfor %}
    </ol>
  </section>
  {% endif %}
</div>

<script src="{{ '/assets/js/guides.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
