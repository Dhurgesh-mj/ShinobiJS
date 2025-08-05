# 🥷 ShinobiJS - Advanced JavaScript Recon Tool

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

**ShinobiJS** is a stealthy, fast, and powerful JavaScript recon tool for bug bounty hunters, security researchers, and penetration testers.

---

## ✨ Features

- 🔎 Crawl websites and discover JavaScript files
- 📦 Detect `import()` dynamic imports
- 🌐 Extract `fetch()` and `axios` endpoints
- 🔑 Identify secrets, API keys, and tokens
- 🧠 Beautiful terminal UI with [Rich]
- 🚀 Fully asynchronous analysis for speed
- 🥷 Built for stealth and performance

---

## 📦 Installation

### Requirements

- Python 3.8+
- pip

```bash
git clone https://github.com/yourname/ShinobiJS.git
cd ShinobiJS
pip install -r requirements.txt
```

> Optional: Add to `PATH` or install with `setup.py` for global use.

---

## 🚀 Usage

```bash
python main.py https://example.com
```

### Example Output:

```
🔗 Target: https://example.com
⏳ Crawling pages...
🕸️ Pages Crawled: 27
📦 External JS Files Found: 13
🧠 Inline Script Blocks Found: 5

🔍 External JS Files
➤ https://example.com/assets/main.js
➤ https://cdn.jsdelivr.net/library.min.js

🔬 Analyzing JS files for endpoints, secrets, and dynamic imports...

📦 Dynamic Imports
import: ./pages/dashboard.js

🌐 Fetched Endpoints
fetch: /api/login
fetch: https://example.com/graphql

🔑 Secrets / Tokens
secret: apiKey=AIza...

✅ Recon Complete
Stay stealthy, Shinobi. 🥷
```

---

## 🧠 Modules

- `core/crawler.py` - fast, multi-depth web crawler
- `core/extractor.py` - parses JS `<script>` tags and `.js` references
- `core/parser.py` - extracts JS secrets, fetch URLs, source maps, etc.

---

## 🛠 Development

```bash
# Run in debug mode
python main.py https://testsite.com

# Customize depth, timeout (coming soon)
```

---

## 📁 Project Structure

```
ShinobiJS/
├── main.py
├── core/
│   ├── crawler.py
│   ├── extractor.py
│   └── parser.py
├── requirements.txt
└── README.md
```

---

## ✅ To-Do / Coming Features

- [ ] `--json` output support
- [ ] `--depth` and `--threads` options
- [ ] JS beautifier for inline scripts
- [ ] TUI dashboard interface
- [ ] Docker support

---

## 📜 License

[MIT License](LICENSE)

---

## 💬 Author

Created by **[@yourname](https://github.com/yourname)**  
Feel free to star ⭐, fork 🍴, and contribute 🔧!
