"""Skip Optimization Engine - Detect unnecessary content and save time"""

class SkipOptimizer:
    def __init__(self):
        self.skip_criteria = {
            'beginner': self._beginner_skip_list,
            'intermediate': self._intermediate_skip_list,
            'advanced': self._advanced_skip_list
        }
    
    def optimize(self, learning_path, user_profile):
        """Optimize learning path by marking skippable content"""
        level = user_profile.get('level', 'beginner')
        speed = user_profile.get('speed', 'fast')
        goal = user_profile.get('goal', 'job')
        
        optimized_path = []
        skip_suggestions = []
        
        for module in learning_path:
            should_skip = self._should_skip(module, level, speed, goal)
            
            module_copy = module.copy()
            module_copy['recommended_action'] = 'skip' if should_skip else 'study'
            
            if should_skip:
                skip_suggestions.append({
                    'module': module['title'],
                    'reason': self._get_skip_reason(module, level, goal),
                    'time_saved': module.get('duration', 'Unknown')
                })
            
            optimized_path.append(module_copy)
        
        return optimized_path
    
    def _should_skip(self, module, level, speed, goal):
        """Determine if a module should be skipped"""
        title_lower = module.get('title', '').lower()
        priority = module.get('priority', 'MEDIUM')
        
        # Never skip CRITICAL modules
        if priority == 'CRITICAL':
            return False
        
        # Beginner-specific skips
        if level == 'beginner':
            if any(word in title_lower for word in ['advanced', 'optimization', 'internals', 'under the hood']):
                return True
        
        # Advanced users can skip basics
        if level == 'advanced':
            if any(word in title_lower for word in ['introduction', 'basics', 'fundamentals', 'what is']):
                return True
        
        # Fast mode: skip MEDIUM priority
        if speed == 'fast' and priority == 'MEDIUM':
            return True
        
        # Job-focused: skip heavy theory
        if goal == 'job':
            if any(word in title_lower for word in ['history', 'theory', 'academic', 'research']):
                return True
        
        # Exam-focused: don't skip much
        if goal == 'exam':
            return False
        
        return False
    
    def _get_skip_reason(self, module, level, goal):
        """Get reason for skipping"""
        title_lower = module.get('title', '').lower()
        
        if any(word in title_lower for word in ['history', 'introduction', 'overview']):
            return "Nice to know but not essential for practical skills"
        
        if any(word in title_lower for word in ['advanced', 'optimization']):
            return "Come back to this after mastering fundamentals"
        
        if any(word in title_lower for word in ['theory', 'academic']):
            return "Focus on practical application first"
        
        return "Low priority for your current goals"
    
    def get_skip_list(self):
        """Get general skip recommendations"""
        return {
            'general_skips': [
                {
                    'topic': 'Installation & Setup Videos (long)',
                    'reason': 'Use quick start guides or IDE defaults',
                    'time_saved': '30-60 min'
                },
                {
                    'topic': 'Historical Background',
                    'reason': 'Interesting but not practical',
                    'time_saved': '15-30 min'
                },
                {
                    'topic': 'Complex Mathematical Proofs',
                    'reason': 'Understand concept, skip derivations initially',
                    'time_saved': '45-90 min'
                },
                {
                    'topic': 'Every Single Library Function',
                    'reason': 'Learn common ones, Google the rest when needed',
                    'time_saved': '2-3 hours'
                },
                {
                    'topic': 'Legacy Methods (Deprecated)',
                    'reason': 'Focus on modern best practices',
                    'time_saved': '30-60 min'
                },
                {
                    'topic': 'Overly Complex Edge Cases',
                    'reason': 'Handle when you encounter them',
                    'time_saved': '1-2 hours'
                }
            ],
            'pro_tips': [
                'Skip installation tutorials - use documentation',
                'Don\'t memorize everything - learn to search effectively',
                'Focus on 20% of features used 80% of the time',
                'Build projects instead of watching endless tutorials',
                'Skip sections you already understand confidently'
            ]
        }
    
    def _beginner_skip_list(self):
        """Skip list for beginners"""
        return [
            'Advanced optimization techniques',
            'Internal implementation details',
            'Multiple approaches (learn one first)',
            'Legacy/deprecated features',
            'Complex design patterns'
        ]
    
    def _intermediate_skip_list(self):
        """Skip list for intermediate learners"""
        return [
            'Basic syntax tutorials',
            'Simple examples you already know',
            'Introductory concepts',
            'Hand-holding setup guides'
        ]
    
    def _advanced_skip_list(self):
        """Skip list for advanced learners"""
        return [
            'Fundamental concepts you master',
            'Basic tutorials',
            'Beginner projects',
            'Obvious best practices'
        ]
    
    def calculate_time_saved(self, original_path, optimized_path):
        """Calculate total time saved"""
        original_time = self._parse_total_time(original_path)
        optimized_time = self._parse_total_time(optimized_path)
        
        saved = original_time - optimized_time
        percentage = (saved / original_time * 100) if original_time > 0 else 0
        
        return {
            'original_minutes': original_time,
            'optimized_minutes': optimized_time,
            'saved_minutes': saved,
            'percentage_saved': round(percentage, 1)
        }
    
    def _parse_total_time(self, path):
        """Parse total time from path"""
        total = 0
        for module in path:
            duration = module.get('duration', '0 min')
            if isinstance(duration, str):
                try:
                    minutes = int(''.join(filter(str.isdigit, duration)))
                    total += minutes
                except:
                    pass
            elif isinstance(duration, (int, float)):
                total += duration
        return total
