# 🚀 Generate Google Drive `token.pickle`, Client ID, Client Secret & Refresh Token on WSL

This guide explains how to generate a valid **Google OAuth 2.0 `token.pickle`** and extract:

- ✅ Client ID
- ✅ Client Secret
- ✅ Refresh Token

using **Windows Subsystem for Linux (WSL)** and `credentials.json`.

These credentials can be used for:

- Cloudflare SecretX Index
- Google Drive OAuth scripts
- Google Drive API automation
- Other Google API integrations

> ⚠️ **Security:** `credentials.json`, `token.pickle`, Client Secret, and Refresh Token are sensitive credentials. Never commit them to GitHub or share them publicly.

---

## 🔗 Links

- WSL: https://learn.microsoft.com/windows/wsl/install
- Google Cloud Console: https://console.cloud.google.com
- OAuth 2.0 Playground: https://developers.google.com/oauthplayground
- Token-Pickle Repository: https://github.com/GK-BOTZ/Token-Pickle
- Original project credit: https://github.com/subhajit-maji/Gdrive-OAuth-Gen

---

# 🐧 WSL Setup

## 1. Install WSL

Open **PowerShell as Administrator** in Windows and run:

```powershell
wsl --install -d Ubuntu-24.04
```

Restart Windows if requested. Then launch **Ubuntu** from the Start Menu and create your Linux username and password.

Check that WSL is working:

```powershell
wsl --status
```

You can also check the installed distributions:

```powershell
wsl -l -v
```

The Ubuntu distribution should normally show **WSL 2**.

If your distribution is using WSL 1 and you want WSL 2:

```powershell
wsl --set-version Ubuntu-24.04 2
```

---

## 2. Update Ubuntu and Install Required Packages

Open your WSL Ubuntu terminal and run:

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y git python3 python3-pip python3-venv ca-certificates
```

Check Python and Git:

```bash
python3 --version && git --version
```

---

# 📦 Install the Google OAuth Libraries

## 3. Create a Virtual Environment

Using a virtual environment avoids conflicts with Ubuntu's system Python packages.

```bash
python3 -m venv .venv && source .venv/bin/activate
```

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

Install the required Google libraries:

```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Whenever you reopen WSL and return to the project, activate the environment again:

```bash
source .venv/bin/activate
```

---

# 📥 Clone the Repository

## 4. Clone Token-Pickle

You can use the original repository directly:

```bash
git clone https://github.com/GK-BOTZ/Token-Pickle.git
```

Enter the repository:

```bash
cd Token-Pickle
```

If you have your own fork, clone that repository instead:

```bash
git clone https://github.com/YOUR_USERNAME/Token-Pickle.git
cd Token-Pickle
```

The repository's current `generate.py` searches the current directory for a `.json` credentials file, so keep `credentials.json` in the same directory where you run the script. citeturn772268view0

---

# 🔑 Google Cloud Credentials

## 5. Create or Download `credentials.json`

Open:

https://console.cloud.google.com

Create or select your Google Cloud project, enable the API you need, configure the OAuth consent screen, and create an **OAuth 2.0 Client ID**.

Download the OAuth client JSON file.

Rename it to:

```text
credentials.json
```

Place it inside the cloned `Token-Pickle` directory.

Your directory should look similar to:

```text
Token-Pickle/
├── .venv/
├── credentials.json
├── generate.py
└── token.pickle
```

`token.pickle` will appear after successful authentication.

> ⚠️ Do not upload `credentials.json` or `token.pickle` to a public repository.

---

# 🚀 Generate `token.pickle`

## 6. Run the Generator

Make sure you are inside the repository and the virtual environment is active:

```bash
cd ~/Token-Pickle && source .venv/bin/activate
```

Run:

```bash
python3 generate.py
```

The repository's `generate.py` uses the Google Drive OAuth scope and starts a local OAuth server without automatically opening a browser. It prints the authentication URL that you can open manually. citeturn772268view0

---

## 7. Open the OAuth URL in Windows

Copy the URL printed by the WSL terminal and open it in **Chrome, Edge, or another Windows browser**.

Sign in with the Google account that should authorize the application and grant the requested permissions.

After successful authentication, the browser should complete the OAuth redirect and the script should save:

```text
token.pickle
```

The repository's current script stores the token in the same working directory. citeturn772268view0

You may see a message similar to:

```text
The authentication flow has completed. You may close this window.
```

---

# 🌐 If `localhost` Does Not Work

WSL normally allows Windows applications to access services running on WSL through `localhost` when localhost forwarding is enabled.

First check your WSL version:

```powershell
wsl -l -v
```

If the OAuth callback cannot reach the WSL process, restart WSL from PowerShell:

```powershell
wsl --shutdown
```

Then open Ubuntu again and rerun:

```bash
cd ~/Token-Pickle && source .venv/bin/activate && python3 generate.py
```

If you are using a custom WSL networking configuration, check your WSL networking settings before changing anything. Randomly poking networking until OAuth stops complaining is a beloved human tradition, but not a particularly efficient one.

---

# 📂 Locate `token.pickle` From Windows

Your WSL home directory can be opened from Windows File Explorer using:

```text
\\wsl$\Ubuntu-24.04\home\YOUR_USERNAME\Token-Pickle
```

You can also open the current WSL directory directly from the terminal:

```bash
explorer.exe .
```

To verify the generated file:

```bash
ls -lh token.pickle
```

---

# 📥 Download `token.pickle` Through a Local HTTP Server

