# 🦁 Shrine Browser Lite v3.5.0

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v3.5.0):

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

## 📝 Changelog v3.5.0

Shrine Browser Lite Changelog
v3.5.0 (August 8, 2025)
This version focuses on fundamentally improving the user experience (UX) by introducing more standard window functionality and a more intuitive tab interface.

✨ New Features:

Main Window Now Resizable: Full implementation of resizing the main window. You can now easily drag any edge (top, bottom, left, right) and any corner of the window to resize it as desired, providing full layout flexibility.

"Add Tab" Button Next to Tabs: The + button for opening a new tab has been moved from the navigation toolbar to a more familiar position to the right of the last tab. This speeds up workflow and mimics modern browser design.

🛠️ Fixes & Improvements:

Header UI Structure: The header layout has been overhauled to accommodate the new "Add Tab" button. The tab bar will now dynamically fill the available space.

Toolbar Optimizations: The old "Add Tab" button has been removed from the main navigation toolbar to eliminate redundancy and clean up the interface.

Mouse Handling Improvements: The logic for detecting mouse movements and clicks has been refined to differentiate between window moves, window resizing, and interactions with control buttons.

QSS Updates: The stylesheets (QSS) for the light and dark themes have been updated to style the new "Add Tab" button to be consistent with the app's visual theme.

Note: Previous versions (such as v3.3.0) focused on fixing bugs related to maximizing windows and bookmark toolbar functionality.

Added light and dark mode themes
Changed Total UI to Frameless
Added AutoUpdate feature to GitHub
Refactor Total UI

## 📸 Screenshots

| Tabs & Bookmarks | Task Manager RAM Usage |
|------------------|----------------------------------|
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/010a8135-690f-47be-adae-238fa2d35f21" />


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
