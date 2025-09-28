# 🦁 Shrine Browser Lite v5.5.5

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v5.5.5):

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
📜 Shrine Browser Lite v5.5.5 Changelog
This is a significant update focused on improving the user experience (UX), adding advanced custom features, and improving stability based on feedback.

✨ New Features
Interactive Profile Menu:
The profile icon in the top left corner now functions as a menu button.
Displays a list of all currently open tabs, allowing quick, one-click navigation.
Displays a list of the five most recently closed tabs, making it easy to reopen accidentally closed pages.
Tab Preview Tooltip:
Hovering your mouse over a tab will display a custom tooltip.
The tooltip displays a thumbnail of the webpage content in that tab.
Includes information about estimated memory usage by the renderer process, providing insight into which tabs are consuming the most resources. (Requires the psutil library).
Force Dark Mode for Web Content:
Adds a new option in the Appearance > Theme menu to force a dark appearance on website content.
This feature intelligently injects CSS to change webpage colors to a dark theme, even on sites that don't have a built-in dark mode.
It can be enabled/disabled as desired and will take effect on new tabs or after reloading existing tabs.
Per-Site Zoom Persistence:
The browser now automatically remembers the zoom level you set for each domain.
When you revisit the site, the saved zoom level will be reapplied automatically, eliminating the need to reset the zoom every time.
🎨 Enhancements & Changes
Chrome-Style Custom Link Tooltip:
Replaces the default link tooltip with a custom status bar that appears in the bottom-left corner of the browser window.
Provides a cleaner, more modern look and is consistent with major browsers like Google Chrome.
The status bar will automatically disappear after a few seconds or when the cursor is no longer hovering over the link.
🛠️ Bug Fixes
Tab Preview Stability Fix:
Fixed a TypeError that occurred when attempting to create a tab preview thumbnail.
This issue was caused by a mismatch between the standard Python BytesIO object and the QIODevice expected by Qt/PySide6.
Solution: Implemented the use of Qt's QBuffer and QByteArray to process images in memory, ensuring full compatibility and stability.
Fixed Dark Mode Content Effectiveness:
Fixed an issue where the "Force Dark Mode" feature was not working on some websites.
This issue was caused by inappropriate timing and execution environment of the injected script.
Solution: Changed the injection point to DocumentReady and the world ID to MainWorld to ensure CSS scripts have the proper priority and access to effectively modify the web page's appearance.


---

## 📸 Screenshots
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/c71a02f9-4f6f-4f2c-afb0-4e8ee75a271c" />




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
