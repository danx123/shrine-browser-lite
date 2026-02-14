Shrine Browser Lite

Enterprise‑Grade Hybrid Web Browser
Built with a multi‑engine architecture that prioritizes performance, privacy, and extensibility.


---

Overview

Shrine Browser Lite is a modern, lightweight, and highly extensible web browser designed with an enterprise‑oriented hybrid architecture. It combines native Python performance with web technologies through a secure JavaScript–Python bridge, enabling features rarely found in conventional Chromium‑based browsers.

The project focuses on technical clarity, transparency, and real engineering value — not gimmicks.


---
Screenshot
<img width="1365" height="767" alt="Screenshot 2026-02-05 024944" src="https://github.com/user-attachments/assets/b00d066c-7850-4fba-a49f-ddb600aa07f6" />
<img width="1365" height="767" alt="Screenshot 2026-02-05 024703" src="https://github.com/user-attachments/assets/446af138-83d4-4cb6-b0ea-3c0f3b95e19e" />
<img width="1002" height="486" alt="Screenshot 2026-02-14 135237" src="https://github.com/user-attachments/assets/31fc8955-5615-468f-959b-7f626866f4a0" />




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
