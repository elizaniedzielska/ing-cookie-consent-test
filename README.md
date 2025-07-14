# ING Cookie Consent Test (Playwright + Pytest)

This project contains an automated test that verifies if the correct analytics cookies are stored after accepting only the analytics option in ING's cookie consent banner.

The test is written in Python using Playwright and Pytest. It also includes a bonus feature: running the test across multiple browser engines (Chromium, Firefox, WebKit).

---

## How to run

1. Clone the repo:

    ```bash
    git clone <your-repo-url>
    cd <your-project-folder>
    ```

2. (Optional but recommended) Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # on Linux/macOS
    venv\Scripts\activate     # on Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Playwright browsers:

    ```bash
    python -m playwright install
    ```

5. Run the test:

    ```bash
    pytest test_cookie_consent.py
    ```

---

## What does the test do?

- Opens https://www.ing.pl  
- Clicks “Dostosuj” (Customize) on the cookie banner  
- Selects only the analytics cookies  
- Clicks “Zaakceptuj wybrane” (Accept selected)  
- Waits for the page to set cookies  
- Reloads the page to ensure cookies are stored  
- Checks for analytics-related cookies (e.g. `_ga`, `_gid`, etc.)

---

## Bonus: Multi-browser support

The test runs sequentially in:

- Chromium  
- Firefox  
- WebKit

This verifies that behavior is consistent across major engines.

---

## Files included

- `test_cookie_consent.py` – main test file  
- `requirements.txt` – required Python packages  
- `README.md` – this file

---

## Requirements

- Python 3.7 or newer  
- Linux, macOS, or Windows  
- Internet access (to load the ING website)

---

## Notes

- ING’s website sets cookies via JavaScript and tag managers, so the test includes a short wait and page reload before checking cookies.
- If needed, set `headless=False` in the test script to see the browser during execution.

---

## Contact

If you have any questions, feel free to reach out via email or GitHub.