import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

def test_token():
    if not os.path.exists('token.pickle'):
        print("❌ Error: token.pickle file not found in this directory!")
        return

    # 1. Load the token
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

    # 2. Check validity and refresh if expired
    if creds and creds.expired and creds.refresh_token:
        print("🔄 Token expired. Attempting automatic background refresh...")
        try:
            creds.refresh(Request())
            # Save the refreshed token back to the file
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
            print("✅ Token refreshed successfully!")
        except Exception as e:
            print(f"❌ Refresh failed: {e}")
            return

    if not creds or not creds.valid:
        print("❌ Token is invalid. You need to re-authenticate.")
        return

    print("🔑 Token authenticated successfully. Connecting to Google API...")

    # 3. Test the token by calling the API
    try:
        service = build('drive', 'v3', credentials=creds)
        
        # Call the Drive API to list the 10 most recent files
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        print("\n🎉 Success! Connection verified. Your files:")
        if not items:
            print('No files found (but the API connection worked!).')
        else:
            for item in items:
                print(f"- {item['name']} ({item['id']})")
                
    except Exception as e:
        print(f"❌ API Call failed: {e}")
        print("Hint: Check if your token has the correct API scopes enabled.")

if __name__ == '__main__':
    test_token()
