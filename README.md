Shrine Browser Lite

Enterprise‑Grade Hybrid Web Browser
Built with a multi‑engine architecture that prioritizes performance, privacy, and extensibility.


---

Overview

Shrine Browser Lite is a modern, lightweight, and highly extensible web browser designed with an enterprise‑oriented hybrid architecture. It combines native Python performance with web technologies through a secure JavaScript–Python bridge, enabling features rarely found in conventional Chromium‑based browsers.

The project focuses on technical clarity, transparency, and real engineering value — not gimmicks.


---
Screenshot
<img width="1365" height="767" alt="Cuplikan layar 2026-01-09 231827" src="https://github.com/user-attachments/assets/56092e67-f341-4e89-8ee3-f1fdae209bf1" />
<img width="1365" height="767" alt="Cuplikan layar 2026-01-09 231903" src="https://github.com/user-attachments/assets/5e7bf0f8-d598-4f5f-b06d-ff5e7aed06c5" />
<img width="1365" height="767" alt="Screenshot 2026-01-17 152609" src="https://github.com/user-attachments/assets/9ec3df44-8713-4e13-9977-1e825252d63a" />





---

Changelog
🔹 Shrine Browser Lite v15.5.5

🚀 New Features

- PWA Manager & Application Suite
  - PWA Inventory: Introduced a centralized management interface to view and organize all installed Progressive Web Apps (PWAs).
  - Cache Management: Added granular controls for PWA data, including "Clear Cache" for specific applications to free up storage.
  - Life-cycle Controls: Integrated "Refresh" and "Reset/Delete" functionalities to troubleshoot and manage individual web app instances.
  - Instance Isolation: Improved reliability when launching PWAs in standalone windows.

- Secure DNS (DNS-over-HTTPS)
  - Privacy-First Networking: Implemented support for DoH (DNS-over-HTTPS) to encrypt DNS queries and prevent ISP tracking/hijacking.
  - Multi-Provider Integration: Included a comprehensive list of pre-configured secure providers:
    - Google Public DNS, Cloudflare (Standard, Security, Family), Quad9, AdGuard (Ad-blocking), and OpenDNS.
  - System Default Toggle: Seamlessly switch between the local system DNS and encrypted remote resolvers.

- Enhanced Proxy & VPN Module (macan_vpn)
  - Geo-Location Tunneling: Added a built-in Proxy/VPN manager supporting HTTP, SOCKS4, and SOCKS5 protocols.
  - Tor Network Support: Dedicated preset for local Tor routing (127.0.0.1:9050) for maximum anonymity.
  - Custom Proxy Configuration: New UI dialog allowing users to input custom proxy server credentials and addresses manually.
  - Regional Presets: Pre-configured server slots for various regions (SG, US, ID, JP) for quick access.

🛠️ Improvements & Fixes

- Settings UI: Redesigned the "Settings" menu hierarchy to include new "Secure DNS" and "VPN & Proxy" submenus located conveniently below the User-Agent settings.
- Startup Logic: Optimized the Chromium Flag injector to handle network-layer configurations (DNS/Proxy) before the browser engine initializes.
- Global Config Persistence: Enhanced the shrine_browser_config.json handler to ensure network settings persist across different user profiles.

Technical Implementation Note:
To apply changes to DNS or VPN settings, a full application restart is required. This ensures the Chromium network stack correctly initializes the encrypted tunnels and proxy mappings at the engine level.



---

Key Architecture

Hybrid Engine (Core Technology)

Shrine Browser Lite operates on a Hybrid Engine model:

Native backend powered by Python + Qt WebEngine

JavaScript used as a controlled bridge layer

Bidirectional communication between JS and Python

Network‑level operations prioritized over DOM injection


This architecture allows advanced features without sacrificing performance or stability.


---

Core Features

Advanced Ad Blocking (Network‑Level)

Blocks ads at the request/network layer, not via JS injection

Prevents ads from loading at all (no placeholders, no DOM residue)

Resistant to common ad‑blocker detection techniques

Configurable domain list (JSON‑based)

Per‑site whitelist support

Real‑time blocking statistics


> Note: YouTube ads are intentionally excluded to avoid playback and account issues.




---

Hybrid Mode Capabilities

Hybrid Mode is a specialized execution environment inside Shrine Browser Lite.

Supported features:

Inspect Element (Hybrid Engine)

Print Preview (Hybrid Engine)

Secure JS ↔ Python bridge

History synchronization

Download synchronization

Fullscreen video support (Hybrid Engine)


These features were introduced gradually to ensure architectural stability.


---

AI Integration Suite

Shrine Browser Lite integrates multiple AI systems directly into the browser:

ChatGPT

Gemini

Microsoft Copilot

Macan AI Imaging (React + Gemini)


AI features are embedded as first‑class tools, not external extensions.


---

Privacy & Security

No forced telemetry

No behavioral tracking

Local‑first configuration files

Clear separation between UI, network, and engine layers

Designed to be auditable and modifiable



---

Performance Philosophy

Shrine Browser Lite follows a strict performance doctrine:

Avoid unnecessary DOM manipulation

Prefer network‑level interception

Background processing with non‑blocking caching

Minimal UI overhead

Explicit control over engine behavior


The result is a browser that feels fast, predictable, and stable, even under complex workloads.


---

Configuration

Most core behaviors are configurable via JSON files:

Adblock domain lists

Homepage settings

Feature toggles

Engine behavior flags


This design enables advanced users and enterprise environments to maintain full control.


---

Target Audience

Shrine Browser Lite is designed for:

Power users

Developers & researchers

Privacy‑focused users

Technical professionals

Experimental and enterprise environments


It is not designed as a mass‑market consumer browser.


---

Development Status

Actively developed

Rapid but controlled release cycle

Features are released only when stable

Architecture‑first, feature‑second approach


Frequent updates reflect iterative engineering, not instability.


---

Open Source

Shrine Browser Lite is developed under the Macan Angkasa ecosystem philosophy.

Community contributions are welcome

Architecture discussions are encouraged

Quality and technical depth are prioritized over quantity



---

Legal & Ethical Notes

The browser does not claim ownership of third‑party content

Streaming and media features respect upstream sources

Certain features (e.g., recording protected streams) are intentionally excluded



---

Credits

© 2026 – Macan Angkasa
