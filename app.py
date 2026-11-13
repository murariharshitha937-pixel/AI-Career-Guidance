from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

CAREERS = [
    {
        "name": "AI Engineer",
        "description": "Build intelligent applications using artificial intelligence.",
        "interests": ["AI", "Coding", "Mathematics", "Technology"],
        "skills": ["Python", "Machine Learning", "Deep Learning", "Mathematics"],
        "certifications": ["Google AI Essentials", "Machine Learning Specialization"],
        "resources": [
            {"name": "Google AI Learning", "url": "https://ai.google/"},
            {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn"}
        ],
        "roadmap": ["Learn Python", "Study Mathematics", "Learn Machine Learning", "Build AI Projects"]
    },
    {
        "name": "Data Scientist",
        "description": "Analyze data and discover useful insights.",
        "interests": ["Data", "Mathematics", "Coding", "Research"],
        "skills": ["Python", "Statistics", "SQL", "Data Visualization"],
        "certifications": ["IBM Data Science", "Google Data Analytics"],
        "resources": [
            {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn"},
            {"name": "NPTEL", "url": "https://nptel.ac.in/"}
        ],
        "roadmap": ["Learn Python", "Study Statistics", "Learn SQL", "Practice Data Analysis"]
    },
    {
        "name": "Web Developer",
        "description": "Create websites and interactive web applications.",
        "interests": ["Coding", "Design", "Technology", "Creativity"],
        "skills": ["HTML", "CSS", "JavaScript", "React"],
        "certifications": ["Meta Front-End Developer", "freeCodeCamp Certification"],
        "resources": [
            {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/"},
            {"name": "MDN Web Docs", "url": "https://developer.mozilla.org/"}
        ],
        "roadmap": ["Learn HTML", "Learn CSS", "Master JavaScript", "Build Websites"]
    },
    {
        "name": "Cybersecurity Analyst",
        "description": "Protect computer systems, networks and information.",
        "interests": ["Security", "Technology", "Problem Solving", "Networking"],
        "skills": ["Networking", "Linux", "Cybersecurity Basics", "Python"],
        "certifications": ["Google Cybersecurity Certificate", "CompTIA Security+"],
        "resources": [
            {"name": "Cisco Networking Academy", "url": "https://www.netacad.com/"},
            {"name": "TryHackMe", "url": "https://tryhackme.com/"}
        ],
        "roadmap": ["Learn Networking", "Understand Linux", "Study Security Basics", "Practice in Legal Labs"]
    },
    {
        "name": "Software Developer",
        "description": "Design and develop software applications.",
        "interests": ["Coding", "Technology", "Problem Solving", "Mathematics"],
        "skills": ["Python", "Java", "Data Structures", "Problem Solving"],
        "certifications": ["Oracle Java Certification", "freeCodeCamp Certification"],
        "resources": [
            {"name": "GeeksforGeeks", "url": "https://www.geeksforgeeks.org/"},
            {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/"}
        ],
        "roadmap": ["Learn Programming", "Study Data Structures", "Practice Algorithms", "Build Applications"]
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    interests = data.get("interests", [])
    skills = data.get("skills", [])

    if not interests:
        return jsonify({"error": "Please select at least one interest."}), 400

    results = []

    for career in CAREERS:
        interest_matches = len(
            set(interests) & set(career["interests"])
        )

        skill_matches = len(
            set(skills) & set(career["skills"])
        )

        total_possible = len(career["interests"]) + len(career["skills"])

        score = round(
            (interest_matches + skill_matches) / total_possible * 100
        )

        results.append({
            **career,
            "match": score
        })

    results.sort(key=lambda x: x["match"], reverse=True)

    return jsonify({
        "recommendations": results[:3]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)