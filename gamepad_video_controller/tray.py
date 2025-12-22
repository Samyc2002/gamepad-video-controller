from pystray import Icon, Menu, MenuItem
from PIL import Image
from importlib import resources
from gamepad_video_controller import autostart

# Shared state (imported by main)
enabled = True


def create_icon():
    """Create a simple tray icon dynamically."""
    with (
        resources.files("gamepad_video_controller.assets")
        .joinpath("icon.png")
        .open("rb") as f
    ):
        return Image.open(f).convert("RGBA")


def toggle_enabled(icon, item):
    global enabled
    enabled = not enabled
    icon.update_menu()
    print(f"Gamepad Video Controller {'enabled' if enabled else 'disabled'}")


def quit_app(icon, item):
    icon.stop()
    raise SystemExit


def toggle_autostart(icon, item):
    if autostart.is_autostart_enabled():
        autostart.disable_autostart()
    else:
        autostart.enable_autostart()
    icon.update_menu()


def build_menu():
    return Menu(
        MenuItem(
            lambda item: "Enabled ✓" if enabled else "Disabled ✗",
            toggle_enabled,
        ),
        MenuItem(
            lambda item: "Start with Windows ✓"
            if autostart.is_autostart_enabled()
            else "Start with Windows ✗",
            toggle_autostart,
        ),
        Menu.SEPARATOR,
        MenuItem("Quit", quit_app),
    )


def run_tray():
    icon = Icon(
        "Gamepad Video Controller",
        create_icon(),
        "Gamepad Video Controller",
        menu=build_menu(),
    )
    icon.run()
