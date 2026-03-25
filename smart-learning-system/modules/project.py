"""Project Builder Mode - Suggest and guide projects"""

class ProjectBuilder:
    def __init__(self):
        self.project_templates = {
            'python': self._get_python_projects(),
            'javascript': self._get_js_projects(),
            'data': self._get_data_projects(),
            'web': self._get_web_projects(),
            'default': self._get_generic_projects()
        }
    
    def suggest_project(self, course_data):
        """Suggest projects based on course content"""
        title = course_data.get('overview', {}).get('title', '').lower()
        
        # Determine project category
        if 'python' in title:
            return self.project_templates['python']
        elif 'javascript' in title or 'react' in title:
            return self.project_templates['javascript']
        elif 'data' in title or 'analytics' in title:
            return self.project_templates['data']
        elif 'web' in title:
            return self.project_templates['web']
        else:
            return self.project_templates['default']
    
    def get_project_guide(self, project_name):
        """Get detailed step-by-step guide for a project"""
        guides = self._get_all_guides()
        return guides.get(project_name.lower(), self._get_generic_guide())
    
    def _get_python_projects(self):
        return [
            {
                'id': 1,
                'name': 'Automation Script',
                'description': 'Automate a repetitive task on your computer',
                'difficulty': 'Beginner',
                'time_required': '2-3 hours',
                'skills_practiced': ['File handling', 'Loops', 'Functions', 'OS module'],
                'deliverable': 'Working script that saves you time daily'
            },
            {
                'id': 2,
                'name': 'Data Analysis Dashboard',
                'description': 'Analyze a dataset and create visualizations',
                'difficulty': 'Intermediate',
                'time_required': '4-6 hours',
                'skills_practiced': ['Pandas', 'Matplotlib', 'Data cleaning', 'Statistics'],
                'deliverable': 'Jupyter notebook with insights and charts'
            },
            {
                'id': 3,
                'name': 'REST API',
                'description': 'Build a backend API with CRUD operations',
                'difficulty': 'Intermediate',
                'time_required': '5-8 hours',
                'skills_practiced': ['Flask/FastAPI', 'Database', 'Authentication', 'Testing'],
                'deliverable': 'Deployed API with documentation'
            },
            {
                'id': 4,
                'name': 'Web Scraper',
                'description': 'Extract data from websites automatically',
                'difficulty': 'Intermediate',
                'time_required': '3-5 hours',
                'skills_practiced': ['BeautifulSoup', 'Requests', 'Data parsing', 'CSV/JSON'],
                'deliverable': 'Scraper that collects and saves data'
            }
        ]
    
    def _get_js_projects(self):
        return [
            {
                'id': 1,
                'name': 'Interactive To-Do List',
                'description': 'Build a feature-rich task manager',
                'difficulty': 'Beginner',
                'time_required': '3-4 hours',
                'skills_practiced': ['DOM manipulation', 'Event listeners', 'Local storage'],
                'deliverable': 'Working web app with add/delete/edit features'
            },
            {
                'id': 2,
                'name': 'Weather App',
                'description': 'Fetch and display weather data from API',
                'difficulty': 'Intermediate',
                'time_required': '4-6 hours',
                'skills_practiced': ['Async/await', 'Fetch API', 'Error handling', 'UI updates'],
                'deliverable': 'Live weather app with search functionality'
            },
            {
                'id': 3,
                'name': 'E-commerce Frontend',
                'description': 'Build a shopping interface with cart',
                'difficulty': 'Advanced',
                'time_required': '8-12 hours',
                'skills_practiced': ['React/Vue', 'State management', 'Routing', 'API integration'],
                'deliverable': 'Full-featured shopping UI'
            }
        ]
    
    def _get_data_projects(self):
        return [
            {
                'id': 1,
                'name': 'Exploratory Data Analysis',
                'description': 'Analyze a real-world dataset end-to-end',
                'difficulty': 'Beginner',
                'time_required': '3-5 hours',
                'skills_practiced': ['Pandas', 'Visualization', 'Statistics', 'Storytelling'],
                'deliverable': 'Complete EDA report with insights'
            },
            {
                'id': 2,
                'name': 'Predictive Model',
                'description': 'Build and deploy a machine learning model',
                'difficulty': 'Intermediate',
                'time_required': '6-10 hours',
                'skills_practiced': ['Scikit-learn', 'Model evaluation', 'Feature engineering'],
                'deliverable': 'Trained model with accuracy metrics'
            },
            {
                'id': 3,
                'name': 'Dashboard with Insights',
                'description': 'Create an interactive business dashboard',
                'difficulty': 'Advanced',
                'time_required': '8-12 hours',
                'skills_practiced': ['Plotly/Dash', 'Data pipelines', 'KPIs', 'Deployment'],
                'deliverable': 'Live dashboard with real-time data'
            }
        ]
    
    def _get_web_projects(self):
        return [
            {
                'id': 1,
                'name': 'Portfolio Website',
                'description': 'Build your personal portfolio site',
                'difficulty': 'Beginner',
                'time_required': '4-6 hours',
                'skills_practiced': ['HTML/CSS', 'Responsive design', 'Deployment'],
                'deliverable': 'Live portfolio website'
            },
            {
                'id': 2,
                'name': 'Blog Platform',
                'description': 'Full-stack blog with authentication',
                'difficulty': 'Intermediate',
                'time_required': '8-12 hours',
                'skills_practiced': ['Backend', 'Database', 'Auth', 'CRUD'],
                'deliverable': 'Deployed blog platform'
            },
            {
                'id': 3,
                'name': 'Real-time Chat App',
                'description': 'Chat application with WebSocket',
                'difficulty': 'Advanced',
                'time_required': '10-15 hours',
                'skills_practiced': ['WebSocket', 'Real-time', 'Database', 'Security'],
                'deliverable': 'Working chat application'
            }
        ]
    
    def _get_generic_projects(self):
        return [
            {
                'id': 1,
                'name': 'Capstone Project',
                'description': 'Apply everything you learned in one project',
                'difficulty': 'All levels',
                'time_required': '10-20 hours',
                'skills_practiced': ['All course concepts', 'Problem-solving', 'Deployment'],
                'deliverable': 'Portfolio-worthy project'
            }
        ]
    
    def _get_all_guides(self):
        """Return all project guides"""
        return {
            'automation script': self._automation_script_guide(),
            'to-do list': self._todo_list_guide(),
            'weather app': self._weather_app_guide(),
            'portfolio website': self._portfolio_guide()
        }
    
    def _get_generic_guide(self):
        return """📋 PROJECT GUIDE TEMPLATE

STEP 1: Planning (30 min)
- Define project scope
- List required features
- Sketch the architecture

STEP 2: Setup (30 min)
- Create project structure
- Install dependencies
- Set up version control

STEP 3: Core Implementation (2-4 hours)
- Build main functionality first
- Test as you go
- Don't aim for perfection

STEP 4: Polish (1 hour)
- Add error handling
- Improve UI/UX
- Write documentation

STEP 5: Deploy (30 min)
- Choose hosting platform
- Deploy your project
- Share with others!

💡 Tips:
- Start small, add features gradually
- Google is your friend
- Don't copy-paste without understanding
- Deploy early, iterate often"""
    
    def _automation_script_guide(self):
        return """🤖 AUTOMATION SCRIPT PROJECT GUIDE

Goal: Automate file organization

Steps:
1. Import os and shutil modules
2. Define source and destination folders
3. Loop through files in source folder
4. Categorize files by extension
5. Move files to appropriate folders
6. Add logging for tracking
7. Schedule with cron/task scheduler

Bonus: Add GUI with tkinter!"""
    
    def _todo_list_guide(self):
        return """✅ TO-DO LIST PROJECT GUIDE

Features to build:
1. Add new tasks
2. Mark tasks as complete
3. Delete tasks
4. Filter (all/active/completed)
5. Save to local storage

Tech stack: HTML, CSS, JavaScript

Steps:
1. Create HTML structure
2. Style with CSS
3. Add JS for interactivity
4. Implement localStorage
5. Deploy to Netlify/Vercel"""
    
    def _weather_app_guide(self):
        return """🌤️ WEATHER APP PROJECT GUIDE

API: OpenWeatherMap (free tier)

Features:
1. Search by city name
2. Display current weather
3. Show 5-day forecast
4. Handle errors gracefully

Steps:
1. Get API key
2. Create UI layout
3. Fetch weather data
4. Display results
5. Add loading states
6. Handle errors
7. Deploy!"""
    
    def _portfolio_guide(self):
        return """👤 PORTFOLIO WEBSITE GUIDE

Sections to include:
1. Hero section (intro)
2. About me
3. Skills
4. Projects
5. Contact

Tech: HTML, CSS, minimal JS

Steps:
1. Plan layout
2. Code sections one by one
3. Make it responsive
4. Add smooth scrolling
5. Optimize images
6. Deploy to GitHub Pages

Pro tip: Keep it simple and clean!"""
