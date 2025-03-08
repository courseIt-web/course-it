import streamlit as st
import random
import json
import time

# Hide sidebar and header
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
st.markdown('<div class="k"><h1>Checking Skill Gap</h1></div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Let's Check Your Skill Gap:")

# Define the job skills data
data = {
    "Machine Learning": {
        "required_skills": [
            "Python", "SQL", "Machine Learning", "Statistics", "Data Visualization",
            "TensorFlow/PyTorch", "NLP", "A/B Testing", "Big Data Tools"
        ]
    },
    "Frontend Developer": {
        "required_skills": [
            "HTML/CSS", "JavaScript", "React/Angular/Vue", "Responsive Design",
            "Web Performance", "Version Control", "Testing", "UI/UX Principles"
        ]
    },
    "Backend Developer": {
        "required_skills": [
            "Python/Java/Node.js", "Databases", "API Development", "Authentication",
            "Server Management", "Containerization", "Microservices", "Security"
        ]
    }
}

# Set default session state values if not already defined
if "selected_option" not in st.session_state:
    st.session_state.selected_option = "Machine Learning"  # Default job title
if "user_skills" not in st.session_state:
    st.session_state.user_skills = ["Python", "SQL", "Machine Learning"]  # Default skills

# Retrieve job title and user skills from session state
job_title = st.session_state.selected_option
user_skills = st.session_state.user_skills

# Write the job skills data to file (this overwrites every run; adjust as needed)
with open('job_skills.json', 'w') as f:
    json.dump(data, f, indent=4)

# Function to load job skills data from file
def load_job_skills():
    with open('job_skills.json', 'r') as f:
        return json.load(f)

# Function to analyze the skill gap
def analyze_skill_gap(user_skills, job_title):
    job_data = load_job_skills()
    
    if job_title not in job_data:
        return [], [], 0  # Return empty results if job title not found
    
    required_skills = job_data[job_title]["required_skills"]
    
    # Convert both lists to lowercase for case-insensitive comparison
    user_skills_lower = [skill.lower() for skill in user_skills]
    required_skills_lower = [skill.lower() for skill in required_skills]
    
    # Determine missing and matching skills
    missing_skills = [skill for skill, skill_lower in zip(required_skills, required_skills_lower)
                      if skill_lower not in user_skills_lower]
    matching_skills = [skill for skill, skill_lower in zip(required_skills, required_skills_lower)
                       if skill_lower in user_skills_lower]
    
    # Calculate match percentage
    match_percentage = (len(matching_skills) / len(required_skills) * 100) if required_skills else 0
    return missing_skills, matching_skills, float(match_percentage)

# Get analysis results
missing_skills, matching_skills, match_percentage = analyze_skill_gap(user_skills, job_title)

# Save the analysis results to session state so that they persist across pages
st.session_state.missing_skills = missing_skills
st.session_state.matching_skills = matching_skills
st.session_state.match_percentage = match_percentage

# Display the analysis results
st.subheader("Analysis Results")
st.markdown(f"**Skill Match: {match_percentage:.1f}%**")
st.progress(match_percentage / 100)

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Skills You Have:**")
    for skill in matching_skills:
        st.markdown(f"✅ {skill}")
with col2:
    st.markdown("**Skills You Need:**")
    for skill in missing_skills:
        st.markdown(f"❌ {skill}")

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Go Back"):
        st.switch_page("pages/skills.py")
with col2:
    if st.button("Continue"):
        st.switch_page("pages/todo.py")

# Ensure user_skills stays in session state
st.session_state.user_skills = user_skills
