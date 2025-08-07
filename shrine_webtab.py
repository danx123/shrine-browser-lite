import os
import sys
import subprocess
import requests
from io import BytesIO
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QLabel, QProgressBar, QFileDialog, QTabWidget, QMessageBox, QListWidget, QListWidgetItem,
    QDialog, QTextEdit, QDialogButtonBox, QMenu, QInputDialog
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import (
    QWebEngineProfile, QWebEngineUrlRequestInterceptor, QWebEnginePage, QWebEngineScript, QWebEngineDownloadRequest
)
from PyQt6.QtCore import QUrl, QTimer, Qt, QByteArray, pyqtSignal, QProcess, QStandardPaths
from PyQt6.QtGui import QPixmap, QIcon, QPainter, QDesktopServices, QAction
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog

import re
import shutil
import json
from datetime import datetime
from collections import deque
from PyQt6.QtWidgets import QApplication

# Pastikan file shrine_bridge.py ada di direktori yang sama
from shrine_bridge import ShrineBridge

# --- SVG ICONS ---
SVG_BACK = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>"""
SVG_FORWARD = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>"""
SVG_REFRESH = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 4v6h-6"/><path d="M1 20v-6h6"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>"""
SVG_GO = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>"""
SVG_ZOOM_IN = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>"""
SVG_ZOOM_OUT = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>"""
SVG_ZOOM_RESET = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 2v6h6"/><path d="M21 22v-6h-6"/><path d="M3 11.5A10 10 0 0 1 12 2a10 10 0 0 1 9 10.5"/><path d="M21 12.5a10 10 0 0 1-18 0"/></svg>"""
SVG_NEW_TAB = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14m-7-7h14"/></svg>"""
SVG_CLONE_TAB = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>"""
SVG_BOOKMARK = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>"""
SVG_TRASH = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>"""
SVG_MENU = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>"""

