# 🦁 Shrine Browser Lite v4.9.2

Shrine Browser Lite is a lightweight, fast, and efficient locally developed browser with high performance, low RAM consumption, and a modular design and modern features similar to high-end browsers.

## ⚠️ Night Build Source (v2.6)

> The currently available source code is Night Build v2.6.

> This version is an early stage of development and **does not yet reflect the full features of the latest stable version.**

### 🛠 Differences from the stable version (v4.9.2):

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

#### **\[4.9.2] - Profile Security & New Themes — 2025-08-19**

**Added:**

* **Password Protection per Profile (Optional)**

* Each profile can now be password protected.
* Passwords are not stored in plain text or `.json` files, but are protected using **SHA-256** to ensure security.
* When unlocking a locked profile, the user is required to enter the corresponding password.

* **New Themes**

* **Neon Blue** — A modern, glowing blue theme with futuristic accents.
* **Dark Blue** — A dark look with elegant blue tones for easy viewing.
* **Soft Pink** — A soft theme with a calming, aesthetic pink tone.

**Improved:**

* Improved security in the profile data storage system.
* Minor improvements to UI rendering performance when switching themes.

---

## 📸 Screenshots
<img width="1021" height="703" alt="Screenshot 2025-08-19 172212" src="https://github.com/user-attachments/assets/8745a3b9-3d37-418f-b8ce-f553e4c6fd63" />

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
