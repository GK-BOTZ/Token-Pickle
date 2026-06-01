# 🔐 Token Generator for Google OAuth (`token.pickle`)

This tool allows you to securely generate a `token.pickle` for accessing Google APIs (Drive, Gmail, YouTube, etc.) using `credentials.json`.

---

## 🚀 Setup Instructions

### 1. Install Termux (If Not Already)

> ⚠️ **Download from F-Droid, NOT the Play Store!**  
> ➡️ [Termux on F-Droid](https://f-droid.org/en/packages/com.termux/)

Then open Termux and run:

```bash
pkg update && pkg upgrade -y
pkg install git python python-pip -y
```

---

### 2. Install `python-cryptography` (Important!)

```bash
pkg install python-cryptography
```

> 💡 This step prevents build errors when installing Google auth libraries. Install this **before** running `pip install`.

---

### 3. Fork This Repository

https://github.com/GK-BOTZ/Token-Pickle/fork

---

### 4. Upload Your Credentials File

Upload your `.json` file and name it `credentials.json`

---

### 5. Clone The Repo

```bash
git clone https://github.com/YOUR_USERNAME/Token-Pickle
cd Token-Pickle
```

---

### 6. Install Python Requirements

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2
```

---

### 7. Generate the Token

```bash
python3 generate.py
```

- Copy the URL shown in Termux
- Open it in a browser
- Sign in and allow access
- You'll see: *"The authentication flow has completed. You may close this window."*

---

### 8. Download the `token.pickle` File

Run a simple Python HTTP server to download the token from your mobile browser:

```bash
python3 -m http.server 8080
```

Visit `http://localhost:8080` in your Android browser (e.g. Chrome) and download `token.pickle` directly.

---

## ✅ Done

You've successfully generated and saved `token.pickle`.  
Use it in your projects to access Google APIs without re-authenticating.

---

## ❓ Troubleshooting

| Error | Solusi |
|-------|--------|
| `cryptography build failed` | Run `pkg install python-cryptography` first |
| `credentials.json not found` | Make sure the file is uploaded and named correctly |
| `ModuleNotFoundError` | Re-run the `pip install` command in Step 6 |
| `permission denied` on storage | Run `termux-setup-storage` and allow access |
