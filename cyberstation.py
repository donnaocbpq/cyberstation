import subprocess
import os
import sys
import shutil

class CyberStation:
    def __init__(self, browser_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"):
        self.browser_path = browser_path
        self.sandbox_dir = "C:\\CyberStationSandbox"
        self.setup_sandbox()

    def setup_sandbox(self):
        # Create a directory to act as a sandbox
        if not os.path.exists(self.sandbox_dir):
            os.makedirs(self.sandbox_dir)
        print(f"Sandbox environment set up at: {self.sandbox_dir}")

    def launch_browser(self):
        # Launch the browser in a restricted environment
        try:
            subprocess.run(
                ["sandboxie", "/box:CyberStation", "/silent", self.browser_path],
                check=True
            )
            print("Browser launched in a secure browsing environment.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to launch browser in sandbox: {e}")

    def clear_sandbox(self):
        # Clear the sandbox directory
        try:
            shutil.rmtree(self.sandbox_dir)
            os.makedirs(self.sandbox_dir)
            print("Sandbox environment cleared.")
        except Exception as e:
            print(f"Error clearing sandbox: {e}")

    def run(self):
        print("Starting CyberStation...")
        self.launch_browser()

if __name__ == "__main__":
    cyber_station = CyberStation()
    cyber_station.run()