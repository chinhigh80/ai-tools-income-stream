---
title: "Blog"
description: "Latest articles on AI tools, productivity apps, and budget tech."
date: 2024-01-01
type: "blog"
---

Welcome to the blog section where we post regular updates, reviews, and guides.

{{ if .Paginator.HasPrev }}
<a href="{{ .Paginator.Prev.URL }}" class="btn btn-primary">Newer Posts</a>
{{ end }}
{{ if .Paginator.HasNext }}
<a href="{{ .Paginator.Next.URL }}" class="btn btn-primary ml-2">Older Posts</a>
{{ end }}

<ul>
{{ $paginator := .Paginate (where .Site.RegularPages "Section" "blog") }}
{{ range $paginator.Pages }}
<li>
<a href="{{ .RelPermalink }}">{{ .Title }}</a>
<span>{{ .Date.Format "Jan 2, 2006" }}</span>
</li>
{{ end }}
</ul>
