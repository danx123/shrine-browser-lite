# 🦁 Shrine Browser Lite v4.7.7

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v4.7.7):

- History still uses the `.txt` format
- The credential system is still dummy (not saved)
- Bookmarks do not use a database (SQLite)
- The extension management panel is not yet available
- Navigation and download functions **are now working properly**

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
# Changelog — Shrine Browser Lite

## \[4.7.7] – Download Manager & Save Location Fix — 2025-08-15

The focus of this release: a much clearer, more controlled, and more accurate download experience.

### Added

* **Download Progress Dialog (non-blocking):** a new progress dialog that allows users to continue using the browser while downloading; it displays the file name, a progress bar, and a **Cancel** button. The dialog automatically closes when the download status is not "in progress." Connects to `receivedBytesChanged`, `totalBytesChanged`, and `stateChanged` for real-time progress.
* **App version updated in About:** version string now shows `4.7.7 (Download Dialog Fixed)`.

### Changed

* **Explicit file save flow:** when a download request is made, it now issues a **Save As** (`QFileDialog.getSaveFileName`) and then sets the directory and filename via `setDownloadDirectory()` and `setDownloadFileName()` before `accept()`. This ensures the file is saved in the exact location the user selected.
* **Integration with Download Panel & bubble notifications:** every new download is immediately registered in the panel, the final status is mapped to a neat text (“✅ Completed”, “🚫 Canceled”, “⚠️ Failed”) and a short bubble appears at start/finish.

### Fixed

* **Fixed Location for downloads:** fixed a save location bug—the path now always follows the user's choice from the dialog, instead of an unwanted fallback.
* **Clean up signal connections:** performs a safe disconnect when the download is complete to prevent leaking/duplicating callbacks; the progress dialog also clears its signals when closed.

---

## 📸 Screenshots
<img width="1365" height="767" alt="Screenshot 2025-08-13 211604" src="https://github.com/user-attachments/assets/2712d8cb-9344-48b0-b0e3-88c8b33f5f57" />












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
