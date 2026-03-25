"""Course Analyzer - Break courses into structured modules"""

import re
from utils.config import SystemConfig

class CourseAnalyzer:
    def __init__(self):
        self.config = SystemConfig()
    
    def analyze(self, input_source):
        """Analyze course input and extract structure"""
        input_type = self._detect_input_type(input_source)
        
        if input_type == 'topic_keyword':
            return self._analyze_topic(input_source)
        elif input_type in ['youtube_url', 'youtube_playlist']:
            return self._analyze_youtube(input_source)
        elif input_type == 'pdf_file':
            return self._analyze_pdf(input_source)
        else:
            return self._analyze_generic(input_source)
    
    def _detect_input_type(self, source):
        """Detect type of input source"""
        if not source:
            return 'topic_keyword'
            
        if 'youtube.com' in source or 'youtu.be' in source:
            return 'youtube_url'
        elif source.endswith('.pdf'):
            return 'pdf_file'
        elif 'drive.google.com' in source:
            return 'google_drive'
        elif '://' in source:
            return 'course_url'
        else:
            return 'topic_keyword'
    
    def _analyze_topic(self, topic):
        """Generate structured curriculum for a topic"""
        # Smart curriculum generator based on topic
        curricula = {
            'python': self._get_python_curriculum(),
            'javascript': self._get_js_curriculum(),
            'data science': self._get_data_science_curriculum(),
            'machine learning': self._get_ml_curriculum(),
            'web development': self._get_web_dev_curriculum(),
            'react': self._get_react_curriculum(),
            'sql': self._get_sql_curriculum(),
            'digital marketing': self._get_marketing_curriculum()
        }
        
        # Fuzzy match topic to known curricula
        topic_lower = topic.lower()
        for key, curriculum in curricula.items():
            if key in topic_lower:
                return curriculum
        
        # Generic curriculum for unknown topics
        return self._get_generic_curriculum(topic)
    
    def _get_python_curriculum(self):
        return {
            'overview': {
                'title': 'Python Programming Mastery',
                'difficulty': 'Beginner to Advanced',
                'total_modules': 8,
                'estimated_time': '6 hours (Fast Track)',
                'time_saved': '20+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'Python Basics & Setup', 'priority': 'HIGH', 'duration': '30 min', 'skip': False},
                {'id': 2, 'title': 'Data Structures (Lists, Dicts, Sets)', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 3, 'title': 'Functions & Modules', 'priority': 'CRITICAL', 'duration': '40 min', 'skip': False},
                {'id': 4, 'title': 'File Handling & Error Management', 'priority': 'HIGH', 'duration': '35 min', 'skip': False},
                {'id': 5, 'title': 'OOP Concepts', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 6, 'title': 'Libraries (NumPy, Pandas)', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 7, 'title': 'API Integration', 'priority': 'MEDIUM', 'duration': '40 min', 'skip': False},
                {'id': 8, 'title': 'Mini Project: Build a Tool', 'priority': 'CRITICAL', 'duration': '90 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': ['Write clean Python code', 'Build automation scripts', 'Work with data', 'Create APIs']
        }
    
    def _get_js_curriculum(self):
        return {
            'overview': {
                'title': 'JavaScript Full-Stack Development',
                'difficulty': 'Beginner to Advanced',
                'total_modules': 9,
                'estimated_time': '8 hours (Fast Track)',
                'time_saved': '25+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'JS Fundamentals', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 2, 'title': 'DOM Manipulation', 'priority': 'CRITICAL', 'duration': '50 min', 'skip': False},
                {'id': 3, 'title': 'ES6+ Features', 'priority': 'HIGH', 'duration': '40 min', 'skip': False},
                {'id': 4, 'title': 'Async/Await & Promises', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 5, 'title': 'Node.js Basics', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 6, 'title': 'Express & APIs', 'priority': 'HIGH', 'duration': '55 min', 'skip': False},
                {'id': 7, 'title': 'React Fundamentals', 'priority': 'HIGH', 'duration': '60 min', 'skip': False},
                {'id': 8, 'title': 'State Management', 'priority': 'MEDIUM', 'duration': '45 min', 'skip': False},
                {'id': 9, 'title': 'Full-Stack Project', 'priority': 'CRITICAL', 'duration': '120 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': ['Build interactive websites', 'Create REST APIs', 'Develop full-stack apps']
        }
    
    def _get_data_science_curriculum(self):
        return {
            'overview': {
                'title': 'Data Science Bootcamp',
                'difficulty': 'Beginner to Intermediate',
                'total_modules': 7,
                'estimated_time': '7 hours (Fast Track)',
                'time_saved': '30+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'Python for Data Science', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 2, 'title': 'NumPy & Pandas Mastery', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 3, 'title': 'Data Cleaning Techniques', 'priority': 'CRITICAL', 'duration': '50 min', 'skip': False},
                {'id': 4, 'title': 'Data Visualization', 'priority': 'HIGH', 'duration': '45 min', 'skip': False},
                {'id': 5, 'title': 'Statistics Essentials', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 6, 'title': 'Machine Learning Basics', 'priority': 'HIGH', 'duration': '60 min', 'skip': False},
                {'id': 7, 'title': 'Capstone Project', 'priority': 'CRITICAL', 'duration': '90 min', 'skip': False}
            ],
            'prerequisites': ['Basic Python'],
            'outcomes': ['Analyze datasets', 'Create visualizations', 'Build ML models', 'Present insights']
        }
    
    def _get_ml_curriculum(self):
        return {
            'overview': {
                'title': 'Machine Learning A-Z',
                'difficulty': 'Intermediate to Advanced',
                'total_modules': 8,
                'estimated_time': '10 hours (Fast Track)',
                'time_saved': '40+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'ML Fundamentals & Math', 'priority': 'HIGH', 'duration': '60 min', 'skip': False},
                {'id': 2, 'title': 'Supervised Learning', 'priority': 'CRITICAL', 'duration': '75 min', 'skip': False},
                {'id': 3, 'title': 'Unsupervised Learning', 'priority': 'HIGH', 'duration': '60 min', 'skip': False},
                {'id': 4, 'title': 'Model Evaluation', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 5, 'title': 'Feature Engineering', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 6, 'title': 'Deep Learning Intro', 'priority': 'MEDIUM', 'duration': '60 min', 'skip': False},
                {'id': 7, 'title': 'ML Pipeline & Deployment', 'priority': 'HIGH', 'duration': '55 min', 'skip': False},
                {'id': 8, 'title': 'End-to-End ML Project', 'priority': 'CRITICAL', 'duration': '120 min', 'skip': False}
            ],
            'prerequisites': ['Python', 'Basic Statistics'],
            'outcomes': ['Build ML models', 'Deploy to production', 'Optimize performance']
        }
    
    def _get_web_dev_curriculum(self):
        return {
            'overview': {
                'title': 'Full-Stack Web Development',
                'difficulty': 'Beginner to Advanced',
                'total_modules': 10,
                'estimated_time': '12 hours (Fast Track)',
                'time_saved': '50+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'HTML5 & CSS3', 'priority': 'HIGH', 'duration': '60 min', 'skip': False},
                {'id': 2, 'title': 'Responsive Design', 'priority': 'HIGH', 'duration': '45 min', 'skip': False},
                {'id': 3, 'title': 'JavaScript DOM', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 4, 'title': 'Git & Version Control', 'priority': 'HIGH', 'duration': '30 min', 'skip': False},
                {'id': 5, 'title': 'Backend with Node.js', 'priority': 'CRITICAL', 'duration': '75 min', 'skip': False},
                {'id': 6, 'title': 'Databases (SQL & NoSQL)', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 7, 'title': 'React Framework', 'priority': 'HIGH', 'duration': '75 min', 'skip': False},
                {'id': 8, 'title': 'Authentication & Security', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 9, 'title': 'Testing & Debugging', 'priority': 'MEDIUM', 'duration': '40 min', 'skip': False},
                {'id': 10, 'title': 'Deployment & DevOps Basics', 'priority': 'HIGH', 'duration': '55 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': ['Build responsive websites', 'Create full-stack applications', 'Deploy to cloud']
        }
    
    def _get_react_curriculum(self):
        return {
            'overview': {
                'title': 'React.js Complete Guide',
                'difficulty': 'Beginner to Intermediate',
                'total_modules': 7,
                'estimated_time': '6 hours (Fast Track)',
                'time_saved': '20+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'React Fundamentals', 'priority': 'CRITICAL', 'duration': '50 min', 'skip': False},
                {'id': 2, 'title': 'Components & Props', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 3, 'title': 'State & Hooks', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 4, 'title': 'Routing (React Router)', 'priority': 'HIGH', 'duration': '40 min', 'skip': False},
                {'id': 5, 'title': 'Context API & State Management', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 6, 'title': 'API Integration', 'priority': 'HIGH', 'duration': '45 min', 'skip': False},
                {'id': 7, 'title': 'Build & Deploy React App', 'priority': 'CRITICAL', 'duration': '90 min', 'skip': False}
            ],
            'prerequisites': ['JavaScript Basics'],
            'outcomes': ['Build SPAs', 'Manage state efficiently', 'Deploy React apps']
        }
    
    def _get_sql_curriculum(self):
        return {
            'overview': {
                'title': 'SQL for Data Analysis',
                'difficulty': 'Beginner to Intermediate',
                'total_modules': 6,
                'estimated_time': '4 hours (Fast Track)',
                'time_saved': '15+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'SQL Basics & SELECT', 'priority': 'CRITICAL', 'duration': '35 min', 'skip': False},
                {'id': 2, 'title': 'Filtering & Sorting', 'priority': 'HIGH', 'duration': '30 min', 'skip': False},
                {'id': 3, 'title': 'Aggregations & GROUP BY', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 4, 'title': 'JOINs (INNER, LEFT, RIGHT)', 'priority': 'CRITICAL', 'duration': '50 min', 'skip': False},
                {'id': 5, 'title': 'Subqueries & CTEs', 'priority': 'HIGH', 'duration': '40 min', 'skip': False},
                {'id': 6, 'title': 'Real-World SQL Projects', 'priority': 'CRITICAL', 'duration': '80 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': ['Query databases', 'Analyze data', 'Create reports']
        }
    
    def _get_marketing_curriculum(self):
        return {
            'overview': {
                'title': 'Digital Marketing Mastery',
                'difficulty': 'Beginner to Intermediate',
                'total_modules': 7,
                'estimated_time': '5 hours (Fast Track)',
                'time_saved': '20+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'Marketing Fundamentals', 'priority': 'HIGH', 'duration': '40 min', 'skip': False},
                {'id': 2, 'title': 'SEO Essentials', 'priority': 'CRITICAL', 'duration': '50 min', 'skip': False},
                {'id': 3, 'title': 'Social Media Marketing', 'priority': 'HIGH', 'duration': '45 min', 'skip': False},
                {'id': 4, 'title': 'Content Marketing', 'priority': 'HIGH', 'duration': '40 min', 'skip': False},
                {'id': 5, 'title': 'Email Marketing', 'priority': 'MEDIUM', 'duration': '35 min', 'skip': False},
                {'id': 6, 'title': 'Google Ads & Analytics', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 7, 'title': 'Campaign Strategy Project', 'priority': 'CRITICAL', 'duration': '70 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': ['Run ad campaigns', 'Optimize SEO', 'Analyze metrics']
        }
    
    def _get_generic_curriculum(self, topic):
        """Generate generic curriculum for any topic"""
        return {
            'overview': {
                'title': f'{topic.title()} Complete Course',
                'difficulty': 'Beginner to Advanced',
                'total_modules': 6,
                'estimated_time': '5 hours (Fast Track)',
                'time_saved': '15+ hours vs traditional courses',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': f'{topic} Fundamentals', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 2, 'title': 'Core Concepts & Theory', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 3, 'title': 'Practical Applications', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 4, 'title': 'Advanced Techniques', 'priority': 'MEDIUM', 'duration': '50 min', 'skip': False},
                {'id': 5, 'title': 'Tools & Best Practices', 'priority': 'HIGH', 'duration': '45 min', 'skip': False},
                {'id': 6, 'title': 'Capstone Project', 'priority': 'CRITICAL', 'duration': '90 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': [f'Master {topic}', 'Build real projects', 'Job-ready skills']
        }
    
    def _analyze_youtube(self, url):
        """Placeholder for YouTube analysis (would use API in production)"""
        return {
            'overview': {
                'title': 'YouTube Course Analysis',
                'source': url,
                'difficulty': 'Auto-detected',
                'total_modules': 5,
                'estimated_time': '4 hours (Optimized)',
                'time_saved': '60% time reduction',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'Introduction & Setup', 'priority': 'HIGH', 'duration': '20 min', 'skip': False},
                {'id': 2, 'title': 'Core Concepts', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 3, 'title': 'Practical Examples', 'priority': 'CRITICAL', 'duration': '60 min', 'skip': False},
                {'id': 4, 'title': 'Advanced Topics', 'priority': 'MEDIUM', 'duration': '40 min', 'skip': False},
                {'id': 5, 'title': 'Project Implementation', 'priority': 'CRITICAL', 'duration': '75 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': ['Understand key concepts', 'Build projects', 'Skip unnecessary content']
        }
    
    def _analyze_pdf(self, filepath):
        """Placeholder for PDF analysis"""
        return {
            'overview': {
                'title': 'PDF Course Content',
                'source': filepath,
                'difficulty': 'Auto-detected',
                'total_modules': 6,
                'estimated_time': '5 hours (Optimized)',
                'time_saved': '50% time reduction',
                'job_ready': True
            },
            'modules': [
                {'id': 1, 'title': 'Chapter 1: Basics', 'priority': 'HIGH', 'duration': '30 min', 'skip': False},
                {'id': 2, 'title': 'Chapter 2: Core Principles', 'priority': 'CRITICAL', 'duration': '45 min', 'skip': False},
                {'id': 3, 'title': 'Chapter 3: Practical Guide', 'priority': 'CRITICAL', 'duration': '55 min', 'skip': False},
                {'id': 4, 'title': 'Chapter 4: Case Studies', 'priority': 'MEDIUM', 'duration': '40 min', 'skip': False},
                {'id': 5, 'title': 'Chapter 5: Advanced Topics', 'priority': 'HIGH', 'duration': '50 min', 'skip': False},
                {'id': 6, 'title': 'Exercises & Projects', 'priority': 'CRITICAL', 'duration': '80 min', 'skip': False}
            ],
            'prerequisites': [],
            'outcomes': ['Master content', 'Apply knowledge', 'Complete exercises']
        }
    
    def _analyze_generic(self, source):
        """Generic analyzer for any other source"""
        return self._get_generic_curriculum('Custom Topic')
