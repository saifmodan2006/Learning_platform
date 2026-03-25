"""Progress Tracker - Track completed modules and show progress"""

import json
from datetime import datetime

class ProgressTracker:
    def __init__(self):
        self.progress_file = 'progress.json'
        self.current_course = None
    
    def initialize_course(self, course_package):
        """Initialize tracking for a new course"""
        self.current_course = {
            'title': course_package['course_overview'].get('title', 'Unknown Course'),
            'started_at': datetime.now().isoformat(),
            'modules': [],
            'completed_modules': [],
            'quiz_scores': [],
            'time_spent': 0
        }
        
        # Initialize all modules as not started
        for module in course_package['module_breakdown']:
            self.current_course['modules'].append({
                'id': module.get('id', 0),
                'title': module.get('title', 'Module'),
                'status': 'not_started',  # not_started, in_progress, completed
                'started_at': None,
                'completed_at': None,
                'notes': ''
            })
        
        self._save_progress()
        return self.current_course
    
    def start_module(self, module_id):
        """Mark a module as in progress"""
        for module in self.current_course['modules']:
            if module['id'] == module_id:
                module['status'] = 'in_progress'
                module['started_at'] = datetime.now().isoformat()
                break
        
        self._save_progress()
        return True
    
    def complete_module(self, module_id):
        """Mark a module as completed"""
        for module in self.current_course['modules']:
            if module['id'] == module_id:
                module['status'] = 'completed'
                module['completed_at'] = datetime.now().isoformat()
                
                if module_id not in self.current_course['completed_modules']:
                    self.current_course['completed_modules'].append(module_id)
                break
        
        self._save_progress()
        return True
    
    def add_quiz_score(self, score):
        """Record quiz score"""
        self.current_course['quiz_scores'].append({
            'score': score,
            'timestamp': datetime.now().isoformat()
        })
        self._save_progress()
    
    def add_time_spent(self, minutes):
        """Add time spent learning"""
        self.current_course['time_spent'] += minutes
        self._save_progress()
    
    def get_progress(self):
        """Get current progress statistics"""
        if not self.current_course:
            return {
                'completed': 0,
                'total': 0,
                'percentage': 0.0,
                'status': 'No course loaded'
            }
        
        total = len(self.current_course['modules'])
        completed = len(self.current_course['completed_modules'])
        percentage = (completed / total * 100) if total > 0 else 0
        
        # Calculate average quiz score
        avg_quiz_score = 0
        if self.current_course['quiz_scores']:
            scores = [q['score'] for q in self.current_course['quiz_scores']]
            avg_quiz_score = sum(scores) / len(scores)
        
        return {
            'course_title': self.current_course['title'],
            'started_at': self.current_course['started_at'],
            'completed': completed,
            'total': total,
            'percentage': round(percentage, 1),
            'in_progress': len([m for m in self.current_course['modules'] if m['status'] == 'in_progress']),
            'not_started': len([m for m in self.current_course['modules'] if m['status'] == 'not_started']),
            'average_quiz_score': round(avg_quiz_score, 1),
            'time_spent_minutes': self.current_course['time_spent'],
            'status': 'In Progress' if completed < total else 'Completed!'
        }
    
    def get_next_module(self):
        """Get the next module to study"""
        for module in self.current_course['modules']:
            if module['status'] == 'not_started':
                return module
            elif module['status'] == 'in_progress':
                return module
        return None
    
    def get_module_status(self, module_id):
        """Get status of a specific module"""
        for module in self.current_course['modules']:
            if module['id'] == module_id:
                return module['status']
        return 'unknown'
    
    def _save_progress(self):
        """Save progress to file"""
        try:
            with open(self.progress_file, 'w') as f:
                json.dump(self.current_course, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save progress: {e}")
    
    def load_progress(self):
        """Load progress from file"""
        try:
            with open(self.progress_file, 'r') as f:
                self.current_course = json.load(f)
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Error loading progress: {e}")
            return False
    
    def reset_progress(self):
        """Reset all progress"""
        self.current_course = None
        try:
            with open(self.progress_file, 'w') as f:
                json.dump({}, f)
        except:
            pass
        return True
    
    def generate_report(self):
        """Generate a progress report"""
        progress = self.get_progress()
        
        report = "📊 LEARNING PROGRESS REPORT\n"
        report += "="*50 + "\n\n"
        report += f"Course: {progress.get('course_title', 'N/A')}\n"
        report += f"Status: {progress['status']}\n"
        report += f"Started: {progress.get('started_at', 'N/A')[:10] if progress.get('started_at') else 'N/A'}\n\n"
        
        report += "PROGRESS:\n"
        report += "-"*30 + "\n"
        report += f"Modules Completed: {progress['completed']}/{progress['total']}\n"
        report += f"Progress: {progress['percentage']}%\n"
        
        # Visual progress bar
        bar_length = 20
        filled = int(bar_length * progress['percentage'] / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        report += f"[{bar}] {progress['percentage']}%\n\n"
        
        report += f"Average Quiz Score: {progress['average_quiz_score']}%\n"
        report += f"Time Spent: {progress['time_spent_minutes']} minutes\n\n"
        
        if progress['percentage'] < 30:
            report += "💪 Keep going! You're just getting started.\n"
        elif progress['percentage'] < 60:
            report += "🚀 Great progress! You're halfway there.\n"
        elif progress['percentage'] < 90:
            report += "🔥 Almost done! Finish strong!\n"
        else:
            report += "🎉 Congratulations! You've mastered this course!\n"
        
        return report
