# 🚀 Generate Google Drive token.pickle, Client ID, Client Secret & Refresh Token on macOS

This guide explains how to generate a valid **Google OAuth 2.0 token (`token.pickle`)** and extract:

- ✅ Client ID
- ✅ Client Secret
- ✅ Refresh Token

using **macOS Terminal**.

These credentials can be used for:

- Cloudflare SecretX Index
- Google Drive OAuth scripts
- Google Drive API automation
- Other Google API projects

---

## 🔗 Links

- Google Cloud Console
  https://console.cloud.google.com

- OAuth 2.0 Playground
  https://developers.google.com/oauthplayground

- Token-Pickle Repository
  https://github.com/GK-BOTZ/Token-Pickle

---

# 🔐 Token Generator for Google OAuth (`token.pickle`)

This tool generates a `token.pickle` file from your Google OAuth `credentials.json`.

The generated token can then be used by applications that authenticate with Google APIs.

---

# 🚀 Setup Instructions

## 1. Open Terminal

macOS already includes a Unix-style terminal environment, so you do **not** need WSL.

Open:

**Applications → Utilities → Terminal**

You can also press:

```text
Command + Space
```

and search for:

```text
Terminal
```

---

## 2. Install Homebrew

Homebrew is the package manager commonly used on macOS.

Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the instructions shown by the installer.

After installation, verify it:

```bash
brew --version
```

If `brew` is not found, Homebrew will normally provide the command required to add it to your shell `PATH`. Run that command and restart Terminal.

---

## 3. Install Python and Git

Run:

```bash
brew install python git
```

Check the installations:

```bash
python3 --version
```

```bash
git --version
```

---

## 4. Install Google OAuth Libraries

Run:

```bash
python3 -m pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

If macOS reports an externally managed Python environment, create a virtual environment instead:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Then install the libraries:

```bash
python3 -m pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

---

# 📦 5. Clone the Repository

Clone the Token-Pickle repository:

```bash
git clone https://github.com/GK-BOTZ/Token-Pickle.git
```

Enter the repository:

```bash
cd Token-Pickle
```

Verify the files:

```bash
ls
```

---

# 🔑 6. Create Google OAuth Credentials

Open Google Cloud Console:

https://console.cloud.google.com

Create or select your Google Cloud project.

Then:

1. Open **APIs & Services**.
2. Enable the API required by your project, such as **Google Drive API**.
3. Open **OAuth consent screen**.
4. Configure the OAuth consent screen.
5. Add your Google account as a test user if the application is in testing mode.
6. Open **Credentials**.
7. Create an **OAuth 2.0 Client ID**.
8. Select the appropriate application type required by the generator.
9. Download the JSON credentials file.

Rename the downloaded file to:

```text
credentials.json
```

---

# 📁 7. Put `credentials.json` in the Repository

Your directory should look similar to:

```text
Token-Pickle/
├── credentials.json
├── generate.py
├── test_token_pickle.py
└── extract_token_pickle.py
```

You can move the file from your Downloads directory with:

```bash
mv ~/Downloads/credentials.json .
```

Verify:

```bash
ls
```

---

# 🔐 8. Generate `token.pickle`

Run:

```bash
python3 generate.py
```

The script will display an authentication URL.

Copy the URL from Terminal and open it in your browser.

Sign in with the Google account that should have access to the requested API.

Review and allow the requested permissions.

After successful authentication, Google will display:

```text
The authentication flow has completed. You may close this window.
```

Return to Terminal.

The script should save:

```text
token.pickle
```

inside the repository directory.

---

# 📁 9. Verify `token.pickle`

Run:

```bash
ls -lh token.pickle
```

You should see the generated file.

Your directory should now look similar to:

```text
Token-Pickle/
├── credentials.json
├── token.pickle
├── generate.py
├── test_token_pickle.py
└── extract_token_pickle.py
```

---

# 🧪 10. Test `token.pickle`

Run:

```bash
python3 test_token_pickle.py
```

If the token is valid, the script should successfully authenticate using the generated credentials.

---

# 🔍 11. Extract Information From `token.pickle`

Run:

```bash
python3 extract_token_pickle.py
```

This can be used to extract information such as:

- Client ID
- Client Secret
- Refresh Token
- Token information

The exact output depends on the implementation of the script.

---

# 🧾 12. View Raw `token.pickle` Data

Run:

```bash
python3 -c "import pickle; from pprint import pprint; pprint(vars(pickle.load(open('token.pickle', 'rb'))))"
```

