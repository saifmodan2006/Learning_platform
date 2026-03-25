"""Adaptive Learning System - Customize learning path based on user profile"""

class AdaptiveLearning:
    def __init__(self):
        self.learning_styles = {
            'visual': 'Diagrams, charts, and visual examples',
            'auditory': 'Explanations and discussions',
            'kinesthetic': 'Hands-on practice and projects',
            'reading': 'Documentation and written guides'
        }
    
    def get_user_profile(self):
        """Interactive user profile collection"""
        print("\n📋 Let's customize your learning experience!")
        
        level = input("Your skill level? (beginner/intermediate/advanced): ").strip().lower()
        if level not in ['beginner', 'intermediate', 'advanced']:
            level = 'beginner'
        
        goal = input("Your main goal? (job/exam/project/hobby): ").strip().lower()
        if goal not in ['job', 'exam', 'project', 'hobby']:
            goal = 'job'
        
        speed = input("Preferred learning speed? (fast/normal/deep): ").strip().lower()
        if speed not in ['fast', 'normal', 'deep']:
            speed = 'fast'
        
        style = input("Learning style? (visual/practical/reading/mixed): ").strip().lower()
        if style not in ['visual', 'practical', 'reading', 'mixed']:
            style = 'mixed'
        
        time_per_day = input("Time available per day (minutes)? ").strip()
        try:
            time_per_day = int(time_per_day)
        except:
            time_per_day = 60
        
        return {
            'level': level,
            'goal': goal,
            'speed': speed,
            'style': style,
            'time_per_day': time_per_day
        }
    
    def create_path(self, course_data, user_profile):
        """Create adaptive learning path based on user profile"""
        modules = course_data['modules']
        level = user_profile.get('level', 'beginner')
        speed = user_profile.get('speed', 'fast')
        goal = user_profile.get('goal', 'job')
        
        # Adjust path based on level
        if level == 'beginner':
            # Include all modules, add more basics
            filtered_modules = [m for m in modules if m['priority'] != 'SKIP']
            self._add_beginner_friendly_notes(filtered_modules)
        elif level == 'intermediate':
            # Skip very basic modules
            filtered_modules = [m for m in modules if m['priority'] in ['CRITICAL', 'HIGH']]
        else:  # advanced
            # Only critical and advanced content
            filtered_modules = [m for m in modules if m['priority'] == 'CRITICAL']
        
        # Adjust based on speed
        if speed == 'fast':
            # Mark optional items as skip
            for module in filtered_modules:
                if module['priority'] == 'MEDIUM':
                    module['skip_suggestion'] = True
                else:
                    module['skip_suggestion'] = False
            # Reduce estimated times by 20%
            self._compress_timelines(filtered_modules, factor=0.8)
        elif speed == 'deep':
            # Include everything, add extra resources
            for module in filtered_modules:
                module['skip_suggestion'] = False
            self._expand_content(filtered_modules)
        else:  # normal
            for module in filtered_modules:
                module['skip_suggestion'] = False
        
        # Adjust based on goal
        if goal == 'job':
            self._prioritize_job_skills(filtered_modules)
        elif goal == 'exam':
            self._prioritize_exam_topics(filtered_modules)
        elif goal == 'project':
            self._prioritize_project_skills(filtered_modules)
        
        return filtered_modules
    
    def _add_beginner_friendly_notes(self, modules):
        """Add extra explanations for beginners"""
        for module in modules:
            module['extra_help'] = True
            module['analogies_included'] = True
            module['step_by_step'] = True
    
    def _compress_timelines(self, modules, factor=0.8):
        """Compress timelines for fast learning"""
        for module in modules:
            duration = module['duration']
            if isinstance(duration, str) and 'min' in duration:
                minutes = int(duration.replace('min', '').strip())
                new_minutes = max(10, int(minutes * factor))
                module['duration'] = f"{new_minutes} min"
    
    def _expand_content(self, modules):
        """Expand content for deep learning"""
        for module in modules:
            module['additional_resources'] = True
            module['advanced_topics'] = True
            module['practice_exercises'] = 5
    
    def _prioritize_job_skills(self, modules):
        """Reorder modules for job readiness"""
        # Move project and practical modules earlier
        modules.sort(key=lambda x: (
            0 if 'project' in x['title'].lower() else
            1 if x['priority'] == 'CRITICAL' else
            2 if x['priority'] == 'HIGH' else 3
        ))
    
    def _prioritize_exam_topics(self, modules):
        """Focus on exam-relevant topics"""
        # Prioritize theory and fundamentals
        for module in modules:
            if 'fundamental' in module['title'].lower() or 'basic' in module['title'].lower():
                module['exam_weight'] = 'high'
    
    def _prioritize_project_skills(self, modules):
        """Focus on project-building skills"""
        # Move hands-on modules first
        modules.sort(key=lambda x: (
            0 if 'project' in x['title'].lower() or 'build' in x['title'].lower() else
            1 if 'practical' in x['title'].lower() else
            2
        ))
    
    def generate_quiz(self, topic):
        """Generate quiz for a topic"""
        quizzes = {
            'python': {
                'questions': [
                    {'q': 'What is the output of print(2 ** 3)?', 'options': ['6', '8', '9', 'Error'], 'answer': '8'},
                    {'q': 'Which data type is immutable?', 'options': ['List', 'Dictionary', 'Tuple', 'Set'], 'answer': 'Tuple'},
                    {'q': 'How do you start a comment in Python?', 'options': ['//', '#', '/*', '--'], 'answer': '#'}
                ]
            },
            'javascript': {
                'questions': [
                    {'q': 'What does DOM stand for?', 'options': ['Data Object Model', 'Document Object Model', 'Digital Ordinance Model'], 'answer': 'Document Object Model'},
                    {'q': 'Which keyword declares a constant?', 'options': ['var', 'let', 'const', 'fixed'], 'answer': 'const'},
                    {'q': 'What is the result of 2 + "2"?', 'options': ['4', '22', 'NaN', 'Error'], 'answer': '22'}
                ]
            },
            'default': {
                'questions': [
                    {'q': 'What is the primary purpose of this topic?', 'options': ['Option A', 'Option B', 'Option C', 'Option D'], 'answer': 'Option A'},
                    {'q': 'Which tool is commonly used?', 'options': ['Tool X', 'Tool Y', 'Tool Z'], 'answer': 'Tool X'},
                    {'q': 'What is a key best practice?', 'options': ['Practice 1', 'Practice 2', 'Practice 3'], 'answer': 'Practice 1'}
                ]
            }
        }
        
        topic_lower = topic.lower()
        for key in quizzes:
            if key in topic_lower:
                return quizzes[key]
        
        return quizzes['default']
    
    def detect_weakness(self, user_answers):
        """Detect weaknesses based on quiz answers"""
        weaknesses = []
        
        if len(user_answers) == 0:
            return {'weaknesses': ['No data provided'], 'recommendations': ['Take a quiz to identify weak areas']}
        
        # Analyze answer patterns
        correct_count = sum(1 for ans in user_answers if ans.get('correct', False))
        accuracy = correct_count / len(user_answers)
        
        if accuracy < 0.5:
            weaknesses.append('Fundamental concepts need review')
        if accuracy < 0.8:
            weaknesses.append('Practice more problems')
        
        # Check specific topic weaknesses
        topics_missed = [ans['topic'] for ans in user_answers if not ans.get('correct', False)]
        if topics_missed:
            weaknesses.append(f'Focus on: {", ".join(set(topics_missed))}')
        
        recommendations = []
        if accuracy < 0.5:
            recommendations.append('Revisit beginner modules')
            recommendations.append('Use ELI5 mode for simpler explanations')
        if accuracy < 0.8:
            recommendations.append('Complete practice exercises')
            recommendations.append('Build a mini-project')
        
        recommendations.append('Take revision tests regularly')
        
        return {
            'accuracy': f'{accuracy * 100:.1f}%',
            'weaknesses': weaknesses,
            'recommendations': recommendations,
            'next_steps': 'Focus on weak areas before moving to advanced topics'
        }
