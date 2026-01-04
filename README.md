# 🦁 Shrine Browser Lite v14.1.0
Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v14.1.0):

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
📜 Shrine Browser Lite v14.1.0
Major Release

Overview
Version 14.1.0 is a major architectural milestone for Shrine Browser Lite.
This release introduces a Hybrid Engine Architecture, advanced process transparency, and deeper system-level control, designed to solve long-standing codec, DRM, and performance limitations without compromising stability or compliance.

✨ Key Highlights

Hybrid Engine Architecture

Introduced a dual-engine system combining Qt WebEngine and OS-native WebView.

Automatic and contextual engine switching for websites requiring proprietary codecs and DRM.

Ensures compatibility with H.264, MP3/AAC, and DRM-based streaming platforms without embedding restricted codecs.

Engine isolation to prevent failure propagation and maintain system stability.


Advanced Process Management

New Process Monitor integrated into the side panel.

Real-time, read-only visibility of background processes and engine activity.

Improved child process lifecycle management to prevent zombie processes and memory leaks.


Performance & Stability Enhancements

Refined Extreme Performance Mode with safer global application scope.

Optimized Chromium flags tuning while preserving crash safety.

Improved memory usage, CPU efficiency, and startup performance across low-end and modern systems.


System Transparency & Control

Clear separation of engine ownership, process hierarchy, and resource allocation.

Enhanced failure isolation between main engine and hybrid engine.

Improved fallback behavior for unsupported or unstable websites.


Architecture & Maintainability

Modularized internal components to support long-term scalability.

Strengthened internal routing, engine decision logic, and window parenting.

Prepared foundation for future debugging, diagnostics, and enterprise-focused tooling.


Notes

This release represents a significant internal rewrite and expansion.

Version 14.1.0 prioritizes architectural integrity, transparency, and sustainability over short-term features.


QtWebEngine Version: 6.10.1

Chromium Version: 134.0.6998.208
Chromium Security Patch Version: 142.0.7444.162
JavaScript V8: 13.4.114.21


---

## 📸 Screenshots
<img width="1365" height="767" alt="Cuplikan layar 2026-01-04 002519" src="https://github.com/user-attachments/assets/e850846f-2d29-4db7-b6c7-2001895cd6a8" />







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
