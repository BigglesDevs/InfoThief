
<div align="center">
    <img src="https://via.placeholder.com/800x200.png?text=InfoThief+-+Gather+Information+Like+A+Pro" alt="InfoThief Banner" width="100%" />
</div>

# **InfoThief - A Tool for Information Gathering 🕵️‍♂️**

[![Last Commit](https://img.shields.io/github/last-commit/BigglesDevs/InfoThief?style=flat-square)](https://github.com/BigglesDevs/InfoThief/commits)
[![GitHub stars](https://img.shields.io/github/stars/BigglesDevs/InfoThief.svg?style=for-the-badge&color=yellow)](https://github.com/BigglesDevs/InfoThief/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/BigglesDevs/InfoThief.svg?style=flat-square)](https://github.com/BigglesDevs/InfoThief/network)
[![GitHub issues](https://img.shields.io/github/issues/BigglesDevs/InfoThief.svg?style=flat-square)](https://github.com/BigglesDevs/InfoThief/issues)
![Language](https://img.shields.io/github/languages/top/BigglesDevs/InfoThief?style=flat-square)


Welcome to **InfoThief**! This tool enables gathering and analyzing information from multiple platforms in one place. It’s designed for intelligence enthusiasts and security analysts to aggregate information for research and analysis purposes.

## 🔥 Features
- **Multi-Platform Information Extraction**: Collect information across multiple applications and platforms.
- **Token Decryption**: Decrypts encrypted tokens for further use and analysis.
- **Custom Webhook Notifications**: Send data insights to a Discord channel through webhooks.
- **Compiles to EXE**: Generate standalone executable scripts.
- **Interactive ASCII Header**: Stylish ASCII art and interactive user interface.
- **Advanced Error Handling**: Comprehensive error catching for robust execution.

<details>
<summary>🔍 **Example #1: Screenshots & Previews**</summary>

### Preview Images:
1. **Home Menu**:  
   ![Home Menu](https://via.placeholder.com/400x300.png?text=Home+Menu+Preview)  
   This shows the main menu of InfoThief where users can select options like testing or creating a distributable script.

2. **Discord Webhook Preview**:  
   ![Discord Webhook Preview](https://via.placeholder.com/400x300.png?text=Discord+Webhook+Data+Preview)  
   Demonstrates the gathered information sent to a Discord webhook as an embed.

</details>

## 🚀 Getting Started

### Prerequisites
1. **Python 3.x** installed on your system.
2. **MongoDB** instance (for storing gathered data).
3. **PyInstaller** (for compiling scripts into EXE format).
4. **Colorama**, **pyfiglet**, **requests**, and other dependencies (listed in `requirements.txt`).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BigglesDevs/InfoThief.git
   cd InfoThief
   ```

2. **Create and Activate a Virtual Environment (venv)**:
   It is recommended to create a virtual environment to keep your project dependencies isolated. Follow these steps:

   ```bash
   python -m venv venv  # Create a virtual environment named 'venv'
   source venv/bin/activate  # Activate on macOS/Linux
   .\venv\Scripts\activate  # Activate on Windows
   ```

   Once activated, your terminal prompt will show `(venv)` to indicate that the virtual environment is active.

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB connection**: 
   Ensure that your MongoDB URI is correctly stored in the external configuration (e.g., fetched from Pastebin).

### Running the Script

To launch **InfoThief**, use the following command:

```bash
python main.py
```

## 🛠️ Usage

### Main Menu Options:
1. **Test InfoThief (On Self)**:
   - Gathers information from your own system and sends the data to a specified Discord webhook.
   - Displays and stores information in MongoDB.

2. **Create InfoThief (Distribute)**:
   - Allows you to create and distribute a personalized version of the script.
   - Customize the script with your webhook URL and optionally compile it into an executable.

3. **Exit**:
   - Exits the script.

## 🔒 Security Disclaimer
This tool is intended for **educational** and **research** purposes only. Unauthorized use of this tool against systems, devices, or accounts without permission is **illegal** and unethical. The creators and contributors are not responsible for any misuse or damage caused by the use of this tool.

## 📢 Important Notice
The creator of this project, **BigglesDevelopment**, is **not involved in or responsible for any actions or data gathered using this tool**. Any information sent or gathred using the tool is strictly the responsibility of the user.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support & Contributions
We welcome contributions! Feel free to fork this repository and submit a pull request. If you have any questions or need assistance, open an issue in the repository.

---

**InfoThief**: Made by [BigglesDevelopment❤️](https://github.com/BigglesDevs). 

Keep learning, stay secure! 😊