This prints the attributes stored in the credential object.

---

# 🌐 13. Download `token.pickle` From Your Mac

If you need to transfer the generated file to another device, you can temporarily start a local HTTP server.

Run:

```bash
python3 -m http.server 8080
```

The server will normally be available at:

```text
http://localhost:8080
```

Open that address in a browser on the Mac.

You should see the files in the current directory.

Download:

```text
token.pickle
```

Stop the server when finished by pressing:

```text
Ctrl + C
```

---

# 📱 14. Access the Server From Another Device

If another device is connected to the same local network, first find your Mac's local IP:

```bash
ipconfig getifaddr en0
```

If that returns nothing, try:

```bash
ipconfig getifaddr en1
```

Then on the other device open:

```text
http://YOUR_MAC_IP:8080
```

For example:

```text
http://192.168.1.20:8080
```

Your Mac's firewall or network configuration may prevent access from another device.

Only run the HTTP server when you actually need it, because it exposes files from the current directory to devices that can reach the server.

---

# 🧹 15. Deactivate the Virtual Environment

If you created `.venv`, deactivate it when finished:

```bash
deactivate
```

---

# 🔄 16. Using the Token Later

When your Google API application requires authentication, place the generated:

```text
token.pickle
```

where your application expects it.

The exact location depends on the application.

Do not regenerate the token unnecessarily. OAuth refresh tokens can remain usable until revoked, invalidated, or otherwise made unavailable by Google's authentication policies or the application's configuration.

---

# 🔐 Security Warning

Treat these files as sensitive credentials:

```text
credentials.json
token.pickle
```

A refresh token can allow an application to obtain access tokens for the authorized Google account and requested scopes.

**Do not:**

- Upload `credentials.json` to GitHub.
- Upload `token.pickle` to a public repository.
- Send credentials to untrusted people.
- Put credentials directly into source code.
- Post credentials in screenshots or logs.

Add them to `.gitignore`:

```bash
printf "credentials.json\ntoken.pickle\n.venv/\n" >> .gitignore
```

---

# 🛑 If You Accidentally Expose Your Credentials

If a credential has been publicly exposed, revoke or rotate the affected credential through Google Cloud Console and your Google account's security settings as appropriate.

Then generate new credentials if required.

---

# 🧰 Troubleshooting

## `brew: command not found`

Homebrew is either not installed or its shell configuration has not been loaded.

Run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then follow the shell configuration command shown by Homebrew.

---

## `python3: command not found`

Install Python:

```bash
brew install python
```

Then verify:

```bash
python3 --version
```

---

## `git: command not found`

Install Git:

```bash
brew install git
```

Then verify:

```bash
git --version
```

---

## `pip` Installation Error

Use:

```bash
python3 -m pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

If macOS blocks system-wide package installation, use a virtual environment:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
python3 -m pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

---

## `credentials.json` Not Found

Check the current directory:

```bash
pwd
```

Then:

```bash
ls
```

Make sure the file is named exactly:

```text
credentials.json
```

If it is in Downloads:

```bash
mv ~/Downloads/credentials.json .
```

---

## `token.pickle` Not Found

Run:

```bash
ls -lh
```

If the file was not generated, run:

```bash
python3 generate.py
```

again and complete the Google authentication flow.

---

## OAuth Error During Login

Check:

- The correct Google Cloud project is selected.
- The required Google API is enabled.
- The OAuth consent screen is configured.
- Your Google account is added as a test user when required.
- The OAuth client credentials match the application.
- `credentials.json` is the correct downloaded file.

---

# 🖥️ macOS vs WSL

You do **not** need WSL on macOS.

The equivalent environments are:

```text
Windows
└── WSL → Ubuntu → apt

macOS
└── Terminal → Homebrew → brew

Android
└── Termux → pkg
```

The Google OAuth commands are mostly the same once Python and the required libraries are installed.

The main difference is package management:

### macOS

```bash
brew install python git
```

### Ubuntu / WSL

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
```

---

# ✅ Done

You have now:

1. Installed Python and Git on macOS.
2. Installed the required Google OAuth libraries.
3. Downloaded the Token-Pickle repository.
4. Added `credentials.json`.
5. Generated `token.pickle`.
6. Tested the generated token.
7. Extracted the OAuth information.
8. Learned how to securely transfer the generated token.

---

## Credits

Original inspiration:

https://github.com/subhajit-maji/Gdrive-OAuth-Gen

Repository:

https://github.com/GK-BOTZ/Token-Pickle
