import streamlit as st

import streamlit as st

def main():
    st.title("Contact Us - Hotel Booking Management Company")
    st.write("Have questions or need assistance? Feel free to reach out to us!")

    st.write("---") 

    # Contact Information
    st.header("Contact Information")
    st.markdown("You can contact us through the following methods:")

    st.subheader("Email")
    st.write("Email us at [contact@bookingmanagements.com](mailto:contact@bookingmanagements.com)")

    st.subheader("Phone")
    st.write("Call us at +351 123 456 789")

    st.subheader("Address")
    st.write("Visit us at:")
    st.write("123 Main Street")
    st.write("Lisbon")
    st.write("Portugal")

    # Contact Form
    st.header("Contact Form")
    st.write("You can also send us a message using the contact form below:")

    name = st.text_input("Name", "")
    email = st.text_input("Email", "")
    message = st.text_area("Message", "")

    if st.button("Send Message"):
        if name and email and message:
            # You can add code here to send the message to your company's email or database.
            st.success("Message sent successfully!")
        else:
            st.error("Please fill in all the required fields.")

if __name__ == "__main__":
    main()