# Micro Switch Guide

A lightweight English educational blog about micro switch fundamentals, selection, waterproofing, troubleshooting, and applications. It is built with Jekyll and designed for free hosting on GitHub Pages.

## One-time setup

1. Push this project to the `main` branch of the public `yujiedu-gif/micro-switch-guide` repository.
2. In **Settings → Pages**, choose **Deploy from a branch**, then select `main` and `/(root)`.
3. The production address is `https://www.microswitchguide.com/`; GitHub Pages remains the hosting origin.

## Publish an article

1. Copy `_drafts/article-template.md` to `_posts/`.
2. Rename it using `YYYY-MM-DD-short-descriptive-title.md`.
3. Complete the front matter and replace the template copy with the article.
4. Use one of the exact category names below so the article appears in the correct section:
   - `Basics`
   - `Selection Guides`
   - `Waterproof Switches`
   - `Troubleshooting`
   - `Applications`
5. Commit and push to `main`. GitHub Pages rebuilds the site automatically.

Only include `official_url` when an article has a directly relevant official ZINGEAR page. Do not copy an existing article from the official website; write an original guide that serves a distinct reader question.

## Local preview

This project matches GitHub Pages' pinned Jekyll environment.

The local project includes an isolated Ruby environment under the ignored `work/` directory. Start the site with:

```bash
./bin/site serve
```

Then open `http://127.0.0.1:4000/micro-switch-guide/`.

To preview unpublished drafts:

```bash
./bin/site drafts
```

Run a production build with:

```bash
./bin/site build
```

On a fresh computer, install Ruby 3.3 and run `bundle install` once before using the helper.

## Change navigation or topics

- Edit `_data/navigation.yml` to change the primary navigation.
- Edit `_data/topics.yml` to change topic names and descriptions.
- If a topic name changes, update the category value in all affected posts.

## Custom domain

The canonical production domain is `www.microswitchguide.com`.

1. Keep the repository `CNAME` file set to `www.microswitchguide.com`.
2. In Cloudflare DNS, point the `www` CNAME to `yujiedu-gif.github.io` with proxying disabled.
3. Point the apex domain to GitHub Pages using the four documented A records.
4. Keep the domain configured in **Settings → Pages** and enable **Enforce HTTPS** after the certificate is ready.

Article links use Jekyll URL helpers, so article body content does not need to change when the domain is connected.
