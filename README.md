# 🔐 Educational Keylogger

A lightweight Python demonstration project for learning about keyboard event monitoring and system-level input capture. **This project is for educational purposes only.**

⚠️ **DISCLAIMER**: This tool is designed to teach cybersecurity concepts. Unauthorized use of keyloggers is illegal. Always obtain proper consent and follow applicable laws.

## 🎓 Purpose

This project demonstrates:
- How keyboard events are captured at the operating system level
- Event listener patterns in Python
- File I/O operations in real-time applications
- Special key handling and mapping

## ✨ Features

- **Real-time Keyboard Monitoring**: Captures all keyboard input events
- **Special Key Detection**: Distinguishes between regular keys and special keys (Enter, Tab, Backspace, etc.)
- **File Logging**: Writes captured input to a log file with proper encoding
- **Clean Termination**: Press ESC to safely stop the listener
- **Unicode Support**: Handles multi-byte characters correctly
- **Lightweight**: Minimal dependencies, efficient implementation

## 📦 Requirements

- Python 3.7+
- `pynput` library

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/zexhanamin/educational-keylogger.git
cd educational-keylogger
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install pynput
```

## 📖 Usage

### Basic Usage
```bash
python keylogger.py
```

### What It Does
1. Starts listening for keyboard events
2. Captures each keystroke and writes to `keylog.txt`
3. Special keys are mapped to readable format (e.g., `[ENTER]`, `[TAB]`)
4. Press **ESC** to stop the keylogger

### Example Output (keylog.txt)
```
Hello World[ENTER]
Testing[TAB]123[BACKSPACE][BACKSPACE][BACKSPACE]
[CTRL]C
```

## 🛡️ Educational Value

**Learn about:**
- System-level input monitoring
- Event-driven programming patterns
- Python's `pynput` library
- Cross-platform keyboard handling
- File operations and encoding

## ⚖️ Legal Disclaimer

**This software is provided for educational purposes only.** 

- Unauthorized monitoring of computer systems is **illegal** in most jurisdictions
- **Always obtain explicit written consent** before running this on any system
- The author(s) are **not responsible** for misuse of this software
- Use only in controlled environments you own or have permission to test

## 🤝 Contributing

To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add your feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

## 📚 Resources

- [pynput Documentation](https://pynput.readthedocs.io/)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Cybersecurity Learning Resources](https://www.cybrary.it/)

## ⚡ Quick Start Example

```python
from pynput import keyboard

def on_press(key):
    print(f'Key pressed: {key}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```

---

**Made with ❤️ for educational purposes**
