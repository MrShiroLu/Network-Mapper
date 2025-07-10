# NetworkMapper

NetworkMapper is a command-line-based network port scanner built with Python. It uses the `python-nmap` library to scan specific ports on a given target and retrieve information such as state, service name, and version.

## Features

- CLI-based port scanning
- Displays open ports, service names, and versions
- Custom port selection via command-line arguments

## Requirements

- Python 3.8 or higher
- Nmap installed on the system
- Required Python packages:
  - `python-nmap`
  - `pyfiglet`

### Installing Dependencies

First, make sure Nmap is installed on your system:

- Debian/Ubuntu:
  ```bash
  sudo apt install nmap
```

* macOS:

  ```bash
  brew install nmap
  ```
* Windows:
  Download and install from [https://nmap.org/download.html](https://nmap.org/download.html)

---

## Usage

```bash
python main.py [target] -p [ports]
```

### Examples

Scan a range of ports:

```bash
python main.py 192.168.1.1 -p 1-1000
```

Scan specific ports:

```bash
python main.py example.com -p 22,80,443
```

## Project Structure

```
.
├── main.py           # Entry point script
├── greeting.py       # Contains banner and usage text
├── scanner.py        # Handles port scanning logic
├── requirements.txt  # Python dependencies
└── __pycache__/      # Ignored compiled Python files
```

## Notes

* `__pycache__/` and `.pyc` files should be excluded from version control using a `.gitignore` file.
* Future versions may include a web-based or graphical frontend.



## To-Do

- [x] Backend 
- [ ] GUI