# 🦁 Shrine Browser Lite v4.7.3

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v4.7.3):

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
### **Shrine Browser Lite Changelog**

#### **[4.7.3] - Unified Fullscreen UI - 2025-08-14**
This version unifies and refines fullscreen mode behavior across the entire app.

* **Changed:**
* **Improved F11 Behavior:** Fullscreen mode activated via the **F11** key now also hides all navigation interfaces (tab bar, address bar, etc.), providing the same immersive experience as fullscreen video.
* **Code Refactoring:** The logic for hiding and showing the UI has been centralized into a single function `_toggle_ui_for_fullscreen` to ensure consistency and cleaner code.

#### **[4.7.2] - Immersive Fullscreen UI - 2025-08-14**
Focus on improving the visual experience when watching videos.

* **Changed:**
* **UI Auto-Hide:** When entering fullscreen mode from a web page (for example, clicking the fullscreen button on YouTube), all browser interfaces (tab bar, address bar, bookmarks bar) are now automatically hidden.
* **UI Reappear:** The interface will automatically reappear when exiting fullscreen mode.

#### **[4.7.1] - Web Fullscreen Support - 2025-08-14**
Added core functionality to support fullscreen requests from the web.

* **Added:**
* **Web Fullscreen API Support:** Added support for fullscreen requests originating from JavaScript in web pages.
* **Video Fullscreen Button Functionality:** The fullscreen button on video players like YouTube now works and will make the browser window fullscreen.

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
