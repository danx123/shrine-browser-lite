# 🦁 Shrine Browser Lite v2.8.2

**Shrine Browser Lite** adalah browser ringan, cepat, dan efisien buatan lokal dengan performa tinggi, konsumsi RAM rendah, serta didesain dengan struktur modular dan fitur modern layaknya browser kelas atas.

## ⚠️ Night Build Source (v2.6)

> Source code yang tersedia saat ini merupakan versi **Night Build v2.6**.  
> Versi ini merupakan tahapan awal dari pengembangan, dan **belum mencerminkan fitur penuh dari versi stabil terbaru.**

### 🛠 Perbedaan dengan versi stabil (v2.8.2):

- History masih menggunakan format `.txt`
- Sistem kredensial masih dummy (belum tersimpan)
- Bookmark belum menggunakan database (SQLite)
- Belum tersedia panel manajemen ekstensi
- Fungsi navigasi dan download **sudah berfungsi dengan baik**

👉 **Untuk versi stabil dan fitur lengkap**, silakan unduh dari halaman [Releases](https://github.com/danx123/shrine-browser-lite/releases).

---

## 🚀 Fitur Utama (versi stabil)

- UI modern & ringan
- Multi-tab support
- Bookmark manager berbasis SQLite
- Manajemen kredensial (simpan otomatis)
- View source page
- Modular system: `shrine_storage`, `shrine_cache`, `macan_ext`, dll
- Pengaturan tema & halaman beranda
- GPU rendering optimization
- RAM usage sangat efisien, cocok untuk multitasking
- Sudah dilengkapi installer & siap digunakan secara portable


---

## 📂 Struktur Folder Penting

```
Shrine Browser Lite/
│
├── shrine_storage/
│   ├── Cookies, Favicon, History, Trust Tokens, etc.
│   └── Local & Session Storage
│
├── shrine_cache/
│   └── Cache_Data/ – Menyimpan data website untuk loading cepat
│
├── shrine_settings/
│   └── user_prefs.json – Berisi konfigurasi user
```

---

## 📝 Changelog v2.8.2

- [✔] Fix bug add tab yang menyebabkan crash
- [✔] Perbaikan login akun Google agar lebih persist
- [✔] Popup simpan kredensial + auto-login
- [✔] Toolbar bookmark + panel pengelola bookmark
- [✔] Optimasi internal (RAM usage, storage handling, dll)

---

## 📸 Screenshots

| Tabs & Bookmark | Task Manager RAM Usage |
|-----------------|------------------------|
<img width="1365" height="767" alt="Screenshot 2025-08-07 150814" src="https://github.com/user-attachments/assets/2c9189bd-4ccf-4348-96cd-801675624ae1" />


---

## 👨‍💻 Developer

Project ini dibuat dan dikembangkan oleh **Danx Exodus**, dengan semangat inovasi, pembelajaran mandiri, dan konsistensi update untuk memberikan pengalaman browsing terbaik tanpa beban sistem.

---

## 🤝 Kontribusi

Ingin berkolaborasi? Jangan ragu untuk [open issue](https://github.com/username/shrine-browser-lite/issues) atau ajukan pull request! Shrine Browser Lite terbuka untuk pengembangan bersama yang sehat & produktif.

---

## 📜 Lisensi

MIT License – Bebas digunakan, dipelajari, dimodifikasi, dan dibagikan selama menyertakan atribusi yang sesuai.

---

> Shrine Browser Lite – Dari yang awalnya hanya proyek iseng, kini menjelma jadi browser yang powerful, hemat memori, dan penuh fitur seperti buatan perusahaan besar.