# --- KELAS DARI about.py YANG DIINTEGRASIKAN ---
class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tentang Shrine Browser")
        self.setMinimumSize(450, 400)
        
        self.layout = QVBoxLayout()

        self.title_label = QLabel("Shrine Browser Lite")
        self.title_label.setStyleSheet("font-weight: bold; font-size: 16px;")

        self.description = QTextEdit()
        self.description.setReadOnly(True)
        self.description.setHtml("""
            <p><b>🌌 A Sovereign Browser for the Expressive Soul</b></p>
            <p>Crafted not to compete, but to liberate—<br>
            Macan Shrine is a browser born from glyphs, rituals, and symbolic depth.<br>
            It rejects cluttered paradigms and embraces modular elegance.</p>
            <p>🧭 Navigate with purpose. 🐾 Log with meaning. 🎴 Render with reverence.</p>
            <p><i>Designed by Danx Exodus, woven with code and philosophy.</i></p>
            <p><i>Contact: </i></p>
            <p><i>WhatsApp: +6289626479736</i></p>
            <p><i>E-mail: danxdigitalsolution@gmail.com</i></p>
        """)

        self.readme_btn = QPushButton("📖 Buka Readme (PDF)")
        self.readme_btn.clicked.connect(self.open_readme_pdf)

        self.footer = QLabel("🌀 ‘Each click is a ritual. Each log is a glyph.’")
        self.footer.setStyleSheet("color: gray; font-style: italic;")
        
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        buttons.accepted.connect(self.accept)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.description)
        self.layout.addWidget(self.readme_btn)
        self.layout.addWidget(self.footer)
        self.layout.addWidget(buttons)
        self.setLayout(self.layout)

    def open_readme_pdf(self):
        pdf_filename = "Shrine Browser.pdf"
        pdf_path = os.path.abspath(pdf_filename)
        if os.path.exists(pdf_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText(f"File tidak ditemukan!")
            msg.setInformativeText(f"Pastikan file '{pdf_filename}' berada di folder yang sama dengan aplikasi.")
            msg.setWindowTitle("Error")
            msg.exec()

# --- KELAS-KELAS PANEL PENGATURAN ---
class PanelDialog(QDialog):
    """Wrapper dialog untuk panel pengaturan."""
    def __init__(self, panel_widget, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumSize(500, 400)
        layout = QVBoxLayout(self)
        layout.addWidget(panel_widget)
        
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)
        
        self.setLayout(layout)

class CookieViewDialog(QDialog):
    def __init__(self, cookies_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Daftar Cookie Aktif")
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout(self)
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setText(cookies_text)
        layout.addWidget(self.text_area)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)

class CacheCookiePanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.cache_path = QWebEngineProfile.defaultProfile().cachePath()
        
        layout = QVBoxLayout(self)
        self.label_cache = QLabel()
        self.update_cache_label()
        self.label_cache.setWordWrap(True)
        
        recalc_btn = QPushButton("🔄 Hitung Ulang Ukuran Cache")
        recalc_btn.clicked.connect(self.update_cache_label)
        
        clear_cache_btn = QPushButton("🧽 Hapus Cache Browser")
        clear_cache_btn.clicked.connect(self.clear_cache)
        
        layout.addWidget(self.label_cache)
        layout.addWidget(recalc_btn)
        layout.addWidget(clear_cache_btn)
        layout.addSpacing(20)
        
        clear_cookie_btn = QPushButton("🔥 Hapus Semua Cookie")
        clear_cookie_btn.clicked.connect(self.clear_cookies)
        layout.addWidget(clear_cookie_btn)
        
        view_cookie_btn = QPushButton("🍪 Lihat Cookie Aktif")
        view_cookie_btn.clicked.connect(self.view_cookies)
        layout.addWidget(view_cookie_btn)
        
        self.status_cookie = QLabel("🍪 Status: Cookie aktif.")
        layout.addWidget(self.status_cookie)
        layout.addStretch()

    def get_folder_size(self, path):
        total = 0
        try:
            for entry in os.scandir(path):
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += self.get_folder_size(entry.path)
        except (FileNotFoundError, PermissionError):
            return 0
        return total

    def update_cache_label(self):
        size_bytes = self.get_folder_size(self.cache_path)
        size_mb = size_bytes / (1024 * 1024)
        self.label_cache.setText(f"📦 Path Cache: {self.cache_path}\n"
                                 f"💾 Ukuran Saat Ini: {size_mb:.2f} MB")

    def clear_cache(self):
        try:
            QWebEngineProfile.defaultProfile().clearHttpCache()
            shutil.rmtree(self.cache_path, ignore_errors=True)
            self.update_cache_label()
            self.main_window.showBubble("🧹 Cache telah dibersihkan!")
        except Exception as e:
            QMessageBox.critical(self, "Error Cache", f"Gagal membersihkan cache: {e}")
            self.main_window.showBubble("❌ Gagal bersihkan cache.")

    def clear_cookies(self):
        store = QWebEngineProfile.defaultProfile().cookieStore()
        store.deleteAllCookies()
        self.status_cookie.setText("🍪 Semua cookie telah dihapus.")
        self.main_window.showBubble("🍪 Semua cookie telah dihapus.")

    def view_cookies(self):
        store = QWebEngineProfile.defaultProfile().cookieStore()
        cookies_list = []
        def handle_cookies(qweb_cookies):
            for cookie in qweb_cookies:
                cookies_list.append(f"Nama: {cookie.name().data().decode()}\n"
                                    f"Value: {cookie.value().data().decode()}\n"
                                    f"Domain: {cookie.domain()}\n"
                                    f"Path: {cookie.path()}\n"
                                    f"Kedaluwarsa: {cookie.expirationDate().toString()}\n"
                                    f"Secure: {cookie.isSecure()}\n"
                                    f"HttpOnly: {cookie.isHttpOnly()}\n"
                                    f"----------------------------------------\n")
            dialog = CookieViewDialog("".join(cookies_list) if cookies_list else "Tidak ada cookie.", self.main_window)
            dialog.exec()
        store.loadAllCookies(handle_cookies)

class ShrineAdBlocker(QWebEngineUrlRequestInterceptor):
    def __init__(self, patterns):
        super().__init__()
        self.patterns = patterns
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if any(p in url for p in self.patterns):
            info.block(True)

class PrivacySecurityPanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)
        adblock_info = QLabel("🛡️ Adblock: Block iklan & domain berbahaya.")
        layout.addWidget(adblock_info)
        self.status_adblock = QLabel("Adblock belum aktif.")
        layout.addWidget(self.status_adblock)
        enable_adblock_btn = QPushButton("🧼 Aktifkan Adblock")
        enable_adblock_btn.clicked.connect(self.activate_adblock)
        layout.addWidget(enable_adblock_btn)
        layout.addSpacing(20)
        tracking_info = QLabel("🕵️ Anti-Tracking: Mencegah pelacakan data.")
        layout.addWidget(tracking_info)
        self.tracker_list = QListWidget()
        layout.addWidget(self.tracker_list)
        self.load_tracker_patterns()
        layout.addSpacing(20)
        self.credentials_file = "shrine_settings/credentials.json"
        credential_info = QLabel("🔐 Kredensial: Kelola data login yang tersimpan.")
        layout.addWidget(credential_info)
        self.status_credential = QLabel("Kredensial belum tersimpan.")
        layout.addWidget(self.status_credential)
        save_btn = QPushButton("💾 Simpan Login")
        delete_btn = QPushButton("🔥 Hapus Semua Login")
        save_btn.clicked.connect(self.save_credentials)
        delete_btn.clicked.connect(self.delete_credentials)
        h_layout = QHBoxLayout()
        h_layout.addWidget(save_btn)
        h_layout.addWidget(delete_btn)
        layout.addLayout(h_layout)
        self.load_credentials()

    def activate_adblock(self):
        try:
            with open("shrine_settings/easylist.txt", "r", encoding="utf-8") as f:
                easylist = [line.strip() for line in f if line.strip() and not line.startswith("#")]
            interceptor = ShrineAdBlocker(easylist)
            QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)
            self.status_adblock.setText(f"🛡️ Adblock aktif ({len(easylist)} rules)")
            print(f"✅ Loaded {len(easylist)} adblock rules.")
        except FileNotFoundError:
            self.status_adblock.setText("⚠️ easylist.txt tidak ditemukan.")
            print("❌ Error: easylist.txt tidak ditemukan!")
        except Exception as e:
            self.status_adblock.setText("⚠️ Gagal aktifkan adblock.")
            print(f"❌ Error loading easylist.txt: {e}")

    def load_tracker_patterns(self):
        tracker_file = "tracker.txt"
        if os.path.exists(tracker_file):
            try:
                with open(tracker_file, "r") as file:
                    for line in file:
                        pattern = line.strip()
                        if pattern and not pattern.startswith("#"): self.tracker_list.addItem(f"📡 {pattern}")
            except Exception as e: self.tracker_list.addItem(f"⚠️ Gagal memuat tracker.txt: {e}")
        else: self.tracker_list.addItem("⚠️ tracker.txt tidak ditemukan.")

    def save_credentials(self):
        creds = {"username": "macan_pengintai", "token": "xxxx-xxxx-xxxx"}
        try:
            os.makedirs(os.path.dirname(self.credentials_file), exist_ok=True)
            with open(self.credentials_file, "w") as f: json.dump(creds, f, indent=2)
            self.status_credential.setText("✅ Kredensial tersimpan")
            self.main_window.showBubble("✅ Kredensial tersimpan.")
        except Exception as e:
            QMessageBox.warning(self, "⚠️ Gagal Simpan", f"Terjadi error: {e}")
            self.main_window.showBubble("❌ Gagal simpan kredensial.")

    def load_credentials(self):
        if os.path.exists(self.credentials_file):
            try:
                with open(self.credentials_file, "r") as f: creds = json.load(f)
                self.status_credential.setText(f"🔐 Login sebagai: {creds.get('username', 'tidak diketahui')}")
            except Exception as e: self.status_credential.setText(f"⚠️ Gagal membaca kredensial: {e}")

    def delete_credentials(self):
        try:
            if os.path.exists(self.credentials_file): os.remove(self.credentials_file)
            self.status_credential.setText("🧹 Semua kredensial dihapus")
            self.main_window.showBubble("🧹 Kredensial dihapus.")
        except Exception as e:
            QMessageBox.warning(self, "⚠️ Gagal Hapus", f"Terjadi error: {e}")
            self.main_window.showBubble("❌ Gagal hapus kredensial.")

class DownloadPanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        open_folder_btn = QPushButton("📂 Buka Folder Unduhan")
        open_folder_btn.clicked.connect(self.open_download_folder)
        layout.addWidget(open_folder_btn)

    def add_download(self, item_id, filename):
        item = QListWidgetItem(f"🔄 Mengunduh: {filename}")
        item.setData(Qt.ItemDataRole.UserRole, item_id)
        self.list_widget.addItem(item)
        return item
    
    def update_download(self, item_id, progress, status_text, filename):
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.data(Qt.ItemDataRole.UserRole) == item_id:
                item.setText(f"{status_text} ({progress}%) - {filename}")
                break

    def finish_download(self, item_id, status_text, filename):
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.data(Qt.ItemDataRole.UserRole) == item_id:
                item.setText(f"{status_text} - {filename}")
                break

    def open_download_folder(self):
        download_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)
        if download_path and os.path.exists(download_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(download_path))
        else: QMessageBox.warning(self, "Error", "Tidak dapat menemukan folder unduhan.")

class HistoryPanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)
        self.history_list = QListWidget()
        self.history_list.itemDoubleClicked.connect(self.navigate_to_history)
        layout.addWidget(self.history_list)
        clear_btn = QPushButton("Hapus Riwayat")
        clear_btn.setIcon(self.main_window.create_svg_icon(SVG_TRASH))
        clear_btn.clicked.connect(self.clear_history_and_refresh)
        layout.addWidget(clear_btn)
        self.refresh_history()

    def refresh_history(self):
        self.history_list.clear()
        for item in reversed(self.main_window.history_log):
            self.history_list.addItem(QListWidgetItem(f"[{item['timestamp']}] {item['url']}"))

    def navigate_to_history(self, item):
        url_text = item.text().split('] ')[1]
        self.main_window.add_new_tab(QUrl(url_text))

    def clear_history_and_refresh(self):
        self.main_window.clear_history()
        self.refresh_history()
        
# --- FITUR BARU: PANEL HOMEPAGE & EKSTENSI ---
class HomePagePanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)

        info_label = QLabel("Masukkan URL lengkap untuk halaman utama Anda (homepage).")
        layout.addWidget(info_label)

        self.url_input = QLineEdit()
        self.url_input.setText(self.main_window.settings.get("homepage_url", "https://www.google.com"))
        layout.addWidget(self.url_input)

        save_btn = QPushButton("💾 Simpan Homepage")
        save_btn.clicked.connect(self.save_homepage)
        layout.addWidget(save_btn)
        
        layout.addStretch()
        self.setLayout(layout)

    def save_homepage(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "URL Kosong", "URL tidak boleh kosong.")
            return
        
        self.main_window.settings["homepage_url"] = url
        self.main_window.save_settings()
        self.main_window.showBubble(f"✅ Homepage disimpan: {url}")
        self.parent().parent().accept() # Menutup dialog

