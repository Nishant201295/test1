import streamlit as st

# Hardcoded student and parent credentials (for demonstration purposes)
STUDENT_CREDENTIALS = {"student1": "password1", "student2": "password2"}
PARENT_CREDENTIALS = {"parent1": "password1", "parent2": "password2"}

# Function to authenticate student login
def authenticate_student(username, password):
    return STUDENT_CREDENTIALS.get(username) == password

# Function to authenticate parent login
def authenticate_parent(username, password):
    return PARENT_CREDENTIALS.get(username) == password

# Main function to run the Streamlit app
def main():
    st.title("School Management App")

    # Sidebar for login type selection
    login_type = st.sidebar.radio("Login As", ("Student", "Parent"))

    if login_type == "Student":
        st.subheader("Student Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_student(username, password):
                st.success("Login successful as student.")
                # Add student dashboard functionality here
            else:
                st.error("Invalid username or password for student.")
    
    elif login_type == "Parent":
        st.subheader("Parent Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_parent(username, password):
                st.success("Login successful as parent.")
                # Add parent dashboard functionality here
            else:
                st.error("Invalid username or password for parent.")

if __name__ == "__main__":
    main()
