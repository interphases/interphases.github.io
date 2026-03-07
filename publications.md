---
layout: default
title: Publications
---

<script src="https://cdn.jsdelivr.net/gh/vkaravir/bib-publication-list@master/src/bib-list.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/vkaravir/bib-publication-list@master/src/bib-list.css">

# Publications
From Orcid

<table id="pubTable" class="display"></table>

<script type="text/javascript">
    $(document).ready(function() {
        bibtexify("publications.bib", "pubTable", {
            "visualization": false,
            "sorting": [["year", "desc"]]
        });
    });
</script>

<style>
    /* ACS-specific tweaks */
    .bibtex-title { font-weight: bold; display: block; }
    .bibtex-author { color: #555; }
    .bibtex-journal { font-style: italic; }
    #pubTable { width: 100%; border-collapse: separate; border-spacing: 0 15px; }
</style>