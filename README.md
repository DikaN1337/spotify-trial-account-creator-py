# spotify-trial-account-creator-py
Spotify Trial Account Generator using Selenium and the Chromium Webdriver with Python

**Installation:**
1. Download the master branch.
2. Install **Python 3.7.X** or superior version.
3. Run `pip install colorama` & `pip install selenium`.
4. Download the **Chromium Webdriver** that **matches** your **Google Chrome** version.
5. Put it at `C:/webdrivers/chromedriver.exe` with that **exact name**.
4. Change `password.txt` and insert the **Password** for all the accounts.
5. Change `validade.txt` and insert the **Date of Expiry** for all VCC's.
6. Change `email.txt` and insert **1 Random Email** per line for the accounts.
7. Change `cc.txt` and insert **1 Card Number** per line for the accounts.
8. Change `cvv.txt` and insert **1 CVV** (**must match with the card number**) per line for the accounts.
9. Run `python3 spotify.py`.

**Usage:**
1. After running the script, insert the **number of accounts** to generate (**must match with the number of Emails and VCC's inserted in the files above**).
2. Wait until it creates all the accounts and it's done.