class ExtensionsPanel(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ext_dir = "macan_ext"
        os.makedirs(self.ext_dir, exist_ok=True)

        layout = QVBoxLayout(self)
        
        info_label = QLabel("Kelola ekstensi browser. Perubahan memerlukan restart browser.")
        info_label.setWordWrap(True)
        info_label.setStyleSheet("font-style: italic; color: gray;")
        layout.addWidget(info_label)

        self.ext_list = QListWidget()
        self.ext_list.itemChanged.connect(self.on_item_changed)
        layout.addWidget(self.ext_list)

        btn_layout = QHBoxLayout()
        add_btn = QPushButton("➕ Tambah Ekstensi")
        remove_btn = QPushButton("➖ Hapus Ekstensi")
        add_btn.clicked.connect(self.add_extension)
        remove_btn.clicked.connect(self.remove_extension)
        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(remove_btn)
        layout.addLayout(btn_layout)

        self.populate_list()
        self.setLayout(layout)

    def populate_list(self):
        self.ext_list.blockSignals(True)
        self.ext_list.clear()
        disabled_extensions = self.main_window.settings.get("disabled_extensions", [])
        
        for item_name in os.listdir(self.ext_dir):
            if os.path.isdir(os.path.join(self.ext_dir, item_name)):
                list_item = QListWidgetItem(item_name)
                list_item.setFlags(list_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                if item_name in disabled_extensions:
                    list_item.setCheckState(Qt.CheckState.Unchecked)
                else:
                    list_item.setCheckState(Qt.CheckState.Checked)
                self.ext_list.addItem(list_item)
        self.ext_list.blockSignals(False)

    def on_item_changed(self, item):
        ext_name = item.text()
        disabled_extensions = self.main_window.settings.get("disabled_extensions", [])

        if item.checkState() == Qt.CheckState.Unchecked:
            if ext_name not in disabled_extensions:
                disabled_extensions.append(ext_name)
        else:
            if ext_name in disabled_extensions:
                disabled_extensions.remove(ext_name)
        
        self.main_window.settings["disabled_extensions"] = disabled_extensions
        self.main_window.save_settings()
        self.main_window.showBubble("Perubahan ekstensi akan diterapkan setelah restart.")

    def add_extension(self):
        source_dir = QFileDialog.getExistingDirectory(self, "Pilih Folder Ekstensi", ".")
        if source_dir:
            ext_name = os.path.basename(source_dir)
            target_dir = os.path.join(self.ext_dir, ext_name)
            if os.path.exists(target_dir):
                QMessageBox.warning(self, "Ekstensi Sudah Ada", f"Ekstensi bernama '{ext_name}' sudah ada.")
                return
            try:
                shutil.copytree(source_dir, target_dir)
                self.populate_list()
                self.main_window.showBubble(f"✅ Ekstensi '{ext_name}' ditambahkan. Restart browser.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menyalin ekstensi: {e}")

    def remove_extension(self):
        current_item = self.ext_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Tidak Ada Pilihan", "Pilih ekstensi yang ingin dihapus.")
            return
        
        ext_name = current_item.text()
        reply = QMessageBox.question(self, "Konfirmasi Hapus",
                                     f"Anda yakin ingin menghapus ekstensi '{ext_name}' secara permanen?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                shutil.rmtree(os.path.join(self.ext_dir, ext_name))
                self.populate_list()
                self.main_window.showBubble(f"🧹 Ekstensi '{ext_name}' dihapus. Restart browser.")
            except Exception as e:
                 QMessageBox.critical(self, "Error", f"Gagal menghapus ekstensi: {e}")

# --- KELAS-KELAS INTI ---
class ShrineInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, parent_widget):
        super().__init__()
        self.main_widget = parent_widget
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if "googlevideo.com/videoplayback" in url:
            print(f"🎯 Video Detected: {url}")
            self.main_widget.start_video_download(url)

class ShrinePage(QWebEnginePage):
    def __init__(self, profile, parent=None, tab_callback=None, window_factory=None):
        super().__init__(profile, parent)
        self.tab_callback = tab_callback
        # --- PERUBAHAN DIMULAI: Tambahkan window_factory ---
        self.window_factory = window_factory
        # --- PERUBAHAN SELESAI ---

    def createWindow(self, window_type):
        # --- PERUBAHAN DIMULAI: Logika untuk membuka jendela baru ---
        # Jika diminta membuka pop-up atau jendela baru
        if window_type == QWebEnginePage.WebWindowType.WebBrowserWindow:
            if self.window_factory:
                new_window = self.window_factory() # Panggil fungsi pabrik jendela
                return new_window.current_webview().page()
        
        # Perilaku default untuk membuka tab baru (jika link menargetkan _blank tanpa js)
        if self.tab_callback:
            return self.tab_callback()
            
        return None
        # --- PERUBAHAN SELESAI ---

class ShrineWebTab(QWidget):
    DATA_FILE = "shrine_data.json"
    SETTINGS_FILE = "shrine_settings.json" # --- BARU ---
    FAVICON_CACHE_DIR = ".favicon_cache"
    HISTORY_MAX_ITEMS = 500

    # --- PERUBAHAN DIMULAI: Sinyal untuk memberitahu aplikasi tentang jendela baru ---
    windowClosed = pyqtSignal(object)
    # --- PERUBAHAN SELESAI ---

    def __init__(self, window_factory=None):
        super().__init__()
        self.window_factory = window_factory # Simpan fungsi pabrik
        
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

        self.bookmarks = []
        self.history_log = deque(maxlen=self.HISTORY_MAX_ITEMS)
        self.settings = {} # --- BARU ---
        
        self.load_data()
        self.load_settings() # --- BARU ---
        
        os.makedirs(self.FAVICON_CACHE_DIR, exist_ok=True)
        
        self.download_panel = DownloadPanel(self)
        self.downloads = {}

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setVisible(False)
        self.progress_bar.setTextVisible(False)

        self.video_download_process = QProcess(self)
        self.video_download_process.readyReadStandardOutput.connect(self.update_video_progress)
        self.video_download_process.readyReadStandardError.connect(self.handle_video_download_error)
        self.video_download_process.finished.connect(self.video_download_finished)

        self.shrine_bridge = ShrineBridge()
        self.shrine_bridge.messageReceived.connect(self.handle_js_message)
        self.channel = QWebChannel()
        self.channel.registerObject('shrineBridge', self.shrine_bridge)
        self.extension_scripts = self._load_extension_scripts_from_dir("macan_ext")
        
        self.add_new_tab()
        
    def closeEvent(self, event):
        # --- PERUBAHAN DIMULAI: Emit sinyal saat jendela ditutup ---
        self.windowClosed.emit(self)
        super().closeEvent(event)
        # --- PERUBAHAN SELESAI ---

    def _load_extension_scripts_from_dir(self, directory):
        scripts = []
        if not os.path.isdir(directory): return scripts
        
        # --- PERUBAHAN DIMULAI: Cek ekstensi yang dinonaktifkan ---
        disabled_extensions = self.settings.get("disabled_extensions", [])
        print(f"Ekstensi yang dinonaktifkan: {disabled_extensions}")
        # --- PERUBAHAN SELESAI ---
        
        for item_name in os.listdir(directory):
            # --- PERUBAHAN DIMULAI: Lewati jika dinonaktifkan ---
            if item_name in disabled_extensions:
                print(f"🚫 Melewatkan ekstensi nonaktif: {item_name}")
                continue
            # --- PERUBAHAN SELESAI ---
            
            item_path = os.path.join(directory, item_name)
            if os.path.isdir(item_path):
                script_file = os.path.join(item_path, "content_script.js")
                if os.path.exists(script_file):
                    try:
                        with open(script_file, "r", encoding='utf-8') as f:
                            scripts.append({"name": item_name, "source": f.read()})
                        print(f"✅ Berhasil memuat ekstensi: {item_name}")
                    except Exception as e:
                        print(f"❌ Gagal memuat ekstensi {item_name}: {e}")
        return scripts

    def inject_all_extensions(self, webview):
        for ext in self.extension_scripts:
            js_script = QWebEngineScript()
            js_script.setSourceCode(ext["source"])
            js_script.setInjectionPoint(QWebEngineScript.InjectionPoint.DocumentReady)
            js_script.setWorldId(QWebEngineScript.ScriptWorldId.MainWorld)
            webview.page().scripts().insert(js_script)

    def create_svg_icon(self, svg_data):
        renderer = QSvgRenderer(QByteArray(svg_data.encode('utf-8')))
        pixmap = QPixmap(24, 24)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return QIcon(pixmap)

    def load_data(self):
        try:
            if os.path.exists(self.DATA_FILE):
                with open(self.DATA_FILE, 'r') as f:
                    data = json.load(f)
                    self.bookmarks = data.get("bookmarks", [])
                    history_list = data.get("history", [])
                    self.history_log.extend(history_list)
                    print("💾 Data history dan bookmark dimuat.")
        except Exception as e:
            print(f"⚠️ Gagal memuat data: {e}. Membuat data baru.")
            self.bookmarks = []
            self.history_log = deque(maxlen=self.HISTORY_MAX_ITEMS)
            
    # --- FITUR BARU ---
    def load_settings(self):
        try:
            if os.path.exists(self.SETTINGS_FILE):
                with open(self.SETTINGS_FILE, 'r') as f:
                    self.settings = json.load(f)
                    print("⚙️ Pengaturan dimuat dari shrine_settings.json.")
            else:
                self.settings = {
                    "homepage_url": "https://www.google.com",
                    "disabled_extensions": []
                }
                print("⚙️ File shrine_settings.json tidak ditemukan, membuat pengaturan default.")
        except Exception as e:
            print(f"⚠️ Gagal memuat pengaturan: {e}. Menggunakan default.")
            self.settings = {}

    def save_data(self):
        try:
            with open(self.DATA_FILE, 'w') as f:
                data = {"bookmarks": self.bookmarks, "history": list(self.history_log)}
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"⚠️ Gagal menyimpan data: {e}")
            
    # --- FITUR BARU ---
    def save_settings(self):
        try:
            with open(self.SETTINGS_FILE, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"⚠️ Gagal menyimpan pengaturan: {e}")

    def handle_js_message(self, msg):
        print(f"Pesan dari JS: {msg}")
        self.showBubble(f"🛡️ {msg}")
    
    def add_new_tab(self, url=None):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        tab_layout.setContentsMargins(5, 5, 5, 5)

        webview = QWebEngineView()
        profile = QWebEngineProfile(f"ShrineProfile_{self.tab_widget.count()}_{id(self)}", self)
        interceptor = ShrineInterceptor(self)
        profile.setUrlRequestInterceptor(interceptor)
        
        # --- PERUBAHAN DIMULAI ---
        page = ShrinePage(profile, webview, tab_callback=self.spawn_tab_from_site, window_factory=self.window_factory)
        # --- PERUBAHAN SELESAI ---

        webview.setPage(page)
        page.setWebChannel(self.channel)
        self.inject_all_extensions(webview)
        page.linkHovered.connect(self.handle_link_hovered)
        page.profile().downloadRequested.connect(self.handle_download)

        # --- Toolbar ---
        nav_layout = QHBoxLayout()
        
        back_btn = QPushButton(self.create_svg_icon(SVG_BACK), "")
        back_btn.setToolTip("Mundur (Alt+Kiri)")
        forward_btn = QPushButton(self.create_svg_icon(SVG_FORWARD), "")
        forward_btn.setToolTip("Maju (Alt+Kanan)")
        refresh_btn = QPushButton(self.create_svg_icon(SVG_REFRESH), "")
        refresh_btn.setToolTip("Muat Ulang (F5)")
        new_tab_btn = QPushButton(self.create_svg_icon(SVG_NEW_TAB), "")
        new_tab_btn.setToolTip("Buka Tab Baru (Ctrl+T)")
        
        url_bar = QLineEdit()
        url_bar.setPlaceholderText("Masukkan URL atau cari...")
        
        go_btn = QPushButton(self.create_svg_icon(SVG_GO), "")
        go_btn.setToolTip("Pergi ke URL")
        
        zoom_in_btn = QPushButton(self.create_svg_icon(SVG_ZOOM_IN), "")
        zoom_in_btn.setToolTip("Perbesar")
        zoom_out_btn = QPushButton(self.create_svg_icon(SVG_ZOOM_OUT), "")
        zoom_out_btn.setToolTip("Perkecil")
        zoom_reset_btn = QPushButton(self.create_svg_icon(SVG_ZOOM_RESET), "")
        zoom_reset_btn.setToolTip("Reset Zoom")
        
        clone_btn = QPushButton(self.create_svg_icon(SVG_CLONE_TAB), "")
        clone_btn.setToolTip("Gandakan Tab")
        bookmark_btn = QPushButton(self.create_svg_icon(SVG_BOOKMARK), "")
        bookmark_btn.setToolTip("Tambah Bookmark")
        
        menu_btn = QPushButton(self.create_svg_icon(SVG_MENU), "")
        menu_btn.setToolTip("Menu Utama")
        
        # --- Koneksi Sinyal ---
        url_bar.returnPressed.connect(lambda: self.load_url(webview, url_bar.text()))
        go_btn.clicked.connect(lambda: self.load_url(webview, url_bar.text()))
        back_btn.clicked.connect(webview.back)
        forward_btn.clicked.connect(webview.forward)
        refresh_btn.clicked.connect(webview.reload)
        new_tab_btn.clicked.connect(self.add_new_tab)
        zoom_in_btn.clicked.connect(lambda: self.zoom_in(webview))
        zoom_out_btn.clicked.connect(lambda: self.zoom_out(webview))
        zoom_reset_btn.clicked.connect(lambda: self.zoom_reset(webview))
        clone_btn.clicked.connect(self.clone_current_tab)
        bookmark_btn.clicked.connect(self.add_bookmark)

        # --- Susunan Toolbar ---
        nav_layout.addWidget(back_btn)
        nav_layout.addWidget(forward_btn)
        nav_layout.addWidget(refresh_btn)
        nav_layout.addWidget(new_tab_btn) # Tombol Add Tab di sini
        nav_layout.addWidget(url_bar)
        nav_layout.addWidget(go_btn)
        nav_layout.addWidget(zoom_in_btn)
        nav_layout.addWidget(zoom_out_btn)
        nav_layout.addWidget(zoom_reset_btn)
        nav_layout.addWidget(clone_btn)
        nav_layout.addWidget(bookmark_btn)
        nav_layout.addWidget(menu_btn) # Tombol menu di ujung

        # --- Membuat Menu Dropdown ---
        self.main_menu = QMenu(self)
        menu_btn.setMenu(self.main_menu)
        
        print_action = QAction("🖨️ Cetak...", self)
        print_action.triggered.connect(lambda: self.print_page(webview.page()))
        self.main_menu.addAction(print_action)

        print_preview_action = QAction("📄 Simpan ke PDF", self)
        print_preview_action.triggered.connect(lambda: self.print_preview(webview.page()))
        self.main_menu.addAction(print_preview_action)
        
        self.main_menu.addSeparator()

        # --- Submenu Pengaturan ---
        settings_menu = self.main_menu.addMenu("⚙️ Pengaturan")

        history_action = QAction("📜 Buka Riwayat", self)
        history_action.triggered.connect(self.open_history_panel)
        settings_menu.addAction(history_action)

        cache_cookie_action = QAction("🍪 Buka Panel Cache/Cookie", self)
        cache_cookie_action.triggered.connect(self.open_cache_cookie_panel)
        settings_menu.addAction(cache_cookie_action)

        privacy_action = QAction("🛡️ Buka Panel Privasi", self)
        privacy_action.triggered.connect(self.open_privacy_security_panel)
        settings_menu.addAction(privacy_action)
        
        download_action = QAction("📥 Buka Panel Unduhan", self)
        download_action.triggered.connect(self.open_download_panel)
        settings_menu.addAction(download_action)
        
        # --- FITUR BARU: Menu item untuk Homepage dan Ekstensi ---
        settings_menu.addSeparator()
        
        homepage_action = QAction("🏠 Atur Homepage", self)
        homepage_action.triggered.connect(self.open_homepage_panel)
        settings_menu.addAction(homepage_action)
        
        extensions_action = QAction("🧩 Kelola Ekstensi", self)
        extensions_action.triggered.connect(self.open_extensions_panel)
        settings_menu.addAction(extensions_action)
        
        self.main_menu.addSeparator()

        about_action = QAction("🛕 Tentang", self)
        about_action.triggered.connect(self.show_about_dialog)
        self.main_menu.addAction(about_action)
        
        exit_action = QAction("🚪 Keluar", self)
        exit_action.triggered.connect(self.close)
        self.main_menu.addAction(exit_action)

        # --- Finalisasi Tab ---
        # --- PERUBAHAN DIMULAI: Gunakan URL dari pengaturan ---
        homepage_url = self.settings.get("homepage_url", "https://www.google.com")
        start_url = QUrl(url) if url else QUrl(homepage_url)
        # --- PERUBAHAN SELESAI ---
        
        webview.load(start_url)
        webview.urlChanged.connect(lambda qurl: self.on_url_changed(qurl, url_bar, tab))
        webview.titleChanged.connect(lambda title: self.update_tab_title(webview, title))
        webview.loadProgress.connect(self.progress_bar.setValue)
        webview.loadFinished.connect(lambda ok: self.progress_bar.setVisible(not ok))
        webview.loadStarted.connect(lambda: self.progress_bar.setVisible(True))
        
        tab_layout.addLayout(nav_layout)
        tab_layout.addWidget(webview)
        tab_layout.addWidget(self.progress_bar)
        
        self.tab_widget.addTab(tab, "🕸️ Tab Shrine")
        self.tab_widget.setCurrentWidget(tab)

    # --- Metode untuk membuka panel sebagai dialog ---
    def open_panel_as_dialog(self, panel_class, title):
        panel = panel_class(self)
        dialog = PanelDialog(panel, title, self)
        dialog.exec()
        
    def open_history_panel(self):
        panel = HistoryPanel(self)
        dialog = PanelDialog(panel, "📜 Riwayat Penjelajahan", self)
        dialog.exec()

    def open_cache_cookie_panel(self):
        self.open_panel_as_dialog(CacheCookiePanel, "🍪 Pengaturan Cache & Cookie")

    def open_privacy_security_panel(self):
        self.open_panel_as_dialog(PrivacySecurityPanel, "🛡️ Pengaturan Privasi & Keamanan")

    def open_download_panel(self):
        dialog = PanelDialog(self.download_panel, "📥 Daftar Unduhan", self)
        dialog.exec()

    # --- FITUR BARU: Metode untuk membuka panel baru ---
    def open_homepage_panel(self):
        self.open_panel_as_dialog(HomePagePanel, "🏠 Atur Homepage Default")

    def open_extensions_panel(self):
        self.open_panel_as_dialog(ExtensionsPanel, "🧩 Kelola Ekstensi")
        
    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec()

    def print_page(self, page: QWebEnginePage):
        # --- PERUBAHAN DIMULAI: Implementasi Print Dialog Lengkap ---
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            def callback(success):
                if success:
                    self.showBubble("✅ Dokumen dikirim ke printer.")
                else:
                    self.showBubble("⚠️ Gagal mencetak dokumen.")
            page.print(printer, callback)
        # --- PERUBAHAN SELESAI ---

    def print_preview(self, page: QWebEnginePage):
        path, _ = QFileDialog.getSaveFileName(self, "Simpan sebagai PDF", "", "PDF Files (*.pdf)")
        if path:
            def handle_print_result(success):
                if success:
                    self.showBubble("✅ PDF berhasil dibuat!")
                    QDesktopServices.openUrl(QUrl.fromLocalFile(path))
                else: self.showBubble("⚠️ Gagal membuat PDF.")
            page.printToPdf(path, handle_print_result)
            
    def clear_history(self):
        reply = QMessageBox.question(self, 'Konfirmasi',
                                     'Anda yakin ingin menghapus semua riwayat penjelajahan?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.history_log.clear()
            self.save_data()
            self.showBubble("Riwayat telah dibersihkan.")

    def start_video_download(self, url):
        save_path, _ = QFileDialog.getSaveFileName(self, "Simpan Video", "", "Video Files (*.mp4 *.mkv *.webm)")
        if not save_path:
            self.showBubble("🚫 Unduhan video dibatalkan.")
            return
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.showBubble(f"🎥 Mengunduh video...\n{os.path.basename(save_path)}")
        try:
            self.video_download_process.start("yt-dlp", ["--progress", "-o", save_path, url])
        except QProcess.ProcessError:
            QMessageBox.critical(self, "Error yt-dlp", "Gagal memulai yt-dlp. Pastikan terinstal dan ada di PATH.")
            self.showBubble("❌ Gagal memulai unduhan video.")
            self.progress_bar.setVisible(False)

    def update_video_progress(self):
        output = self.video_download_process.readAllStandardOutput().data().decode('utf-8', 'ignore')
        match = re.search(r"\[download\]\s+([0-9\.]+)%", output)
        if match: self.progress_bar.setValue(int(float(match.group(1))))

    def handle_video_download_error(self):
        error_output = self.video_download_process.readAllStandardError().data().decode('utf-8', 'ignore')
        print(f"❌ yt-dlp Error: {error_output}")
        self.showBubble(f"⚠️ Unduhan video gagal: {error_output.splitlines()[-1] if error_output else 'Unknown error'}")
        self.progress_bar.setVisible(False)

    def video_download_finished(self, exitCode, exitStatus):
        if exitStatus == QProcess.ExitStatus.NormalExit and exitCode == 0:
            self.progress_bar.setValue(100)
            self.showBubble("✅ Video berhasil diunduh!")
        else: self.showBubble("⚠️ Unduhan video gagal atau dibatalkan.")
        QTimer.singleShot(1000, lambda: self.progress_bar.setVisible(False))

    def current_webview(self):
        current_tab = self.tab_widget.currentWidget()
        if current_tab: return current_tab.findChild(QWebEngineView)
        return None

    def zoom_in(self, webview):
        if webview: webview.setZoomFactor(webview.zoomFactor() + 0.1)
    def zoom_out(self, webview):
        if webview: webview.setZoomFactor(webview.zoomFactor() - 0.1)
    def zoom_reset(self, webview):
        if webview: webview.setZoomFactor(1.0)
       
    def spawn_tab_from_site(self):
        self.add_new_tab()
        webview = self.current_webview()
        if webview: return webview.page()
        return None

    def clone_current_tab(self):
        webview = self.current_webview()
        if webview: self.add_new_tab(webview.url())

    def add_bookmark(self):
        webview = self.current_webview()
        if webview:
            url, title = webview.url().toString(), webview.title()
            if (title, url) not in self.bookmarks:
                self.bookmarks.append((title, url))
                self.showBubble(f"📌 Bookmark added:\n{title}")
                self.save_data()
            else: self.showBubble(f"ℹ️ Bookmark sudah ada:\n{title}")

    def on_url_changed(self, url, url_bar, tab):
        url_bar.setText(url.toString())
        url_bar.setCursorPosition(0)
        self.update_favicon(url, tab)
        if url.isValid() and not url.isLocalFile():
            url_str = url.toString()
            if not self.history_log or self.history_log[-1]['url'] != url_str:
                self.history_log.append({
                    "url": url_str,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                self.save_data()

    def update_favicon(self, url: QUrl, tab_widget: QWidget):
        domain = url.host()
        if not domain: return
        favicon_filename = os.path.join(self.FAVICON_CACHE_DIR, f"{domain.replace('.', '_')}.png")
        index = self.tab_widget.indexOf(tab_widget)
        if index == -1: return

        if os.path.exists(favicon_filename):
            icon = QIcon(favicon_filename)
            self.tab_widget.setTabIcon(index, icon)
            return

        try:
            response = requests.get(f"https://www.google.com/s2/favicons?domain={domain}&sz=32", timeout=3)
            response.raise_for_status()
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            if not pixmap.isNull():
                icon = QIcon(pixmap)
                self.tab_widget.setTabIcon(index, icon)
                pixmap.save(favicon_filename)
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Gagal ambil favicon untuk {domain}: {e}")

    def load_url(self, webview, url):
        cleaned = url.strip()
        if not re.match(r"^[a-zA-Z]+://", cleaned): cleaned = "https://" + cleaned
        qurl = QUrl.fromUserInput(cleaned)
        if qurl.isValid(): webview.load(qurl)
        else:
            search_url = QUrl("https://www.google.com/search")
            search_url.setQuery(url)
            webview.load(search_url)

    def update_tab_title(self, webview, title):
        index = self.tab_widget.indexOf(webview.parent())
        if index != -1: self.tab_widget.setTabText(index, title[:25])

    def handle_download(self, item):
        path, _ = QFileDialog.getSaveFileName(self, "Simpan File", item.suggestedFileName())
        if path:
            item.setDownloadDirectory(os.path.dirname(path))
            item.setDownloadFileName(os.path.basename(path))
            
            item_widget = self.download_panel.add_download(id(item), os.path.basename(path))
            self.downloads[id(item)] = item_widget
            self.showBubble(f"🧿 Unduhan dimulai ➜ {os.path.basename(path)}")
            self.progress_bar.setVisible(True)

            item.stateChanged.connect(lambda state: self.on_download_state_changed(item, state))
            item.accept()
        else:
            item.cancel()
            self.showBubble("❌ Unduhan dibatalkan.")
    
    def on_download_state_changed(self, item, state):
        received = item.receivedBytes()
        total = item.totalBytes()
        filename = item.downloadFileName()
        progress = int((received / total) * 100) if total > 0 else 0
        
        state_map = {
            QWebEngineDownloadRequest.DownloadState.DownloadInProgress: "🔄 Mengunduh",
            QWebEngineDownloadRequest.DownloadState.DownloadCompleted: "✅ Selesai",
            QWebEngineDownloadRequest.DownloadState.DownloadCancelled: "🚫 Dibatalkan",
            QWebEngineDownloadRequest.DownloadState.DownloadInterrupted: "⚠️ Gagal",
        }
        status_text = state_map.get(state, "❔ Status Tidak Dikenal")

        if state == QWebEngineDownloadRequest.DownloadState.DownloadInProgress:
            self.progress_bar.setValue(progress)
            self.download_panel.update_download(id(item), progress, status_text, filename)
        else:
            self.download_panel.finish_download(id(item), status_text, filename)
            self.showBubble(f"{status_text} - {filename}")
            self.progress_bar.setVisible(False)
            if id(item) in self.downloads: del self.downloads[id(item)]
            try:
                item.stateChanged.disconnect()
            except TypeError:
                pass 

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            # --- PERUBAHAN DIMULAI: Logika pembersihan sebelum menutup tab ---
            widget = self.tab_widget.widget(index)
            if widget:
                webview = widget.findChild(QWebEngineView)
                if webview:
                    webview.stop() # Hentikan media (video/audio)
                    webview.setPage(None) # Lepaskan halaman
                self.tab_widget.removeTab(index)
                widget.deleteLater() # Jadwalkan penghapusan widget dan semua turunannya
            # --- PERUBAHAN SELESAI ---
        else:
            self.showBubble("🚫 Tidak bisa menutup tab terakhir. Tutup jendela sebagai gantinya.")

    def showBubble(self, text):
        bubble = QLabel(text, self)
        bubble.setStyleSheet("background-color: #2E2E2E; color: #00FF00; border: 1px solid #00FF00; border-radius: 8px; padding: 8px; font-family: Consolas, monospace; font-size: 10pt;")
        bubble.setWindowFlags(Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        bubble.adjustSize()
        pos = self.mapToGlobal(self.rect().bottomRight())
        bubble.move(pos.x() - bubble.width() - 15, pos.y() - bubble.height() - 15)
        bubble.show()
        QTimer.singleShot(4000, bubble.close)

    def handle_link_hovered(self, url):
        self.setToolTip(url)    

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
        super().keyPressEvent(event)    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # --- PERUBAHAN DIMULAI: Logika untuk manajemen multi-jendela ---
    windows = []

    def create_new_window():
        window = ShrineWebTab(window_factory=create_new_window)
        window.setWindowTitle("Shrine Browser Lite")
        window.resize(1200, 720)
        
        icon_path = "browser.ico"
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, icon_path)
        if os.path.exists(icon_path):
            window.setWindowIcon(QIcon(icon_path))
        
        window.show()
        windows.append(window)
        window.windowClosed.connect(lambda w: windows.remove(w))
        return window

    create_new_window()
    # --- PERUBAHAN SELESAI ---

    sys.exit(app.exec())