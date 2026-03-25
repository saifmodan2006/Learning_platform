# 🚀 Smart Learning System - Web Application

A full-stack web application that transforms traditional courses into fast, practical, and personalized learning experiences using AI.

## 🌟 Features

### Core Intelligence Modules
1. **Smart Course Analyzer** - Breaks courses into structured modules with priority detection
2. **Adaptive Learning System** - Customizes paths based on skill level and goals
3. **Practical Learning Engine** - Extracts and simplifies code examples
4. **AI Teacher Mode** - Explains concepts in simple language (ELI5, Interview, Coding modes)
5. **Weakness Detector** - Identifies weak areas via auto-generated quizzes
6. **Career Mode** - Provides job roles, salary info, and resume points
7. **Project Builder** - Suggests real-world projects with step-by-step guides
8. **Smart Notes Generator** - Creates short notes, detailed guides, and cheatsheets
9. **Progress Tracker** - Visual progress monitoring
10. **Skip Optimization** - Recommends what content to skip for maximum efficiency

### Game Changer Features
- 🧠 **ELI5 Mode** - Ultra-simple explanations
- ⚡ **2x Speed Learning** - Only critical concepts
- 🎯 **Interview Mode** - Focused Q&A preparation
- 💻 **Coding Mode** - Practical examples only
- 📊 **Auto Quiz Generator** - Instant knowledge testing

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Flask (REST API)
- Flask-CORS

**Frontend:**
- HTML5 / CSS3 (Modern Dark Theme)
- Vanilla JavaScript (No framework dependencies)
- Responsive Grid Layout

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd backend
pip install flask flask-cors
```

### 2. Run Backend Server
```bash
cd backend
python app.py
```
Server will start on `http://localhost:5000`

### 3. Open Frontend
Open `frontend/index.html` in your browser, or serve it:
```bash
# Option A: Simple Python server
cd frontend
python -m http.server 8080

# Then visit http://localhost:8080
```

## 📖 How to Use

1. **Enter Topic**: Type any subject (Python, React, Data Science, etc.)
2. **Set Profile**: Choose your level (Beginner/Intermediate/Advanced) and goal (Job/Project/Interview)
3. **Generate Path**: Click "Generate Smart Path" to get:
   - Optimized curriculum with time estimates
   - Practical code examples
   - Career guidance
   - Project ideas
4. **Take Quiz**: Test your knowledge and get weakness analysis
5. **View Notes**: Switch between Short, Cheatsheet, and Detailed modes

## 📁 Project Structure

```
smart-learn-web/
├── backend/
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # Single-page application
└── README.md               # This file
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/profile` | GET/POST | Manage user profile settings |
| `/api/analyze` | POST | Generate curriculum for a topic |
| `/api/quiz` | POST | Get auto-generated quiz questions |
| `/api/submit-quiz` | POST | Submit quiz and get weakness analysis |
| `/api/notes` | POST | Get notes in different formats |
| `/api/projects` | GET | Fetch project ideas for a topic |

## 🎨 UI Features

- **Dark Theme**: Easy on eyes for long learning sessions
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Interactive Cards**: Hover effects and smooth transitions
- **Real-time Feedback**: Loading spinners and instant updates
- **Priority Indicators**: Color-coded module importance

## 🔮 Future Enhancements

- [ ] User authentication & persistent database
- [ ] Video integration (YouTube API)
- [ ] PDF upload & parsing
- [ ] Voice learning mode
- [ ] Gamification (badges, streaks)
- [ ] Community discussion forums
- [ ] AI chatbot for doubt solving

## 📄 License

MIT License - Free to use and modify

---

**Made with ❤️ for faster, smarter learning!**
