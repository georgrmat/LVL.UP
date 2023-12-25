import streamlit as st
import page1, page2  # Import your page scripts

# Add page selectors to the sidebar
page = st.sidebar.selectbox("Select a page", ["Home", "Page 1", "Page 2"])

# Display the selected page
if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
elif page == "Page 1":
    page1.show()
elif page == "Page 2":
    page2.show()
