import tempfile
import subprocess
import os

from playwright.sync_api import sync_playwright


executable_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" # Change this
extension_path = f"{os.getcwd()}/Return-Youtube-Dislike"
temp_user_data_dir = tempfile.mkdtemp()

cdp_port = "9222"
flags = [f"--disable-extensions-except={extension_path}", f"--load-extension={extension_path}"]
subprocess.Popen([executable_path, f"--remote-debugging-port={cdp_port}", f"--user-data-dir={temp_user_data_dir}", *flags])

playwright = sync_playwright().start()
main_browser = playwright.chromium.connect_over_cdp(f"http://localhost:{cdp_port}")

page = main_browser.new_page()
page.goto("https://www.youtube.com/watch?v=YbJOTdZBX1g")
# Extension doesnt load/work on this New Page
# Note if you go to this link on the original browser window the extension works.
page.wait_for_timeout(10000)