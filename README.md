# CyberStation

CyberStation is a Python program designed to offer a secure browsing environment by isolating internet activities from the rest of the Windows system. By launching your browser in a sandboxed environment, CyberStation helps protect your system from potential threats encountered during web browsing.

## Features

- **Sandboxed Browsing**: Launches the web browser in a sandbox to isolate it from the main system.
- **Easy Setup**: Automatically sets up and clears the sandbox environment.
- **Customizable**: Allows specification of the browser to be used.

## Requirements

- A Windows operating system
- Python 3.x
- Sandboxie (a third-party sandboxing tool)
- A web browser (default is Mozilla Firefox)

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install Sandboxie from its [official website](https://sandboxie-plus.com/).
3. Clone the repository or download `cyberstation.py`.

## Usage

1. Open a command prompt.
2. Navigate to the directory containing `cyberstation.py`.
3. Run the script using Python:

   ```bash
   python cyberstation.py
   ```

   By default, the program will attempt to launch Mozilla Firefox in a sandboxed environment. Ensure Sandboxie is installed and properly configured on your system.

## Customization

To change the browser, edit the `browser_path` in the `CyberStation` class initialization:

```python
cyber_station = CyberStation(browser_path="C:\\Path\\To\\Your\\Browser.exe")
```

## Disclaimer

CyberStation relies on Sandboxie, a third-party tool, to provide sandboxing functionality. Ensure that Sandboxie is correctly installed and configured to meet your security needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.