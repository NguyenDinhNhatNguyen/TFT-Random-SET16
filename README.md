# TFT Randomizer - Destiny Trait Generator

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

**TFT Randomizer SET 16** is a simple yet fun Command Line Interface (CLI) tool for **Teamfight Tactics** players. If you don't know what composition to force today, or if you want to challenge yourself with a random Origin/Class, let this tool decide your destiny!

## ✨ Features

* 🎲 **Random Selection:** Randomly picks between Origins and Classes from the game.
* ⚡ **Visual Effects:** Includes a "spinning" text animation to build suspense before revealing the result.
* 🔁 **Continuous Play:** Allows you to re-roll multiple times without restarting the program.
* 💻 **Cross-Platform:** Runs smoothly on Windows, macOS, and Linux.

## 🗂 Current Data

The tool currently contains data for **Set 16 (Runeterra Reforged)**, featuring traits such as:
* *Origins:* Noxus, Demacia, Piltover, Bilgewater, Ixtal, etc.
* *Classes:* Sorcerer, Bruiser, Bastion, Gunner, etc.

*(You can easily update this list in the `main.py` file to match the latest TFT Set).*

## 🚀 Installation & Usage

There are two ways to use this tool:

### Method 1: Run the EXE file directly (For Standard Users)
No Python installation required.
1.  Download the `TFT-Random.exe` file.
2.  Double-click to run it.
3.  Press **Enter** to start spinning!

### Method 2: Run from Source Code (For Developers)
Requires [Python](https://www.python.org/) installed on your machine.

1.  Clone this repository or download the source code.
2.  Open your terminal/command prompt in the folder containing the file.
3.  Run the command:
    ```bash
    python main.py
    ```

## 🛠 Build Instructions (Packaging)

This project includes a `TFT-Random.spec` configuration file. If you modify the code and want to repackage it into an `.exe` file, follow these steps:

1.  Install **PyInstaller**:
    ```bash
    pip install pyinstaller
    ```
2.  Run the build command using the provided spec file:
    ```bash
    pyinstaller TFT-Random.spec
    ```
3.  The new `.exe` file will be generated in the `dist/` folder.

## 📝 Project Structure

```text
TFT-Random/
├── main.py            # Main source code
├── dist
│   └── TFT-Random.exe # Executable file (compiled)
├── TFT-Random.spec    # PyInstaller configuration file
└── .gitignore         # Git configuration
```

## 🤝 Customization
To update the traits for a new season (e.g., Set 10, 11, etc.), simply open main.py and edit the traits list:
```
traits = [
    "New Origin A",
    "New Class B",
    ...
]
```
May the RNG gods be ever in your favor! 🎲

## 👤 Author
Nguyen Dinh Nhat Nguyen - Computer Engineering Student @ UIT-VNUHCM
