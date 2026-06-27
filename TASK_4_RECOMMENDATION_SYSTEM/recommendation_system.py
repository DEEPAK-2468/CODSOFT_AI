career_paths = {
    1: ("Artificial Intelligence", [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist"
    ]),
    2: ("Software Development", [
        "Python Developer",
        "Backend Developer",
        "Full Stack Developer"
    ]),
    3: ("Web Development", [
        "Frontend Developer",
        "UI Developer",
        "Full Stack Developer"
    ]),
    4: ("Cybersecurity", [
        "Security Analyst",
        "Ethical Hacker",
        "Cybersecurity Engineer"
    ]),
    5: ("Design & Animation", [
        "3D Artist",
        "Animator",
        "VFX Artist"
    ])
}

print("=== Career Recommendation System ===")
print("\nChoose your area of interest:\n")

for key, value in career_paths.items():
    print(f"{key}. {value[0]}")

try:
    choice = int(input("\nEnter your choice: "))

    if choice in career_paths:
        print(f"\nRecommended Careers in {career_paths[choice][0]}:\n")

        for career in career_paths[choice][1]:
            print("•", career)

    else:
        print("Invalid Choice.")

except ValueError:
    print("Please enter a valid number.")