import streamlit as st

# Access control based on user email
st.set_page_config(layout="wide")
st.title("Log In/Sign Up ")
st.markdown("Register to gain more insights about your business! We're sure you will not regret it!")

col1, col2 = st.columns(2)
with col1:
    if st.button("Sign Up", key="signup_button"):
        # Handle sign-up logic here
        st.subheader("Sign Up")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Submit", key="signup_submit_button"):
            # Handle sign-up submission logic here
            st.success("Sign-up successful! You can now log in.")
with col2:
    if st.button("Log In", key="login_button"):
        # Handle login logic here
        st.subheader("Log In")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Log In", key="login_submit_button"):
            # Handle login submission logic here
            # Replace this with your authentication logic
            if username == "demo" and password == "demo":
                st.success("Login successful!")
            else:
                st.error("Login failed. Please check your credentials.")