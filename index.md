---
title: Micro Switch Guide
description: Practical, plain-English guides to micro switch fundamentals, selection, waterproofing, troubleshooting, and applications.
permalink: /
---

<section class="hero">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Micro switch knowledge, clearly explained</p>
      <h1>Make better micro switch decisions.</h1>
      <p class="hero-copy">Understand how micro switches work, compare the specifications that matter, and apply them more reliably in real products.</p>
      <div class="hero-actions">
        <a class="button" href="{{ '/guides/' | relative_url }}">Browse all guides</a>
        <a class="text-link" href="{{ '/about/' | relative_url }}">How this site works</a>
      </div>
    </div>
    <figure class="hero-cutaway">
      <div class="cutaway-stage">
        <picture>
          <source srcset="{{ '/assets/images/micro-switch-exploded-cutaway.avif' | relative_url }}" type="image/avif">
          <img src="{{ '/assets/images/micro-switch-exploded-cutaway.png' | relative_url }}" width="900" height="900" alt="Exploded cutaway illustration showing the lever, plunger, snap spring, contacts, housing, and three terminals of a micro switch" fetchpriority="high">
        </picture>
      </div>
      <figcaption><strong>Inside a snap-action switch</strong><span>Schematic construction; internal arrangements vary by design.</span></figcaption>
    </figure>
  </div>
</section>

<section class="topic-section" aria-labelledby="topics-heading">
  <div class="container">
    <div class="section-heading split-heading">
      <div>
        <p class="eyebrow">Start with your question</p>
        <h2 id="topics-heading">Explore by topic</h2>
      </div>
      <p>From first principles to field diagnosis, each collection is designed around a practical engineering task.</p>
    </div>
    <div class="topic-grid">
      {% for topic in site.data.topics %}
      <a class="topic-card" href="{{ '/guides/' | append: '#' | append: topic.slug | relative_url }}">
        <span class="topic-number">0{{ forloop.index }}</span>
        <h3>{{ topic.name }}</h3>
        <p>{{ topic.description }}</p>
        <span class="card-link">Explore topic</span>
      </a>
      {% endfor %}
    </div>
  </div>
</section>

<section class="latest-section" aria-labelledby="latest-heading">
  <div class="container">
    <div class="section-heading split-heading">
      <div>
        <p class="eyebrow">Recently published</p>
        <h2 id="latest-heading">Latest guides</h2>
      </div>
      {% if site.posts.size > 0 %}<a class="text-link" href="{{ '/guides/' | relative_url }}">View every guide</a>{% endif %}
    </div>
    {% if site.posts.size > 0 %}
    <div class="post-grid">
      {% for post in site.posts limit: 3 %}
        {% include post-card.html post=post %}
      {% endfor %}
    </div>
    {% else %}
    <div class="empty-state">
      <p class="eyebrow">Editorial library</p>
      <h3>The first guides are being prepared.</h3>
      <p>New articles will cover fundamentals, selection tradeoffs, sealed construction, troubleshooting, and real-world applications.</p>
      <a class="text-link" href="{{ '/feed.xml' | relative_url }}">Follow the RSS feed</a>
    </div>
    {% endif %}
  </div>
</section>

<section class="method-section">
  <div class="container method-grid">
    <div>
      <p class="eyebrow">A practical editorial standard</p>
      <h2>Useful before it is promotional.</h2>
    </div>
    <div>
      <p>Every guide begins with the operating principle or selection problem, defines technical terms in context, and separates general engineering guidance from product-specific information.</p>
      <a class="text-link" href="{{ '/about/' | relative_url }}">Read our editorial approach</a>
    </div>
  </div>
</section>
