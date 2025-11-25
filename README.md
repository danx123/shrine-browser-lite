# 🦁 Shrine Browser Lite v11.4.0
Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v11.4.5):

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
📜 Shrine Browser Lite v11.4.5
New Features
Native HTML Interfaces: Migrated History, About, and Downloads menus from legacy dialogs to fully responsive HTML pages for a modern, native browser experience.
Download Persistence: Implemented a persistent download history system. Download logs are now saved to downloads.json located specifically within the user's profile directory, ensuring data isolation between profiles.
Enhanced File Management: Added functionality to the Downloads page allowing users to open files directly or reveal them in the system file explorer (Show in Folder).
Improvements
URL Masking: Implemented smart address bar masking for internal pages. Internal file paths (e.g., file:///.../history.html) are now displayed cleanly as "History", "About", or "Downloads".
Internal Navigation: Refactored the main menu to open internal pages in new tabs via the open_internal_page helper method.

QtWebEngine Version: 6.10.1

Chromium Version: 134.0.6998.208
Chromium Security Patch Version: 142.0.7444.162
JavaScript V8: 13.4.114.21


---

## 📸 Screenshots
<img width="1365" height="721" alt="Screenshot 2025-11-25 082223" src="https://github.com/user-attachments/assets/a6142af3-f73e-4d80-a365-db6d3236aca9" />
<img width="1365" height="721" alt="Screenshot 2025-11-25 082322" src="https://github.com/user-attachments/assets/af05a417-298c-402c-8903-f2ad92f6fac9" />
<img width="1365" height="717" alt="Screenshot 2025-11-25 082250" src="https://github.com/user-attachments/assets/30f4edce-b476-429b-b175-b6699831a201" />




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
