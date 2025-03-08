import streamlit as st
import random
import json
import time


missing_skills=st.session_state.missing_skills

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

# Function to generate the learning roadmap based on missing skills and recommendations
def generate_roadmap(missing_skills, recommendations):
    roadmap = []

    prioritized_skills = sorted(missing_skills, key=lambda x: random.random())
    
    for skill in prioritized_skills:
        if skill in recommendations:
            courses = recommendations[skill]
            estimated_weeks = random.randint(2, 8)  # Random estimate for demo purposes
            roadmap.append({
                "skill": skill,
                "courses": courses,
                "estimated_time": f"{estimated_weeks} weeks"
            })
    return roadmap

def main():
    recommendations = {
        "Python": ["Learn Python Basics", "Intermediate Python"],
        "SQL": ["SQL Fundamentals", "Advanced SQL"],
        "Machine Learning": ["Intro to Machine Learning", "Machine Learning with Python"]
    }
    
    # Generate the roadmap using the dummy data
    roadmap = generate_roadmap(missing_skills, recommendations)
    
    # Learning Roadmap page
    st.title("📚 Learning Roadmap")
    st.subheader("Your personalized learning path")
    
    if roadmap:
        for i, step in enumerate(roadmap, 1):
            with st.expander(f"Step {i}: Learn {step['skill']} (Est. time: {step['estimated_time']})"):
                st.markdown(f"**Recommended Courses for {step['skill']}:**")
                for j, course in enumerate(step['courses'], 1):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"{j}. {course}")
                    with col2:
                        # For demonstration, assume username is stored in session_state
                        username = st.session_state.get("username", None)
                        if username and st.button("Complete", key=f"complete_{i}_{j}"):
                            with st.spinner("Updating your progress..."):
                                # Dummy function for awarding points (replace with your actual function)
                                points_earned = random.randint(10, 50)
                                total_points = random.randint(100, 500)
                                time.sleep(1)  # Simulate processing delay
                                st.success(f"🎉 You earned {points_earned} points! Total: {total_points}")
    else:
        st.info("No specific learning roadmap needed. You're already well-matched for this position!")

if __name__ == "__main__":
    main()
