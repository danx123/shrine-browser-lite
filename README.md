# 🦁 Shrine Browser Lite v4.8.1

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v4.8.1):

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
📌 Shrine Browser Lite v4.8.1 – Changelog
✨ New Features

Internationalization (I18n) expanded
Added new language support:
🇧🇷 Portuguese (Brazil), 🇨🇳 Chinese, 🇩🇪 German, 🇪🇸 Spanish, 🇫🇷 French, 🇯🇵 Japanese, 🏳️ Javanese, 🏳️ Sundanese, 🇷🇺 Russian, 🇹🇭 Thai.

Profile Dialog with a new design (Stack Card)

Support for colored avatars and initials.

Profile wallpaper for dialog backgrounds.

Quick actions on each card: Launch, Edit, Delete, Unlock.

🔐 Security

Improved credential system (SHA-256 hash with salt).

Profile unlock option via card dialog.

🎨 UI/UX

Interactive profile card design with hover and rounded borders.

Light and dark themes now support the new card style.

Language selection dropdown directly within the Profile Dialog.

🛠️ Improvements

Fixed a bug with default language loading (fallback to English).

Improved stability of profile management and settings storage.

---

## 📸 Screenshots
<img width="1018" height="706" alt="Screenshot 2025-08-16 203551" src="https://github.com/user-attachments/assets/07631f9a-ab9d-4c96-8029-58177d70745d" />
<img width="1365" height="767" alt="Screenshot 2025-08-16 203610" src="https://github.com/user-attachments/assets/8edcf9a2-a526-47fc-9c63-179b7844491e" />














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
