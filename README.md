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
<img width="1365" height="767" alt="Cuplikan layar 2026-01-09 231927" src="https://github.com/user-attachments/assets/b583d049-70c6-4711-8119-ae031cb35e42" />




---

Changelog
🔹 Shrine Browser Lite v15.5.0

🚀 New Features
- Integrated PWA App Mode Launcher Introduced a new "App Mode" module that allows users to launch web applications in a dedicated, standalone window. This feature utilizes the local system's Microsoft Edge (WebView2) or Google Chrome engine to provide a native-app experience, complete with its own window frame and taskbar icon.

- Desktop Shortcut Creation Users can now create native Windows Desktop Shortcuts for any website. These shortcuts are configured to bypass the main browser interface and launch directly into App Mode.

- Automated Icon Engine Implemented an intelligent icon processing system that fetches high-resolution favicons via API and automatically converts them into Windows-compatible .ico format for desktop shortcuts.

- Smart PWA Detection The URL bar now features a dynamic detection engine. It automatically identifies "PWA-Ready" sites (such as YouTube, WhatsApp, Discord, ChatGPT, etc.) and presents a quick-action button for immediate installation/launch.

🛠️ Technical Improvements
- Session Isolation (Sandbox) Each PWA launched through the App Mode utilizes a dedicated user-data-dir within the Shrine Profile directory. This ensures that logins and cookies in App Mode remain separate from the main browser session and other apps.

- VBScript Bridge Implementation Developed a lightweight VBScript-based shortcut generator to ensure .lnk file creation works seamlessly on all Windows environments without requiring heavy external Python dependencies like pywin32.

- Enhanced Fallback Logic Added an intelligent browser locator that automatically detects the most stable engine (Edge or Chrome) available on the host machine to handle App Mode requests.



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
