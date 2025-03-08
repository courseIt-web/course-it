import streamlit as st

# Hide sidebar and header

st.markdown("""
    
    <style>
    /* Style for the 'Go Back' button */
    div.stButton > button:first-child {
        background-color: #ff4b4b; /* Red */
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }

    /* Fixing text background issue */
    div.stButton > button:first-child:hover {
        background-color: #d14343; /* Darker Red on Hover */
    }

    /* Remove unwanted text background */
    div.stButton > button {
        background: none !important;
        box-shadow: none !important;
    }

    /* Style for the 'Continue' button */
    div.stButton > button:nth-child(2) {
        background-color: #4caf50 !important; /* Green */
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }

    div.stButton > button:nth-child(2):hover {
        background-color: #45a049; /* Darker Green on Hover */
    }
</style>
    
    
    
    """,unsafe_allow_html=True)

st.markdown("""
<style>    
section[data-testid="stSidebar"], header, .stAppHeader {
    display: none;
}
* {
    background-color: #282b2c;
    margin: 0; /* Remove default browser margin */
    padding: 0;
    font-family: 'Poppins', sans-serif;
}
/* Center H1 */
.k {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="k"><h1>Skill Assessment</h1></div>', unsafe_allow_html=True)

# Full-width subheader


st.markdown(
    """
    
    <hr>
    
    """
    ,unsafe_allow_html=True)

st.subheader("Let us know your current skills")


# List of common skills
common_skills = [
 "Python", "JavaScript", "Java", "C", "C++", "C#", "HTML", "CSS", "TypeScript", "PHP",
    "SQL", "R", "Kotlin", "Swift", "Dart", "Go", "Bash", "YAML",
    "React", "Angular", "Vue.js", "Node.js", "Express", "Django", "Flask", "Spring Boot", "FastAPI",
    ".NET", "Laravel", "Ruby on Rails",
    "TensorFlow", "PyTorch", "Scikit-learn", "NumPy", "Pandas", "Matplotlib", "Seaborn",
    "Docker", "Kubernetes", "Terraform", "Jenkins", "Ansible", "GitHub Actions",
    "Unity", "Unreal Engine", "Godot", "Pygame",
    "Metasploit", "Nmap", "Wireshark", "Burp Suite", "Scapy",
    "Jetpack Compose", "React Native", "SwiftUI", "Flutter"
    ]

# Apply custom CSS that adapts to the theme and adds extra margin above the component.
st.markdown("""
<style>
    /* Add extra margin above the multiselect container */
    .stMultiSelect {
        margin-top: 20px;
    }

    /* Light theme styles */
    html[data-theme="light"] .stMultiSelect [data-baseweb="select"],
    html[data-theme="light"] .stMultiSelect [data-baseweb="menu"] {
        background-color: #ffffff;
        color: #000000;
    }
    html[data-theme="light"] .stMultiSelect [data-baseweb="tag"] {
        background-color: #ff4b4b; /* Accent color */
        color: #ffffff;
    }
    html[data-theme="light"] .stMultiSelect [role="option"]:hover {
        background-color: rgba(255, 75, 75, 0.2);
    }

    /* Dark theme styles */
    html[data-theme="dark"] .stMultiSelect [data-baseweb="select"],
    html[data-theme="dark"] .stMultiSelect [data-baseweb="menu"] {
        background-color: #282b2c;
        color: #ffffff;
    }
    html[data-theme="dark"] .stMultiSelect [data-baseweb="tag"] {
        background-color: #ff4b4b;
        color: #ffffff;
    }
    html[data-theme="dark"] .stMultiSelect [role="option"]:hover {
        background-color: rgba(255, 75, 75, 0.2);
  
    
      
        
          
            
              
                     /* Style for the 'Go Back' button */
        div.stButton > button:first-child {
            background-color: #282b2c; 
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }

        /* Style for the 'Continue' button */
        div.stButton > button:nth-child(2) {
            background-color: #282b2c; /* Green */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
                  
                    
                      
                        
                          
                            
                              
                                  }
</style>
""", unsafe_allow_html=True)

# Create the multiselect with the common skills list
user_skills = st.multiselect("Select your skills", options=common_skills)

# Display the selected skills
if user_skills:
    st.write("You selected:", user_skills)

st.markdown(
    """

    <hr>
    
    """
    ,unsafe_allow_html=True)

        
        
        
        
        
        
        # Experience level
st.subheader("What is your experience level?")
experience = st.radio(
    "Select your overall experience level",
    ["Beginner(0-3months)", "Intermediate(3-12months)", "Professional(1Year+)"]
)

st.session_state.experience = experience

st.markdown(
    """
    
    <hr>
    
    """
    ,unsafe_allow_html=True)
        
        
st.subheader("Prefered Language?")
lang = st.radio(
    "Select your prefered language",
    ["Hindi", "English", ]
)

st.markdown(
    """
    
    <hr>
    
    """
    ,unsafe_allow_html=True)
        
        
col1, col2 = st.columns(2)

with col1:
    if st.button("Go Back"):
        st.switch_page("./my_app.py")

with col2:
    if st.button("Continue"):
        st.switch_page("pages/page_3.py")
        
st.session_state.user_skills=user_skills