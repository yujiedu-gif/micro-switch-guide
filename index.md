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
        <picture class="cutaway-image">
          <source srcset="{{ '/assets/images/micro-switch-exploded-cutaway.avif' | relative_url }}" type="image/avif">
          <img src="{{ '/assets/images/micro-switch-exploded-cutaway.png' | relative_url }}" width="900" height="900" alt="Generic SPDT micro switch cutaway showing the lever, plunger, snap mechanism, contacts, housing, and COM, NC, and NO terminals" fetchpriority="high">
        </picture>
        <ol class="cutaway-callouts" aria-label="Micro switch structure labels">
          <li class="callout callout-left callout-lever"><span>Actuator lever</span><i aria-hidden="true"></i></li>
          <li class="callout callout-left callout-housing"><span>Housing cover</span><i aria-hidden="true"></i></li>
          <li class="callout callout-left callout-plunger"><span>Plunger</span><i aria-hidden="true"></i></li>
          <li class="callout callout-left callout-spring"><span>Snap-action spring</span><i aria-hidden="true"></i></li>
          <li class="callout callout-right callout-moving"><span>Moving contact</span><i aria-hidden="true"></i></li>
          <li class="callout callout-right callout-fixed"><span>Fixed contacts</span><i aria-hidden="true"></i></li>
          <li class="callout callout-right callout-terminals"><span>COM / NC / NO terminals</span><i aria-hidden="true"></i></li>
        </ol>
      </div>
      <figcaption><strong>Inside a generic SPDT switch</strong><span>The three external terminals represent COM, NC, and NO. Schematic construction; internal arrangements vary by design.</span></figcaption>
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
        <span class="topic-art" aria-hidden="true">
          <picture>
            <source srcset="{{ topic.image | replace: '.png', '.avif' | relative_url }}" type="image/avif">
            <img src="{{ topic.image | relative_url }}" width="560" height="560" alt="" loading="lazy" decoding="async">
          </picture>
        </span>
        <span class="topic-number" aria-hidden="true">0{{ forloop.index }}</span>
        <h3>{{ topic.name }}</h3>
        <p>{{ topic.description }}</p>
        <p class="topic-question"><span>Example question</span>{{ topic.question }}</p>
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
    <div class="launch-panel">
      <div class="launch-panel-intro">
        <p class="eyebrow">Library launch</p>
        <h3>The first practical guides are in preparation.</h3>
        <p>The library will begin with three questions that form a useful foundation for later application and troubleshooting guides.</p>
        <a class="text-link" href="{{ '/feed.xml' | relative_url }}">Follow the RSS feed</a>
      </div>
      <ol class="launch-directions" aria-label="Initial guide directions">
        <li><span>01</span><strong>Fundamentals</strong><small>How snap action and COM, NC, and NO contacts work.</small></li>
        <li><span>02</span><strong>Selection</strong><small>How to compare load, force, travel, actuator, and life ratings.</small></li>
        <li><span>03</span><strong>Waterproofing</strong><small>What sealing and ingress ratings do and do not tell you.</small></li>
      </ol>
    </div>
    {% endif %}
  </div>
</section>

<section class="method-section" aria-labelledby="method-heading">
  <div class="container">
    <div class="method-heading">
      <div>
        <p class="eyebrow">Editorial standard</p>
        <h2 id="method-heading">How each guide earns trust.</h2>
      </div>
      <a class="text-link" href="{{ '/about/#editorial-approach' | relative_url }}">Read our editorial approach</a>
    </div>
    <div class="trust-grid">
      <article><span>01</span><h3>Focused scope</h3><p>Each guide starts with one operating principle, selection decision, or field problem.</p></article>
      <article><span>02</span><h3>Checkable sources</h3><p>Technical claims point to standards, manufacturer documentation, or other primary material when appropriate.</p></article>
      <article><span>03</span><h3>Clear limitations</h3><p>Advice states the conditions, trade-offs, and application checks that can change the answer.</p></article>
    </div>
  </div>
</section>
