# # import streamlit as st
# # from sesh_state import SessionState

# # import sqlite3
# # from pages.Home_01 import home_page
# # from pages.About_03 import about_page

# # session_state = SessionState()


# # def create_table():
# #     conn = sqlite3.connect('database.db')
# #     cursor = conn.cursor()

# #     # Create a users table
# #     cursor.execute('''
# #     CREATE TABLE IF NOT EXISTS users (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         username TEXT UNIQUE,
# #         password TEXT
# #     );
# #     ''')

# #     conn.commit()
# #     conn.close()

# # def login():
# #     username = st.text_input("Username")
# #     password = st.text_input("Password", type='password')

# #     if st.button("Login"):
# #         # Validate credentials
# #         if validate_login(username, password):
# #             st.success("Logged in successfully!")
# #             # Add redirection or other actions upon successful login
# #         else:
# #             st.error("Invalid username or password")

# # def validate_login(username, password):
# #     conn = sqlite3.connect('database.db')
# #     cursor = conn.cursor()

# #     # Check if the username and password match a record in the database
# #     cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
# #     user = cursor.fetchone()

# #     conn.close()
# #     return user is not None


# # def main():
# #     st.title("BUNGA.COM")
# #     st.subheader("Welcome to BUNGA.COM where you can predict the image of your flower!")
# #     # st.button("Next", on_click=project_page)

# #     create_table()  # Ensure the users table exists

# #     # # Display login form
# #     # login()

# #     # Display login form if not logged in
# #     if not session_state.get("logged_in", False):
# #         login()
# #     else:
# #         st.write("Welcome to the application!")
# #         selected_page = st.sidebar.selectbox("Select a page", ["Home","Classification","About"])
# #         if selected_page == "Home":
# #             home_page()
# #         elif selected_page == "About":
# #             about_page()
# #         # elif selected_page == "Classification":
# #         #     classification_page()

# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# from sesh_state import SessionState
# import sqlite3
# from zmq import has
from pages.Home_01 import home_page
from pages.About_03 import about_page
from pages.Classification_02 import classify_page

# # session_state = SessionState()


# def create_table():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()

#     # Create a users table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE,
#         password TEXT
#     );
#     ''')

#     conn.commit()
#     conn.close()

# def login():
#     username = st.text_input("Username")
#     password = st.text_input("Password", type='password')

#     if st.button("Login"):
#         # Validate credentials
#         if validate_login(username, password):
#             session_state.set(logged_in=True, username=username)
#             st.success("Logged in successfully!")
#             # Add redirection or other actions upon successful login
#         else:
#             st.error("Invalid username or password")

# def validate_login(username, password):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()

#     # Check if the username and password match a record in the database
#     cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
#     user = cursor.fetchone()

#     conn.close()
#     return user is not None

# def main():
#     st.title("BUNGA.COM")
#     st.subheader("Welcome to BUNGA.COM where you can predict the image of your flower!")

#     create_table()  # Ensure the users table exists

#     # Display login form if not logged in
#     if not session_state.get("logged_in", False):
#         login()
#     else:
#         st.write(f"Welcome, {session_state.username}!")

#         selected_page = st.sidebar.selectbox("Select a page", ["Home", "About"])
#         if selected_page == "Home":
#             home_page()
#         elif selected_page == "About":
#             about_page()

# if __name__ == "__main__":
#     main()
import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


# # Load configuration
# with open("C:\\Users\\Shureem Shokri\\Documents\\DEGREE\\YEAR 3\\SEM 2\\FYP\\code\\st_multi_app\\config.yaml", "r") as f:
#     config = yaml.safe_load(f)

# # Create authenticator object
# authenticator = stauth.Authenticate(
#     config["credentials"],
#     config["cookie"]["name"],
#     config["cookie"]["key"],
#     config["cookie"]["expiry_days"],
    
    
    
    
    
# )

# # Display login widget
# name, authentication_status, username = authenticator.login("Login", "main")

# --------------User Authentication----------
names = ["Shureem Shokri", "User"]
usernames = ["shureem01","testuser"]

# load passwords
file_path = Path(__file__).parent/"hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)


authenticator = stauth.Authenticate(names,usernames,hashed_passwords, "bunga_app", "abcdef", cookie_expiry_days=2)

name, authentication_status,username = authenticator.login("Login","main" )



def main():

    # Customizing the styling of the title
    st.markdown(
        """
        <style>
            /* Custom CSS for styling */
            .app-title {
                font-size: 36px;
                font-weight: bold;
                color: #FF5733;  /* Change to your desired color */
                font-family: 'Arial', sans-serif;  /* Change to your desired font */
                margin-bottom: 20px;  /* Adjust spacing */
            }

            .welcome-message {
                font-size: 18px;
                color: #008080;  /* Change to your desired color */
                font-family: 'Helvetica', sans-serif;  /* Change to your desired font */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Applying the custom class to the title
    st.markdown('<p class="app-title">BUNGA.COM 🌺</p>', unsafe_allow_html=True)

    # Applying the custom class to the welcome message
    st.markdown('<p class="welcome-message">Welcome to BUNGA.COM where you can predict the image of your flower!</p>', unsafe_allow_html=True)

    if authentication_status == True :
        st.write(f"Welcome, {username}!")

        # Protected app content
        selected_page = st.sidebar.selectbox("Select a page", ["Home","Classification", "About"])
        if selected_page == "Home":
            home_page()
        elif selected_page =="Classification":
            classify_page()
        elif selected_page == "About":
            about_page()

    else:
        st.warning("Please log in to access the application.")

if __name__ == "__main__":
    main()



