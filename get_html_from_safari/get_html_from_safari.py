"""Main module."""
import subprocess
import os,time
import sys
import validators
from urllib.parse import urlparse

class InvalidURLException(Exception):
    default_message = "Invalid URL"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)

class SafariIsNotRunning(Exception):
    default_message = "Safari is not running"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)

# Get the article html
def get_html(url=None):
    if url:
        if run_as('safari_is_running') != 'true' or run_as('safari_window_exists') != 'true':
            run_as('safari_activate')
            time.sleep(1)

        if not url.startswith(('http://', 'https://')):
            url = f'http://{url}'

        if not validators.url(url):
            raise InvalidURLException()

        script_file = 'fetch_html'
        result = run_as(script_file, [url])
    else:
        if run_as('safari_is_running') != 'true' or run_as('safari_window_exists') != 'true':
            raise SafariIsNotRunning()

        script_file = 'safari_grab_source'
        result = run_as(script_file)

    return result

def run_as(script_name, args=[]):
    script_name = script_name + '.scpt'
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "applescripts")
    script_path = os.path.join(script_dir, script_name)
    result = subprocess.run(['osascript', script_path, *args], capture_output=True, text=True)
    return result.stdout.strip()