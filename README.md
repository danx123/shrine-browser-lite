# 🦁 Shrine Browser Lite v4.7.0

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v4.7.0):

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

📜 Changelog - Version 4.7.0 (Security, Bug Fixes, Multi-Language Support, Media Playback)
🔐 Security
Credential Hashing Implementation: The credential storage system (username & password) has been completely overhauled for security.

Passwords are no longer stored in plaintext.

Now using SHA-256 hashing with a unique salt per password and strengthened with PBKDF2. This means the original password cannot be recovered from the stored data, drastically improving security.

Credential Dialog Update: The dialog for adding and editing credentials has been adjusted. When editing, users must enter a new password because the old password cannot be displayed.

Important Warning to Users: Due to this storage format change, the old credentials.json file must be manually removed from each profile folder to avoid conflicts.

🛠️ Bug Fixes (Fixed)
Cookie Panel: Fixed a critical crash that occurred when users tried to open the "View Active Cookies" panel. This function now runs stably and displays the cookie list as expected.

Cache Clearing: Fixed an issue with the "Clear Browser Cache" function that often failed due to a system file lock. The cache clearing process is now more reliable, relying solely on the QtWebEngine internal API, without force-deleting the folder.

🔓 Unlock button in the profile dialog to unlock a locked profile

🌏 Multilingual Support

▶️ Media Playback

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