You do not need to download it through an HTTP server when using WSL because Windows Explorer can access the WSL filesystem directly.

However, if you specifically want a browser download, run:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

Then open this in your Windows browser:

```text
http://localhost:8080
```

Download:

```text
token.pickle
```

Stop the server when finished with:

```text
Ctrl+C
```

> ⚠️ The HTTP server exposes the current directory over the network interface you bind it to. Keep this temporary and local, and stop it immediately after downloading sensitive files.

For a simpler and safer WSL-to-Windows transfer, prefer:

```bash
explorer.exe .
```

---

# 🧪 Test `token.pickle`

If your repository contains `test_token_pickle.py`, run:

```bash
python3 test_token_pickle.py
```

If the script is not present in your copy of the repository, this command will naturally fail because files have not yet developed telepathy. The current repository page lists `README.md` and `generate.py` in the visible file tree. citeturn435980view0

---

# 🔍 Extract `token.pickle` Information

If your repository contains `extract_token_pickle.py`, run:

```bash
python3 extract_token_pickle.py
```

This can be used to inspect the credentials stored in the generated token and retrieve values needed by compatible applications.

---

# 🧾 View Raw `token.pickle` Data

To inspect the credential object's attributes directly:

```bash
python3 -c "import pickle; from pprint import pprint; pprint(vars(pickle.load(open('token.pickle', 'rb'))))"
```

Typical credential information may include values such as:

```text
token
refresh_token
client_id
client_secret
scopes
expiry
```

The exact fields depend on the credential object and authentication flow.

> ⚠️ Never paste the full output publicly. A refresh token and client secret can grant access to your Google account or APIs within the authorized scope.

---

# 🔐 Client ID, Client Secret & Refresh Token

## Client ID and Client Secret

The **Client ID** and **Client Secret** normally come from your downloaded OAuth client JSON file.

You can inspect the JSON locally with:

```bash
python3 -c "import json; d=json.load(open('credentials.json')); print(d)"
```

A typical OAuth client file contains a structure similar to:

```json
{
  "installed": {
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
  }
}
```

Some credential files may use a different top-level key such as `web` instead of `installed`.

To print only the Client ID and Client Secret without printing unrelated fields:

```bash
python3 -c "import json; d=json.load(open('credentials.json')); c=next(iter(d.values())); print('CLIENT_ID:', c.get('client_id')); print('CLIENT_SECRET:', c.get('client_secret'))"
```

## Refresh Token

The generated `token.pickle` can contain the OAuth **refresh token** when the authorization flow returns one.

To print only the refresh token:

```bash
python3 -c "import pickle; print(pickle.load(open('token.pickle','rb')).refresh_token)"
```

To print Client ID, Client Secret, and Refresh Token together:

```bash
python3 -c "import json,pickle; d=json.load(open('credentials.json')); c=next(iter(d.values())); t=pickle.load(open('token.pickle','rb')); print('CLIENT_ID:', c.get('client_id')); print('CLIENT_SECRET:', c.get('client_secret')); print('REFRESH_TOKEN:', t.refresh_token)"
```

> ⚠️ Treat all three values as secrets. In particular, never put them directly into source code that is pushed to GitHub.

---

# 🔄 Re-authenticate / Generate a New Token

If `token.pickle` already exists, the current `generate.py` loads it and, when appropriate, attempts to refresh the credentials using the stored refresh token. Otherwise it runs the interactive OAuth flow. citeturn772268view0

To force a completely new OAuth authorization, remove the old token first:

```bash
rm -f token.pickle
```

Then run:

```bash
python3 generate.py
```

---

# 🧹 Clean Up Sensitive Files

After copying the credentials to the destination where they are needed, remove temporary files from the WSL project directory if they are no longer required:

```bash
rm -f token.pickle credentials.json
```

Do this only after confirming that you have securely stored whatever credentials your application actually needs.

---

# 🛡️ Recommended `.gitignore`

If this directory is a Git repository, create `.gitignore` before committing anything:

```gitignore
credentials.json
token.pickle
.venv/
__pycache__/
*.pyc
```

Then check Git's status:

```bash
git status --short
```

The sensitive files should not appear as files ready to commit.

---

# 🧰 Useful WSL Commands

## Open the current folder in Windows Explorer

```bash
explorer.exe .
```

## Show the current directory

```bash
pwd
```

## List files

```bash
ls -lah
```

## Check the WSL IP address

```bash
hostname -I
```

## Stop all WSL distributions

Run this from **PowerShell**:

```powershell
wsl --shutdown
```

## Enter Ubuntu from PowerShell

```powershell
wsl -d Ubuntu-24.04
```

---

# ✅ Complete Quick Setup

For a fresh Ubuntu 24.04 WSL installation, the main setup can be done with:

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y git python3 python3-pip python3-venv ca-certificates && git clone https://github.com/GK-BOTZ/Token-Pickle.git && cd Token-Pickle && python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Then place `credentials.json` inside the `Token-Pickle` directory and run:

```bash
python3 generate.py
```

Open the printed OAuth URL in your Windows browser and complete authentication.

---

# ✅ Done

You have now generated a Google OAuth `token.pickle` from **WSL** and can inspect or transfer it for use with compatible Google API applications.

The repository's current `generate.py` is specifically configured for the Google Drive OAuth scope and saves the credential object as `token.pickle`. citeturn772268view0

## Credits

- Token-Pickle: https://github.com/GK-BOTZ/Token-Pickle
- Original project: https://github.com/subhajit-maji/Gdrive-OAuth-Gen
