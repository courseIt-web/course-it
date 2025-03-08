import google.generativeai as genai


domains_dict = {
    "soft dev": ["python", "C++", "java", "C#", "Django", "Flask", "Spring Boot", ".NET", "FastAPI"],
    "web dev": ["HTML", "CSS", "JavaScript", "Python", "TypeScript", "PHP", "React", "Vue.js", "Angular", "Django", "Flask", "Node.js", "Express"],
    "ds ml": ["Python", "R", "SQL", "NumPy", "Pandas", "Scikit-learn", "TensorFlow", "PyTorch", "Matplotlib", "Seaborn"],
    "app dev": ["Kotlin", "Swift", "Dart", "Java", "JavaScript", "Flutter", "React Native", "SwiftUI", "Jetpack Compose"],
    "devops": ["Python", "Go", "Bash", "YAML", "Docker", "Kubernetes", "Terraform", "Jenkins", "Ansible", "GitHub Actions"],
    "cyber sec": ["Python", "C", "C++", "JavaScript", "Metasploit", "Nmap", "Wireshark", "Burp Suite", "Scapy"],
    "game dev": ["C#", "C++", "Python", "JavaScript", "Unity", "Unreal Engine", "Godot", "Pygame"],
}

genai.configure(api_key="AIzaSyAxTlLKs0vJoa2lYsic9acrGNuKckX4yFw")
model = genai.GenerativeModel("gemini-1.5-flash-8b")

def get_learning_resources(domain, current_skills, language_preference):
    if domain not in domains_dict:
        available_domains = ", ".join(domains_dict.keys())
        raise ValueError(f"Domain '{domain}' not found. Available domains: {available_domains}")
    
    current_skills_lower = [skill.lower() for skill in current_skills]
    
    required_techs = []
    for tech in domains_dict[domain]:
        if tech.lower() not in current_skills_lower:
            required_techs.append(tech)
    
    if not required_techs:
        print(f"Great job! You already know all technologies for {domain}!")
        return [], {}
    
    courses = {
        "coursera": [],
        "udemy": [],
        "youtube": []
    }
    
    for tech in required_techs:
        try:
            response = model.generate_content(f"Get me the link to a course on {tech} from coursera and absolutely none of your text")
            courses["coursera"].append(response)
            
            response = model.generate_content(f"Get me a link a course on {tech} from udemy and absolutely none of your text")
            courses["udemy"].append(response)
            
            response = model.generate_content(f"Get me a link to the best {tech} tutorial on youtube in {language_preference} and absolutely none of your text")
            
            courses["youtube"].append(response)
        except Exception as e:
            print(f"Error getting resources for {tech}: {e}")
    
    return required_techs, courses

def display_learning_path(required_techs, courses):
    if not required_techs:
        return
    
    print("\n===== YOUR LEARNING PATH =====")
    print(f"Technologies to learn: {', '.join(required_techs)}")
    
    print("\n----- RECOMMENDED RESOURCES -----")
    for tech in required_techs:
        print(f"\n## {tech} ##")
        
        # Find corresponding resources
        coursera_item = next((item for item in courses["coursera"] if item["tech"] == tech), None)
        udemy_item = next((item for item in courses["udemy"] if item["tech"] == tech), None)
        youtube_item = next((item for item in courses["youtube"] if item["tech"] == tech), None)
        
        if coursera_item:
            print(f"Coursera: {coursera_item['link']}")
        if udemy_item:
            print(f"Udemy: {udemy_item['link']}")
        if youtube_item:
            print(f"YouTube: {youtube_item['link']}")

def main():
    print("Welcome to the Learning Path Generator!")
    print("Available domains:", ", ".join(domains_dict.keys()))
    
    # Get user inputs
    domain = input("Enter your desired domain: ")
    current_skills_input = input("Enter the technologies you already know (comma-separated): ")
    current_skills = [skill.strip() for skill in current_skills_input.split(",") if skill.strip()]
    language_preference = input("Preferred language for YouTube tutorials (English, Hindi, etc.): ")
    
    try:
        required_techs, courses = get_learning_resources(domain, current_skills, language_preference)
        display_learning_path(required_techs, courses)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()