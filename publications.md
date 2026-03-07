---
layout: default
title: Publications
---

# Selected Publications
*Automatically synced from ORCID*

<div class="publications-list">
  {% for pub in site.data.publications %}
    <div class="pub-item" style="margin-bottom: 20px; border-left: 3px solid #0070f3; padding-left: 15px;">
      <strong style="font-size: 1.1rem; display: block;">{{ pub.title }}</strong>
      <span style="color: #666;">{{ pub.journal }}</span> | <span>{{ pub.year }}</span>
      {% if pub.url %}
        <br><a href="{{ pub.url }}" target="_blank" style="font-size: 0.9rem; color: #0070f3;">View Publication →</a>
      {% endif %}
    </div>
  {% endfor %}
</div>