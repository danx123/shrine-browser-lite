# 🦁 Shrine Browser Lite v4.2.0

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v4.2.0):

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

---

---

## **📝 Changelog – Shrine Browser Lite v4.2.0**

**Release Date:** August 11, 2025
**Release Type:** Major Update 🚀

### **✨ New Features**

1. **Custom Profile Support**

* Each user now has a **unique ID** and **profile name**.
* The ID and name are displayed in the **top left corner** and in the **profile menu**.
* The **Rename** option is available directly from the profile menu.
* Profile data is stored in `profile.json` so it persists after the app is closed.
* Separate cache and storage for each profile

2. **Profile Integration into the Home Page**

* Profiles are automatically *injected* into `home.html` using **ShrineBridge**.
* The name and ID appear dynamically every time the page is opened.
* Supports instant updates after changing the profile name.

3. **UI and Logic Refactor**

* Separated profile logic from the browser core to facilitate development.
* Restructured the code structure to be more **modular** and **readable**.
* Prepared for profile data integration with advanced features like personalized bookmarks.

---

### **⚡ Optimizations & Improvements**

* Optimized `home.html` loading speed when profile data changes.
* Removed obsolete and unused code to improve performance.
* Fixed a minor bug in the menu bar that caused labels to not refresh.

---

---

## 📸 Screenshots
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/a0a13f4a-fda8-4d56-81bb-2634daa8958d" />










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
