# 🌟 ASTRA Ethical Port Scanner (EPS v1.0) 🌟

Welcome to **ASTRA Ethical Port Scanner**, a powerful yet simple tool designed for ethical hacking and network security assessments. 🚀

## ⚡ Features
- **Fast and Multi-threaded:** Quickly scans a wide range of ports.
- **Customizable Scans:** Specify target IPs and port ranges.
- **Save Results:** Export your scan results to a file for further analysis.
- **User-Friendly Interface:** Simple and easy to use.

## 🔧 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/x3089/astra-port-scanner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd astra-port-scanner
   ```
3. Ensure you have Python 3 installed on your system.
4. Install required libraries (if any):
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the tool directly from the terminal:
```bash
python3 astra_scanner.py -t <target_ip_or_domain> -p <port_range> [-o output_file]
```
### Example:
```bash
python3 astra_scanner.py -t 192.168.1.1 -p 1-65535 -o results.txt
```

### Arguments:
- `-t`, `--target`: Specify the target IP or domain.
- `-p`, `--ports`: Define the range of ports to scan (default: `1-1024`).
- `-o`, `--output`: Save the scan results to a file (optional).

## ⚠️ Disclaimer
⚠️ **This tool is intended for ethical use only.** Ensure you have explicit permission before scanning any network. The author is not responsible for any misuse of this tool. Use responsibly! 🛡️

## 📜 License
This project is licensed under the [MIT License](LICENSE).

## ❤️ Contributing
We welcome contributions! Feel free to fork the repository and submit pull requests. 🌟

---

### Made with 🖤 by ASTRA

