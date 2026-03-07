---
layout: default
title: Publications
---

# Selected Publications
*Formatted in ACS Style • Auto-synced from ORCID*

<div class="publications-list">
  {% for pub in site.data.publications %}
    <div class="pub-item">
      <span class="pub-authors">{{ pub.authors }}.</span>
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
    margin-bottom: 2rem;
    line-height: 1.6;
    padding-bottom: 1rem;
    border-bottom: 1px solid #f0f0f0;
  }
  .pub-authors {
    display: block;
    color: #1a1a1a;
    margin-bottom: 4px;
  }
  .pub-title {
    font-weight: 500;
    color: #444;
  }
  .pub-journal {
    color: #000;
  }
  .pub-year {
    color: #000;
  }
  .pub-links a {
    display: inline-block;
    margin-top: 8px;
    font-size: 0.85rem;
    color: #0070f3;
    text-decoration: none;
    border: 1px solid #0070f3;
    padding: 2px 8px;
    border-radius: 4px;
    transition: all 0.2s;
  }
  .pub-links a:hover {
    background: #0070f3;
    color: white;
  }
</style>