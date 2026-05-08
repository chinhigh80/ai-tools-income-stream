#!/usr/bin/env python3
"""
gen_posts.py
Generate SEO-focused markdown articles from keyword ideas.
Uses a simple template; in production you could integrate with
Google Trends API, AnswerThePublic, or SERP data.
"""
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

def slugify(text):
    return text.lower().replace(" ", "-").replace("--", "-")

def main():
    parser = argparse.ArgumentParser(description="Generate a markdown article for the Hugo site.")
    parser.add_argument("--keyword", required=True, help="Keyword or topic for the article")
    parser.add_argument("--output", default=None, help="Output file path (default: site/content/posts/<slug>.md)")
    args = parser.parse_args()

    keyword = args.keyword.strip()
    if not keyword:
        print("Error: keyword cannot be empty")
        sys.exit(1)

    slug = slugify(keyword)
    date_str = datetime.now().strftime("%Y-%m-%d")
    title = keyword.title()

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path(f"site/content/posts/{slug}.md")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Front matter
    front_matter = f"""---
title: "{title}"
date: {date_str}
draft: false
tags: ["{keyword}", "review", "guide"]
categories: ["AI Tools"]
---
"""

    # Simple article template
    content = f"""# {title}

## Introduction

In this guide, we explore the best {keyword} options available today, focusing on value, performance, and suitability for different budgets.

## Why {keyword} Matters

Whether you're a student, professional, or hobbyist, having the right {keyword} can significantly boost your productivity and workflow.

## Top Picks

{{{{< affiliate name=\"Logitech MX Master 3\" >}}}}
{{{{< affiliate name=\"Anker PowerPort III Nano 20W\" >}}}}
{{{{< affiliate name=\"Microsoft Office 365 Personal\" >}}}}
{{{{< affiliate name=\"BenQ Eye-Care Monitor GL2480\" >}}}}

## How to Choose the Right {keyword}

1. **Determine your budget** – Set a clear price range.
2. **Identify key features** – Look for specs that match your use case.
3. **Read reviews** – Check user feedback and expert opinions.
4. **Consider compatibility** – Ensure it works with your existing setup.

## Conclusion

Investing in quality {keyword} pays off in the long run. Use the affiliate links above to purchase the products you need and support this site.

## Get the Premium Checklist

Want a printable checklist to help you choose the perfect {keyword}? [Get it now](/microtool/checkout/session) (Paystack test mode).

"""
    full_content = front_matter + content

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"Generated article: {output_path}")

if __name__ == "__main__":
    main()