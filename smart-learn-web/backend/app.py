"""
Smart Learning System - Backend API
Provides REST endpoints for course analysis, learning paths, quizzes, and progress tracking.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import random
import time
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend

# --- In-Memory Database (Simulated) ---
# In production, replace with SQLite/PostgreSQL
USER_DATA = {
    "profile": {
        "name": "Guest User",
        "level": "beginner",
        "goal": "job",
        "speed": "fast"
    },
    "progress": {},  # { topic: { completed_modules: [], quiz_scores: [], time_spent: 0 } }
    "weaknesses": []
}

# --- Core Intelligence Modules (Simplified for Demo) ---

def generate_curriculum(topic, level, goal):
    """Smart Course Analyzer & Adaptive Learning System"""
    base_modules = [
        {"id": 1, "title": f"Introduction to {topic}", "type": "theory", "priority": "high", "time": "15 min"},
        {"id": 2, "title": f"Core Concepts of {topic}", "type": "theory", "priority": "critical", "time": "30 min"},
        {"id": 3, "title": f"Practical Implementation", "type": "code", "priority": "critical", "time": "45 min"},
        {"id": 4, "title": f"Common Mistakes & Debugging", "type": "practice", "priority": "high", "time": "20 min"},
        {"id": 5, "title": f"Real-world Project: {topic} App", "type": "project", "priority": "critical", "time": "60 min"},
        {"id": 6, "title": f"Advanced Patterns in {topic}", "type": "theory", "priority": "medium", "time": "30 min"},
        {"id": 7, "title": f"Interview Questions: {topic}", "type": "quiz", "priority": "high", "time": "20 min"},
    ]
    
    # Adaptive Logic
    if level == "beginner":
        modules = [m for m in base_modules if m["priority"] != "low"]
        # Add ELI5 explanation
        modules.insert(0, {"id": 0, "title": "ELI5: What is " + topic + "?", "type": "eli5", "priority": "high", "time": "5 min"})
    elif level == "advanced":
        modules = [m for m in base_modules if m["priority"] in ["critical", "high"]]
        modules.append({"id": 8, "title": "System Design with " + topic, "type": "architecture", "priority": "high", "time": "45 min"})
    
    if goal == "interview":
        modules.append({"id": 9, "title": "Top 20 Interview Questions", "type": "interview", "priority": "critical", "time": "30 min"})
    
    return modules

def generate_code_examples(topic, mode="standard"):
    """Practical Learning Engine"""
    examples = {
        "Python": [
            {"title": "Data Cleaning", "code": "import pandas as pd\ndf = pd.read_csv('data.csv')\ndf.fillna(0)", "explanation": "Handles missing values instantly."},
            {"title": "API Call", "code": "import requests\nres = requests.get('https://api.example.com')\nprint(res.json())", "explanation": "Fetches data from web services."}
        ],
        "JavaScript": [
            {"title": "Async/Await", "code": "const data = await fetch('/api').then(r => r.json());\nconsole.log(data);", "explanation": "Modern way to handle asynchronous operations."},
            {"title": "Array Mapping", "code": "const doubled = numbers.map(n => n * 2);", "explanation": "Functional programming for list transformation."}
        ]
    }
    
    # Fallback generator if topic not in DB
    if topic not in examples:
        return [
            {"title": f"Basic Setup for {topic}", "code": f"# Initialize {topic}\nconst app = new {topic.replace(' ', '')}();\napp.start();", "explanation": "Standard boilerplate to get started."},
            {"title": f"Core Function in {topic}", "code": f"function process(input) {{\n  // Logic for {topic}\n  return input.transform();\n}}", "explanation": "Demonstrates the primary workflow."}
        ]
    
    if mode == "interview":
        return [{"title": "Coding Interview Question", "code": "# Solve this efficiently\ndef solution(arr):\n    return sorted(arr)[0]", "explanation": "Tests knowledge of complexity."}]
    
    return examples[topic]

def generate_quiz(topic, count=5):
    """Auto Quiz Generator"""
    questions = [
        {
            "question": f"What is the primary use of {topic}?",
            "options": ["Data Analysis", "Web Scraping", "General Purpose", "All of the above"],
            "answer": 3
        },
        {
            "question": "Which method is used to handle errors in most languages?",
            "options": ["try-catch", "if-else", "loop", "import"],
            "answer": 0
        },
        {
            "question": "What does 'O(1)' complexity mean?",
            "options": ["Linear time", "Constant time", "Quadratic time", "Logarithmic time"],
            "answer": 1
        },
        {
            "question": f"In {topic}, how do you typically install packages?",
            "options": ["pip install", "npm install", "Both A and B depending on lang", "download exe"],
            "answer": 2
        },
        {
            "question": "What is a variable?",
            "options": ["A storage container", "A function", "A loop", "A database"],
            "answer": 0
        }
    ]
    return random.sample(questions, min(count, len(questions)))

def analyze_weaknesses(quiz_results):
    """Weakness Detector"""
    weaknesses = []
    if quiz_results['score'] < 60:
        weaknesses.append("Fundamental Concepts")
    if quiz_results['time_taken'] > 120: # avg > 24s per question
        weaknesses.append("Speed & Recall")
    
    # Simple logic for demo
    if not weaknesses:
        weaknesses.append("None identified - Great job!")
    
    return weaknesses

def get_career_guidance(topic):
    """Career Mode"""
    return {
        "roles": [f"Junior {topic} Developer", f"Senior {topic} Engineer", f"{topic} Architect"],
        "salary_range": "$60k - $150k (varies by location)",
        "resume_points": [
            f"Built scalable applications using {topic}.",
            f"Optimized performance by 30% using advanced {topic} techniques.",
            "Collaborated in Agile teams to deliver features."
        ],
        "interview_questions": [
            f"Explain the event loop in {topic}.",
            f"How do you manage state in large {topic} applications?",
            "Describe a challenging bug you fixed."
        ]
    }

# --- API Routes ---

@app.route('/api/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        data = request.json
        USER_DATA['profile'].update(data)
        return jsonify({"success": True, "message": "Profile updated", "profile": USER_DATA['profile']})
    return jsonify(USER_DATA['profile'])

@app.route('/api/analyze', methods=['POST'])
def analyze_course():
    data = request.json
    topic = data.get('topic', 'General Programming')
    level = data.get('level', 'beginner')
    goal = data.get('goal', 'job')
    
    curriculum = generate_curriculum(topic, level, goal)
    code_examples = generate_code_examples(topic)
    career = get_career_guidance(topic)
    
    response = {
        "topic": topic,
        "curriculum": curriculum,
        "code_examples": code_examples,
        "career_guidance": career,
        "estimated_time": sum([int(m['time'].split()[0]) for m in curriculum]),
        "skip_recommendations": ["History of the language", "Complex installation steps", "Obsolete syntax"]
    }
    return jsonify(response)

@app.route('/api/quiz', methods=['POST'])
def take_quiz():
    data = request.json
    topic = data.get('topic', 'General')
    quiz = generate_quiz(topic)
    return jsonify({"quiz": quiz})

@app.route('/api/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.json
    score = data.get('score', 0)
    total = data.get('total', 5)
    time_taken = data.get('time_taken', 0)
    
    result = {"score": score, "total": total, "percentage": (score/total)*100, "time_taken": time_taken}
    weaknesses = analyze_weaknesses(result)
    
    # Update progress (simulated)
    topic = data.get('topic', 'General')
    if topic not in USER_DATA['progress']:
        USER_DATA['progress'][topic] = {"quizzes": [], "weaknesses": []}
    
    USER_DATA['progress'][topic]['quizzes'].append(result)
    USER_DATA['progress'][topic]['weaknesses'] = weaknesses
    
    return jsonify({"result": result, "weaknesses": weaknesses})

@app.route('/api/notes', methods=['POST'])
def get_notes():
    data = request.json
    topic = data.get('topic', 'General')
    mode = data.get('mode', 'short') # short, detailed, cheatsheet
    
    notes = {
        "short": f"### Quick Summary: {topic}\n- Key concept 1\n- Key concept 2\n- Practical usage",
        "detailed": f"## Comprehensive Guide to {topic}\n\n1. **Introduction**: Definition and history...\n2. **Syntax**: Basic rules...",
        "cheatsheet": f"| Command | Description |\n|---|---|\n| `init` | Start project |\n| `build` | Compile code |"
    }
    
    return jsonify({"notes": notes.get(mode, notes['short']), "mode": mode})

@app.route('/api/projects', methods=['GET'])
def get_projects():
    topic = request.args.get('topic', 'General')
    projects = [
        {
            "title": f"Build a {topic} Todo App",
            "difficulty": "Beginner",
            "steps": ["Setup env", "Create UI", "Add logic", "Save to local storage"],
            "technologies": [topic, "HTML/CSS"]
        },
        {
            "title": f"{topic} Data Dashboard",
            "difficulty": "Intermediate",
            "steps": ["Fetch API data", "Process with Pandas/JS", "Visualize with Charts", "Deploy"],
            "technologies": [topic, "Chart.js", "API"]
        },
        {
            "title": f"Full Stack {topic} Platform",
            "difficulty": "Advanced",
            "steps": ["Design DB", "Backend API", "Frontend Client", "Auth & Security", "CI/CD"],
            "technologies": [topic, "Node/Python", "React/Vue", "Docker"]
        }
    ]
    return jsonify({"projects": projects})

if __name__ == '__main__':
    print("🚀 Smart Learning System Backend Running on http://localhost:5000")
    app.run(debug=False, port=5000, host='0.0.0.0')
