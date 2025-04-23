
import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker by Shazia Naveed", page_icon="", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {text-align: center;}
        .stButton button {
            width: 50%;
            background-color: #4caf50;
            color: white;
            font-size: 18px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level.")

# Input
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include both uppercase (A-Z) and lowercase (a-z) letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Display strength
    if score == 4:
        st.success("✅ Strong password - your password is secure.")
    elif score == 3:
        st.info("🟡 Moderate password - Consider improving it for better security.")
    else:
        st.error("❌ Weak password - Follow the suggestions below to strengthen it.")
        if feedback:
            with st.expander("💡 Suggestions to improve your password"):
                for item in feedback:
                    st.write("- " + item)

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
