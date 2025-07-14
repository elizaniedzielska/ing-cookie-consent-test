import os
from playwright.sync_api import devices

config = {
    "timeout": 60000,
    "retries": 0,
    "use": {
        "headless": True,
        "viewport": {"width": 1280, "height": 720},
    }
}