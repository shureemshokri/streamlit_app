import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Shureem Shokri", "User"]
usernames = ["shureem01","testuser"]
passwords = ["abc123", "def456"]


hashed_pass = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/ "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_pass, file)