# AI Tools Income Stream

A fully open‑source mini‑income‑stream system that combines:

* **SEO‑focused static blog** (Hugo) targeting AI tools, productivity apps, and budget tech gear.
* **Affiliate product injection** (Amazon Associates, ready for ShareASale later).
* **Paystack payment gateway** (test mode) for a micro‑SaaS upsell (e.g., a downloadable checklist or price‑tracker).
* **Google AdSense integration** for additional ad revenue.
* **Docker‑Compose** for local development and easy VPS deployment.
* **GitHub Actions** auto‑deploy workflow (push to `main` rebuilds and redeploys).
* **Article generator script** that creates SEO‑optimized markdown posts from keyword ideas.

## Quick Start (Local)

```bash
# Clone the repo
git clone https://github.com/chinhigh80/ai-tools-income-stream.git
cd ai-tools-income-stream

# Copy environment example and fill in your keys
cp .env.example .env
# Edit .env with your Paystack test keys and AdSense info

# Build and run
docker compose up --build
```

* Site: http://localhost:1313  
* Micro‑tool API docs: http://localhost:8000/docs  

## Deployment to a $5 VPS

See [`DEPLOY.md`](DEPLOY.md) for a step‑by‑step guide (DigitalOcean, Linode, Vultr, or any Ubuntu server).

## Project Structure

```
.
├─ site/                     # Hugo source
│   ├─ content/
│   │   └─ posts/            # markdown articles (generated via script)
│   ├─ data/
│   │   └─ affiliates.yaml   # affiliate product definitions
│   ├─ layouts/
│   │   ├─ partials/
│   │   │   ├─ adsense-top.html
│   │   │   ├─ adsense-bottom.html
│   │   │   └─ affiliate.html
│   │   └─ shortcodes/
│   │       └─ affiliate.html
│   ├─ assets/
│   │   └─ css/
│   └─ config.toml
├─ microtool/                # FastAPI app (Paystack upsell)
│   ├─ app/
│   │   ├─ main.py
│   │   ├─ routes/
│   │   │   ├─ checkout.py
│   │   │   └─ webhook.py
│   │   ├─ models/
│   │   └─ db/
│   ├─ Dockerfile
│   └─ requirements.txt
├─ scripts/
│   ├─ gen_posts.py          # keyword → markdown article
│   └─ deploy.sh             # VPS provisioning helper
├─ docker-compose.yml
├─ .github/
│   └─ workflows/
│       └─ deploy.yml        # GitHub Actions CI/CD
└─ README.md
```

## License

MIT – feel free to fork, modify, and earn!
