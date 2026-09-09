# Shrine Browser Lite

Shrine Browser Lite is a desktop web browser (hybrid) built with **Python** and **PySide6**, using `QtWebEngine` and Webview2 (Chromium) as its rendering engine.

> **⚠️ Source Code Notice**
> The source code shared in this repository (`shrine_webtab.py`) is **version 2.6 only** — the **base project**. This is the version made public. It represents the core browser foundation and does **not** include the current/private version's features, later architectural changes, or optimizations (e.g. hybrid WebView2 engine, advanced tab memory management, Rust-backed modules, and other integrations found in newer internal builds).

## Overview

Shrine Browser Lite aims to provide a lightweight, customizable browsing experience with the essential features expected of a modern browser: tabs, bookmarks, history, downloads, ad blocking, and basic privacy controls.

## Core Features (v2.6 Base)

- **Tabbed Browsing** — core browsing tab handled by `ShrineWebTab`, built on `QWebEngineView` / `ShrinePage`
- **Ad Blocking** — network-level request interception via `ShrineAdBlocker` and `ShrineInterceptor`
- **Privacy & Security Panel** — dedicated panel for privacy-related settings
- **Cache & Cookie Management** — `CacheCookiePanel` and `CookieViewDialog` for inspecting and clearing cache/cookies
- **Bookmarks** — `BookmarkPanel` for saving and managing bookmarks
- **History** — `HistoryPanel` for browsing history
- **Downloads** — `DownloadPanel` for tracking downloaded files
- **Extensions Panel** — `ExtensionsPanel` for basic extension listing/management
- **Home Page Settings** — `HomePagePanel` for configuring the browser's home page
- **About Dialog** — standard `AboutDialog` with app info
- **PDF Printing Support** — via `QPrinter` / `QPrintDialog`
- **Custom Web Channel Bridge** — `ShrineBridge` (imported from `shrine_bridge`) for JS ↔ Python communication

## 🚀 Evolution — Current Version Highlights

The base project above continues to evolve into a more advanced, actively developed version (private/not included in this share). Some highlights of that evolution:

- **Hybrid WebView2 Engine** — selected sites are routed through a native `WebView2` engine alongside the default Chromium engine, with iframe/popup routing handled via a `pywebview` monkeypatch
- **Tab Memory Guard** — a multi-tier RAM management system (idle GC → freeze → swap → discard → emergency discard) that keeps background tabs from consuming excessive memory
- **Optional Rust-Backed Disk Cache** — a native `qt_cache` module for faster caching, with automatic fallback to the default Chromium cache if unavailable
- **WASM + LZ4 Session Compression** — compressed tab session storage for crash recovery, with a safe JSON fallback if the WASM module isn't present
- **SMTC Integration (Windows)** — native System Media Transport Controls, including a media flyout popup and AUMID matching per window
- **Tab Groups & Vertical Tab Panel** — advanced tab organization beyond the standard horizontal tab bar, including horizontal tab-split dragging
- **Multi-Profile System** — full profile picker (HTML-based and native dialog variants), guest mode, and per-profile window management
- **PWA Manager** — install and manage Progressive Web Apps directly from the browser
- **Built-in Password Manager** — dedicated dialog for credential storage
- **Wallpaper Engine & Theme System** — dynamic, theme-aware color palettes applied across the title bar, sidebar, and status bar
- **Windows Snap Layout Overlay** — native Windows 11-style window snapping
- **VPN & DNS Utilities** — built-in basic network configuration helpers
- **Backup & Restore** — dedicated dialog for backing up and restoring profiles/settings
- **AI Imaging & Image Search** — integrated image search manager and AI-assisted imaging window
- **Chrome Extension Support** — expanded extension manager beyond the base listing panel

> These features are part of the actively developed/private version and are **not included** in the base source code shared here.

---
Screenshot
<img width="1365" height="767" alt="Screenshot 2026-02-05 024944" src="https://github.com/user-attachments/assets/b00d066c-7850-4fba-a49f-ddb600aa07f6" />

<img width="1365" height="767" alt="Screenshot 2026-06-27 095125" src="https://github.com/user-attachments/assets/86cfbc75-7099-47ad-a118-c02176890c59" />

<img width="1365" height="767" alt="Screenshot 2026-06-27 095253" src="https://github.com/user-attachments/assets/cfe8e2c1-d90e-4095-a292-68e80c180726" />

<img width="1106" height="673" alt="Screenshot 2026-04-20 113247" src="https://github.com/user-attachments/assets/bbf10d39-335f-4221-b05c-b497ca1b32c6" />


---

## Tech Stack

| Component | Technology |
|---|---|
| UI Framework | PySide6 (Qt for Python) |
| Rendering Engine | QtWebEngine & Webview2 (Chromium) |
| Language | Python 3 |

## Project Structure (Base)

```
shrine_webtab.py     # Main tab/browser widget and core UI panels
shrine_bridge.py      # Web channel bridge module (required, not included in this share)
```

> Note: `shrine_bridge.py` is imported by the main file but is not included in this base share. It must be provided separately for the application to run standalone.

## Requirements

- Python 3.x
- PySide6
- `requests`

Install dependencies:

```bash
pip install PySide6 requests
```

## Running

```bash
python shrine_webtab.py
```

## Disclaimer

This repository contains the **v2.6 base project** of Shrine Browser Lite, shared publicly for reference/learning purposes. It is **not** the current or complete version of the application — the actively developed/private version includes significantly more features and architectural changes not present here.

## License

No license specified. All rights reserved by the author unless stated otherwise.
