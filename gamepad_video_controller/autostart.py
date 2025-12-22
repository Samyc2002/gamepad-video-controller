import sys
import winreg

APP_NAME = "GamepadVideoController"
RUN_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"


def get_executable_command():
    """
    Returns the command Windows should run on startup.
    Works for:
    - pip-installed CLI
    - packaged exe later
    """
    if getattr(sys, "frozen", False):
        # EXE (PyInstaller etc.)
        return sys.executable
    else:
        # pip / uv installed CLI
        return f'"{sys.executable}" -m gamepad_video_controller.main'


def enable_autostart():
    command = get_executable_command()
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, RUN_KEY, 0, winreg.KEY_SET_VALUE
    ) as key:
        winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, command)


def disable_autostart():
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, RUN_KEY, 0, winreg.KEY_SET_VALUE
        ) as key:
            winreg.DeleteValue(key, APP_NAME)
    except FileNotFoundError:
        pass


def is_autostart_enabled():
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, RUN_KEY, 0, winreg.KEY_READ
        ) as key:
            winreg.QueryValueEx(key, APP_NAME)
            return True
    except FileNotFoundError:
        return False
