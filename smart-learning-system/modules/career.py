"""Career Mode - Connect learning to real jobs"""

class CareerMode:
    def __init__(self):
        self.career_paths = {
            'python': self._python_career_path(),
            'javascript': self._js_career_path(),
            'data': self._data_career_path(),
            'web': self._web_career_path()
        }
    
    def generate_guidance(self, course_data):
        """Generate career guidance based on course"""
        title = course_data.get('overview', {}).get('title', '').lower()
        
        # Determine career path
        if 'python' in title:
            return self.career_paths['python']
        elif 'javascript' in title or 'react' in title:
            return self.career_paths['javascript']
        elif 'data' in title or 'analytics' in title:
            return self.career_paths['data']
        elif 'web' in title:
            return self.career_paths['web']
        else:
            return self._generic_career_path()
    
    def _python_career_path(self):
        return {
            'job_roles': [
                {
                    'title': 'Python Developer',
                    'experience': 'Entry Level',
                    'avg_salary': '$60k - $90k',
                    'key_skills': ['Python', 'Django/Flask', 'SQL', 'Git', 'REST APIs'],
                    'interview_focus': ['Data structures', 'Algorithms', 'Web frameworks']
                },
                {
                    'title': 'Backend Engineer',
                    'experience': 'Mid Level',
                    'avg_salary': '$90k - $130k',
                    'key_skills': ['Python', 'System Design', 'Databases', 'Cloud (AWS/GCP)'],
                    'interview_focus': ['System design', 'Scalability', 'Database optimization']
                },
                {
                    'title': 'DevOps Engineer',
                    'experience': 'Mid-Senior',
                    'avg_salary': '$100k - $150k',
                    'key_skills': ['Python', 'Docker', 'Kubernetes', 'CI/CD', 'Linux'],
                    'interview_focus': ['Automation', 'Infrastructure', 'Troubleshooting']
                }
            ],
            'resume_points': [
                'Built automation scripts saving X hours per week',
                'Developed REST API serving X requests/day',
                'Optimized database queries reducing response time by X%',
                'Implemented CI/CD pipeline reducing deployment time by X%'
            ],
            'portfolio_projects': [
                'Full-stack web application with user authentication',
                'Data pipeline processing large datasets',
                'Open-source library or contribution',
                'Automation tool solving real problem'
            ],
            'interview_questions': [
                'Explain Python decorators with examples',
                'Difference between list and tuple?',
                'How does garbage collection work in Python?',
                'Design a URL shortening service',
                'Optimize this slow database query'
            ]
        }
    
    def _js_career_path(self):
        return {
            'job_roles': [
                {
                    'title': 'Frontend Developer',
                    'experience': 'Entry Level',
                    'avg_salary': '$65k - $95k',
                    'key_skills': ['JavaScript', 'React/Vue', 'HTML/CSS', 'Git'],
                    'interview_focus': ['DOM manipulation', 'Component design', 'CSS']
                },
                {
                    'title': 'Full-Stack Developer',
                    'experience': 'Mid Level',
                    'avg_salary': '$95k - $140k',
                    'key_skills': ['JavaScript', 'Node.js', 'React', 'Databases', 'APIs'],
                    'interview_focus': ['Full-stack architecture', 'State management', 'Security']
                },
                {
                    'title': 'Senior Frontend Engineer',
                    'experience': 'Senior',
                    'avg_salary': '$130k - $180k',
                    'key_skills': ['JavaScript', 'Architecture', 'Performance', 'Mentoring'],
                    'interview_focus': ['System design', 'Performance optimization', 'Leadership']
                }
            ],
            'resume_points': [
                'Built responsive web app used by X users',
                'Improved page load time by X% through optimization',
                'Implemented state management for complex application',
                'Led migration from legacy code to modern framework'
            ],
            'portfolio_projects': [
                'E-commerce site with cart and checkout',
                'Real-time chat application',
                'Dashboard with data visualizations',
                'Progressive Web App (PWA)'
            ],
            'interview_questions': [
                'Explain closure with practical example',
                'Difference between let, const, and var',
                'How does event loop work?',
                'Optimize React component re-renders',
                'Design a infinite scroll feature'
            ]
        }
    
    def _data_career_path(self):
        return {
            'job_roles': [
                {
                    'title': 'Data Analyst',
                    'experience': 'Entry Level',
                    'avg_salary': '$60k - $85k',
                    'key_skills': ['SQL', 'Python/R', 'Excel', 'Tableau/PowerBI', 'Statistics'],
                    'interview_focus': ['SQL queries', 'Data interpretation', 'Case studies']
                },
                {
                    'title': 'Data Scientist',
                    'experience': 'Mid Level',
                    'avg_salary': '$100k - $150k',
                    'key_skills': ['Python', 'ML', 'Statistics', 'Deep Learning', 'Big Data'],
                    'interview_focus': ['ML algorithms', 'Case studies', 'Coding challenges']
                },
                {
                    'title': 'ML Engineer',
                    'experience': 'Mid-Senior',
                    'avg_salary': '$120k - $180k',
                    'key_skills': ['Python', 'TensorFlow/PyTorch', 'MLOps', 'Cloud', 'Scaling'],
                    'interview_focus': ['Model deployment', 'System design', 'Optimization']
                }
            ],
            'resume_points': [
                'Analyzed dataset of X records, uncovering insights that drove Y% revenue increase',
                'Built predictive model with X% accuracy',
                'Created automated dashboard used by X stakeholders daily',
                'Reduced data processing time from X hours to Y minutes'
            ],
            'portfolio_projects': [
                'End-to-end EDA on real-world dataset',
                'Machine learning model deployed to production',
                'Interactive dashboard with business insights',
                'Kaggle competition submission (top X%)'
            ],
            'interview_questions': [
                'How do you handle missing data?',
                'Explain bias-variance tradeoff',
                'Write SQL query for complex join',
                'Interpret this A/B test result',
                'Design recommendation system for X'
            ]
        }
    
    def _web_career_path(self):
        return {
            'job_roles': [
                {
                    'title': 'Web Developer',
                    'experience': 'Entry Level',
                    'avg_salary': '$55k - $80k',
                    'key_skills': ['HTML/CSS', 'JavaScript', 'Responsive Design', 'Git'],
                    'interview_focus': ['CSS layouts', 'JavaScript basics', 'Accessibility']
                },
                {
                    'title': 'Full-Stack Developer',
                    'experience': 'Mid Level',
                    'avg_salary': '$90k - $135k',
                    'key_skills': ['Frontend + Backend', 'Databases', 'APIs', 'Deployment'],
                    'interview_focus': ['Full-stack projects', 'Database design', 'Security']
                }
            ],
            'resume_points': [
                'Developed responsive website increasing mobile traffic by X%',
                'Built e-commerce platform processing $X in transactions',
                'Optimized website achieving 95+ Lighthouse score',
                'Integrated third-party APIs for enhanced functionality'
            ],
            'portfolio_projects': [
                'Portfolio website (your own!)',
                'Blog platform with CMS',
                'Social media clone',
                'SaaS landing page with payment integration'
            ],
            'interview_questions': [
                'Explain CSS box model',
                'Center a div horizontally and vertically',
                'Fetch API vs Axios - which and why?',
                'Secure against XSS and CSRF attacks',
                'Design URL structure for blog platform'
            ]
        }
    
    def _generic_career_path(self):
        return {
            'job_roles': [
                {
                    'title': 'Software Developer',
                    'experience': 'Entry Level',
                    'avg_salary': '$60k - $90k',
                    'key_skills': ['Programming', 'Problem Solving', 'Git', 'Testing'],
                    'interview_focus': ['Coding challenges', 'System design basics']
                }
            ],
            'resume_points': [
                'Built project solving real problem',
                'Learned new technology independently',
                'Contributed to open-source project',
                'Completed certification/course with hands-on projects'
            ],
            'portfolio_projects': [
                'Capstone project from course',
                'Personal project solving your own problem',
                'Contribution to open-source',
                'Clone of popular application'
            ],
            'interview_questions': [
                'Tell me about your learning journey',
                'Describe a challenging project',
                'How do you approach debugging?',
                'Explain a technical concept simply'
            ]
        }
    
    def get_salary_negotiation_tips(self):
        """Tips for salary negotiation"""
        return [
            'Research market rates for your role and location',
            'Know your minimum acceptable salary before interviewing',
            'Don\'t reveal current salary early in process',
            'Focus on value you bring, not personal needs',
            'Consider total compensation (benefits, equity, remote)',
            'Practice saying "I need to think about it"',
            'Get offers in writing before negotiating',
            'Be prepared to walk away if below minimum'
        ]
    
    def get_networking_advice(self):
        """Networking advice for job seekers"""
        return [
            'Build in public - share your learning journey',
            'Contribute to open-source projects',
            'Attend local meetups and conferences',
            'Connect with alumni from your bootcamp/courses',
            'Engage on LinkedIn and Twitter tech community',
            'Offer help before asking for favors',
            'Follow up after meetings with thank you notes',
            'Maintain relationships, don\'t just network when job hunting'
        ]
