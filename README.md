
# Clipboard Logger (Python)

A lightweight clipboard monitoring tool for **Linux**, written in Python. It captures copied **text** and **file paths**, stores metadata like file size and timestamps, and logs all entries into a temporary RAM-based file at `/dev/shm/clipboard_log.txt`.

---

## ✨ Features

- 📝 Logs copied **text** and **file paths**
- 📁 For file paths, captures:
  - File name
  - Absolute path
  - Size
  - Creation & modification timestamps
- 🚀 Stores logs in **RAM** (`/dev/shm`) — auto-cleared on reboot
- 📂 Opens the log file in a Linux GUI text editor (`mousepad` by default)
- 🔄 Maintains **incremental log indexing**
- 🧠 No dependencies beyond Python + shell commands

---

## 📦 Requirements

| Tool          | Description                          | Install Command                    |
|---------------|--------------------------------------|------------------------------------|
| `python3`     | Python 3 interpreter                 | pre-installed on most distros      |
| `pip3`        | Python package manager               | `sudo apt install python3-pip`     |
| `pyperclip`   | Clipboard access in Python           | `pip3 install --user pyperclip`    |
| `mousepad`    | Default text editor (can be changed) | `sudo apt install mousepad`        |
| `tail/grep/awk` | Shell commands for indexing        | usually pre-installed on Linux     |

---

## 📁 Project Structure

```
clipboard-logger/
├── clipboard_logger.py     # Main logger script
├── install.sh              # One-step Linux installer
└── README.md               # Project documentation
```

---

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/samanr333/clipboard-logger.git
cd clipboard-logger
```

### Step 2: Install Dependencies

```bash
pip3 install --user pyperclip
sudo apt install mousepad
```

### Step 3: Run the Logger

```bash
python3 clipboard_logger.py
```

> The logger will automatically open the log file in `mousepad`.

---

## 🛠 Automated Installer

You can use the provided script to install everything:

```bash
chmod +x install.sh
./install.sh
```

What it does:

- Installs `pip3` if missing
- Installs `pyperclip` and `mousepad`
- Makes the logger executable
- Optionally runs the logger

---

## 📍 Where Logs Are Stored

Logs are saved to:

```
/dev/shm/clipboard_log.txt
```

> 🧠 `/dev/shm` is a **RAM-based directory**, so logs disappear after reboot.

---

## 📑 Sample Log Output

```
============================================================
Entry No: 7
Timestamp: 2025-05-10 14:22:53
Copied Text: sudo apt update && sudo apt upgrade

============================================================
Entry No: 8
Timestamp: 2025-05-10 14:30:01
Name: document.pdf
Location: /home/user/Documents/document.pdf
Size: 18432 bytes
Created: Sat May 10 14:15:02 2025
Modified: Sat May 10 14:20:33 2025
```

---

## 🛑 To Stop the Script

Use:

```
Ctrl + C
```

---

## 📝 Make Logs Persistent (Optional)

To keep logs after reboot, edit this line in the Python script:

```python
LOG_FILE = "/dev/shm/clipboard_log.txt"
```

Replace with a permanent path:

```python
LOG_FILE = "/home/yourname/clipboard_log.txt"
```

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

Created with ❤️ for Linux users and devs.
