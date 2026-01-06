# 🦁 Shrine Browser Lite v14.3.8
Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v14.3.8):

👉 **For the stable and full-featured version**, please download from the [Releases] page (https://github.com/danx123/shrine-browser-lite/releases).

---

## 🚀 Main Features (stable version)

- Modern & lightweight UI
- Multi-tab support
- SQLite-based bookmark manager
- Credential management (auto-save)
- View page source
- Modular system: `shrine_storage`, `shrine_cache`, `macan_ext`, etc.
- Theme & homepage settings
- GPU rendering optimization
- Highly efficient RAM usage, suitable for multitasking
- Installer included & ready to use portable

---

## 📂 Important Folder Structure

```
Shrine Browser Lite/
│
├── shrine_storage/
│ ├── Cookies, Favicon, History, Trust Tokens, etc.
│ └── Local & Session Storage
│
├── shrine_cache/
│ └── Cache_Data/ – Stores website data for fast loading
│
├── shrine_settings/
│ └── user_prefs.json – Contains user configuration
```
---
📜 Shrine Browser Lite v14.3.8
Release Highlights

Introduced Chicken Sleep Mode
A lightweight hybrid engine suspension mechanism that preserves identity, session, and process state without full termination.
Enables seamless tab continuity while preventing zombie processes and session fragmentation.

Hybrid Engine Stability Enhancement
Improved state handoff between Qt WebEngine and Hybrid WebView, ensuring smoother transitions without UI freeze or identity loss.

Session & Identity Preservation
Optimized hybrid lifecycle management to maintain authentication context across engine switches.

Process Lifecycle Optimization
Refined spawn, sleep, and resume flow to reduce memory pressure and background process leaks.

Overall Reliability Improvements
Enhanced failure isolation and recovery behavior for complex multi-engine scenarios.

Optimized Context Menu in Hybrid Mode


> Shrine Browser Lite remains “Lite” by name — not by capability.


QtWebEngine Version: 6.10.1

Chromium Version: 134.0.6998.208
Chromium Security Patch Version: 142.0.7444.162
JavaScript V8: 13.4.114.21


---

## 📸 Screenshots
<img width="1365" height="767" alt="Cuplikan layar 2026-01-04 231103" src="https://github.com/user-attachments/assets/b693059e-94ea-4cd5-a3f1-79adb879d378" />
<img width="1365" height="767" alt="Cuplikan layar 2026-01-04 231117" src="https://github.com/user-attachments/assets/ae4ffbfc-b7ad-4427-bd0b-f9551f7a84a7" />









---

## 👨‍💻 Developer

This project is created and developed by **Danx Exodus**, with a spirit of innovation, self-learning, and consistent updates to provide the best browsing experience without system load.

---

## 🤝 Contribution

Want to collaborate? Feel free to [open an issue](https://github.com/username/shrine-browser-lite/issues) or submit a pull request! Shrine Browser Lite is open for healthy and productive collaborative development.

---

## 📜 License

MIT License – Free to use, study, modify, and share as long as proper attribution is included.

---

> Shrine Browser Lite – What started as a fun project has now become a powerful, memory-efficient, and feature-packed browser like those made by major companies.
