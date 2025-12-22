# Gamepad Video Controller 🎮

Control media players and browsers using a gamepad.

![Demo](https://github.com/Samyc2002/gamepad-video-controller/blob/main/gamepad-video-controller-demo.gif)

Works with:
- VLC
- YouTube (Chrome / Firefox / Edge)
- Most desktop video players
- Any app that responds to keyboard shortcuts

---

## Features

### Media Controls
- Play / Pause
- Fullscreen toggle
- Seek forward / backward
- Volume up / down
- Mute / captions (player dependent)

### Browser & Window Controls
- Next / previous browser tab
- Reload current tab
- Switch between windows
- Scroll vertically and horizontally using the left joystick

### System Integration
- Runs in the background
- Windows system tray icon
- One-click enable / disable toggle
- Optional auto-start on Windows login

---

## Requirements

- Windows
- Python 3.9+
- Xbox / XInput-compatible controller (other controllers may work but are untested)

---

## Installation

```bash
pip install gamepad-video-controller
gamepad-video-controller
```

Once running, the app will appear in the Windows system tray.

Focus your media player or browser window and use the controller.

---

## Usage Notes

- Button and axis mappings may vary by controller and driver
- Tested primarily with Xbox controllers on Windows
- DRM-heavy apps may limit some controls
- No custom configuration UI yet (planned)

---

## Autostart

You can enable Start with Windows directly from the system tray menu.
This uses the standard Windows per-user startup registry and does not require admin privileges.

---

## License

[MIT](./LICENSE)
