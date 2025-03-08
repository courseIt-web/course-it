import streamlit as st


st.set_page_config(
    page_title="AI Job Gap Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
    )

st.markdown("""
    
    
    <style>
    
    .stApp{
            position: relative;
            min-height: 100vh;
            background-size: 95%;
            opacity:0.8;
            background-position: center;
         background-image: url('img.jpeg');
background-size: cover; /* Ensures it covers the full area */
background-position: center;
        
        
    }
    
section[data-testid="stSidebar"] {
    display: none;
}
header, .stAppHeader {
    display: none;
    
}
    
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    *{
        

     margin:0;
     padding:0;   
       font-family: 'Poppins', sans-serif;
    }
    
    
    
    
    </style>
    

    """,unsafe_allow_html=True)


st.markdown("""
    <style>
    .navbar {
        overflow: hidden;
        display: flex;
        padding: 10px;
        justify-content:center;
        position:relative;
       transition-delay: 1s;
        top:-120px;
        font-family: 'Poppins', sans-serif;
    
    
    }
    .navbar a {
        color: white;
        padding: 10px 15px;
        text-decoration: none;
        font-size: 16px;
        border-radius:10px;
    margin:20px;
      font-family: 'Poppins', sans-serif;
    }
    .navbar a:hover {
        background-color: #FF4B4B;
       
    }
    .p{
        background-color: #FF4B4B;
        color: black;
        
    }
    </style>

    <div class="navbar">
        <a class="p" href="?page=home">Home</a>
        <a href="?page=about">About</a>
        <a href="?page=contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    
       div[data-testid="stSelectbox"] label {
        color: #32B98B !important;  /* Change to your desired color */
        font-weight:500;
        font-size: 18px !important;
    margin:10px;
    }
    
    
    /* Center the selectbox container */
    div[data-testid="stSelectbox"] {
        max-width: 300px !important;
        margin: 0 auto !important;
        color:#32B98B;
    }

    /* Target the container that renders the select control */
    div[data-testid="stSelectbox"] > div {
        background-color: #5b5b5b !important;
        color: #32B98B !important;  /* Use white text for contrast */
        border-radius: 10px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }

    /* Target the arrow icon if present */
    div[data-testid="stSelectbox"] svg {
        fill: #32b98B !important;
    }

    /* When focused, adjust the styling */
    div[data-testid="stSelectbox"] > div:focus {
        outline: none !important;
        
        
        
 border: 2px solid #32B98B !important; /* Custom highlight border */
    outline: none !important;
 background-color: #32B98B !important; /* Change background if desired */
        border-radius: 10px !important;
  
        
    }
    
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    
    <style>
    
    .m{
        display:flex;
        align-items:center;
        justify-content:center;
        color:#FF4B4B;
        font-weight:600;
        font-size:40px;
        margin-bottom:70px;
        cursor:pointer;
        transition:transform 0.4s ease;
        
    }
      .m:hover{
          transform:scale(1.03);
      }
      
      
div[data-testid="stTextInput"] {
    max-width: 100% !important;
  
}



      div[data-testid="stTextInput"] input[type="text"] {
        background-color: #5B5B5B !important; 
        color: whte !important; 
  
      
        border-radius: 6px !important;
        padding: 8px !important;
    
       
    }
    /* Style the placeholder text */
    div[data-testid="stTextInput"] input[type="text"]::placeholder {
        color: 282b2c !important; /* Placeholder color */
        opacity: 1 !important;
        font-weight:300;
    }
    
    
div[data-testid="stTextInput"] input[type="text"]:focus {
    border: 2px solid #32B98B !important; 
    outline: none !important; 
    cursor:pointer;
}
div[data-testid="stSelectbox"] label {
        color: #32B98B !important; /* Change to desired color */
        font-size: 30px !important; /* Adjust font size */
        font-weight: 600 !important; /* Bold if desired */
      background-color: #5b5b5b !important;
      border-radius:10px;  
      cursor:pointer;
    }    

/* Center the selectbox container */
div[data-testid="stSelectbox"] {
    max-width: 500px !important;
    margin: 0 auto !important;
    background-color:#5b5b5b;
    padding:20px;
    border-radius:30px;
    transition:transform 0.4s ease;
 cursor:pointer;   
}
    
}
/* Target the container that renders the select control */
div[data-testid="stSelectbox"] > div {
    background-color: #5b5b5b !important;
    color: #5b5b5b !important;
    # border-radius: 10px !important;
    padding: 10px !important;
    font-size: 16px !important;
    cursor:pointer;
}

/* Target the arrow icon if present */
div[data-testid="stSelectbox"] svg {
    fill: #5b5b5b !important;
    cursor:pointer;
}

/* When focused, adjust the border */
div[data-testid="stSelectbox"] > div:focus {
    # border: 2px solid #5b5b5b !important;
    outline: none !important;
    background-color:#32B98B;
    border-radius:10px;
    cursor:pointer;
}
    
    </style>
 <div class="m">
    What would you like to Learn?
</div>
    
    
    
    
    
    """,unsafe_allow_html=True)




# other_skills = st.text_input("",placeholder="Search the Domain")

# st.write("""
    
#     <style>
#     .a{
        
#         color:#32b98b;
#     font-weight:600;
#     font-size:30px;
#     display:flex;
#     align-items:center;
#     justify-content:center;
#     margin:20px;
    
#     }    
    
#     </style>
#     <div class = "a">Or</div>

st.markdown("""
    <style>
    
    .l{
        
        color:#FF4B4B;
     position:absolute;
 bottom:-80px;
         z-index:4;
         left:400px;
         font-weight:600;
         background-color:#5b5b5b;
         cursor:pointer;
      font-family: 'Poppins', sans-serif;
    }
    </style>
    <div class="l">
    Choose :
    </div>
    
    """,unsafe_allow_html=True)

import streamlit as st

# Initialize session state variable if it doesn't exist
if "selected_option" not in st.session_state:
    st.session_state.selected_option = ""

# Selectbox with session state storage
selected_option = st.selectbox(
    "",
    ("Select an option", "Web Dev", "Machine Learning", "Data Structures", "Game Dev", "Cyber Security"),
)

# Store the selection in session state
st.session_state.selected_option = selected_option

# Navigate only when a valid option is chosen
if selected_option and selected_option != "Select an option":
    st.switch_page("pages/skills.py")

#navigating to other page



# if page == "home":
#     st.write("🏠 Welcome to Home Page!")
# elif page == "about":
#     st.write("📖 About Us")
# elif page == "contact":
#     st.write("📧 Contact Us")
