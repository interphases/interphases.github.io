---
layout: default
title: Publications
---

# Selected Publications

<div class="publications-list">
  {% for pub in site.data.publications %}
    <div class="pub-item">
      <span class="pub-title">{{ pub.title }}.</span>
      <span class="pub-journal"><em>{{ pub.journal }}</em></span> 
      <span class="pub-year"><strong>{{ pub.year }}</strong></span>.
      
      {% if pub.url != "" %}
        <div class="pub-links">
          <a href="{{ pub.url }}" target="_blank">Full Text (DOI) →</a>
        </div>
      {% endif %}
    </div>
  {% endfor %}
</div>

<style>
  .pub-item {
    margin-bottom: 1.5rem;
    line-height: 1.6;
    padding-bottom: 1rem;
    border-bottom: 1px solid #eee;
  }
  .pub-title {
    display: block;
    font-weight: 500;
    margin-bottom: 0.2rem;
  }
  .pub-journal {
    color: #333;
  }
  .pub-year {
    color: #000;
  }
  .pub-links a {
    font-size: 0.85rem;
    color: #0070f3;
    text-decoration: none;
    font-weight: 600;
  }
  .pub-links a:hover {
    text-decoration: underline;
  }
</style>