"""AI Summarizer - Convert long content into key insights"""

class AISummarizer:
    def __init__(self):
        self.summary_templates = {
            'technical': self._technical_summary,
            'conceptual': self._conceptual_summary,
            'practical': self._practical_summary
        }
    
    def summarize_modules(self, learning_path):
        """Generate summaries for each module"""
        summaries = []
        for module in learning_path:
            summary = self._generate_module_summary(module)
            summaries.append(summary)
        return summaries
    
    def _generate_module_summary(self, module):
        """Generate smart summary for a module"""
        title = module['title']
        priority = module['priority']
        
        # Smart content based on module title keywords
        if 'python' in title.lower() or 'coding' in title.lower():
            return self._summarize_coding_module(module)
        elif 'data' in title.lower() or 'analytics' in title.lower():
            return self._summarize_data_module(module)
        elif 'web' in title.lower() or 'react' in title.lower() or 'javascript' in title.lower():
            return self._summarize_web_module(module)
        elif 'marketing' in title.lower():
            return self._summarize_marketing_module(module)
        else:
            return self._generic_summary(module)
    
    def _summarize_coding_module(self, module):
        return {
            'module_id': module['id'],
            'title': module['title'],
            'key_points': [
                'Understand core syntax and structure',
                'Learn best practices for clean code',
                'Master common patterns and anti-patterns',
                'Practice with real-world examples'
            ],
            'must_learn': [
                'Variable declaration and data types',
                'Control flow (if/else, loops)',
                'Functions and scope',
                'Error handling'
            ],
            'optional': [
                'Historical context',
                'Rare edge cases',
                'Complex theoretical proofs'
            ],
            'real_life_example': 'Think of functions like recipes - you define steps once and reuse them whenever needed.',
            'time_estimate': module['duration'],
            'difficulty': 'Medium' if module['priority'] == 'HIGH' else 'Hard' if module['priority'] == 'CRITICAL' else 'Easy'
        }
    
    def _summarize_data_module(self, module):
        return {
            'module_id': module['id'],
            'title': module['title'],
            'key_points': [
                'Data collection and cleaning techniques',
                'Exploratory data analysis (EDA)',
                'Statistical foundations',
                'Visualization best practices'
            ],
            'must_learn': [
                'Handling missing values',
                'Data transformation',
                'Aggregation functions',
                'Correlation vs causation'
            ],
            'optional': [
                'Advanced mathematical proofs',
                'Obscure statistical tests',
                'Legacy library functions'
            ],
            'real_life_example': 'Data cleaning is like washing vegetables before cooking - skip it and your results will be dirty!',
            'time_estimate': module['duration'],
            'difficulty': 'Medium'
        }
    
    def _summarize_web_module(self, module):
        return {
            'module_id': module['id'],
            'title': module['title'],
            'key_points': [
                'DOM manipulation techniques',
                'Event handling and user interaction',
                'Component-based architecture',
                'State management strategies'
            ],
            'must_learn': [
                'HTML/CSS fundamentals',
                'JavaScript ES6+ features',
                'Component lifecycle',
                'API integration'
            ],
            'optional': [
                'Browser compatibility quirks (old browsers)',
                'Complex build configurations',
                'Niche CSS tricks'
            ],
            'real_life_example': 'Components are like LEGO blocks - build small, reusable pieces and combine them to create anything.',
            'time_estimate': module['duration'],
            'difficulty': 'Medium'
        }
    
    def _summarize_marketing_module(self, module):
        return {
            'module_id': module['id'],
            'title': module['title'],
            'key_points': [
                'Target audience identification',
                'Channel selection strategy',
                'Content creation frameworks',
                'Analytics and optimization'
            ],
            'must_learn': [
                'SEO fundamentals',
                'Social media algorithms',
                'Conversion funnel optimization',
                'A/B testing methods'
            ],
            'optional': [
                'Outdated marketing theories',
                'Platform-specific quirks (frequently changing)',
                'Expensive tool dependencies'
            ],
            'real_life_example': 'Marketing is like fishing - you need the right bait (content), at the right place (channel), at the right time.',
            'time_estimate': module['duration'],
            'difficulty': 'Easy'
        }
    
    def _generic_summary(self, module):
        return {
            'module_id': module['id'],
            'title': module['title'],
            'key_points': [
                'Core concepts and fundamentals',
                'Practical applications',
                'Common pitfalls to avoid',
                'Best practices'
            ],
            'must_learn': [
                'Basic terminology',
                'Key principles',
                'Essential tools',
                'Hands-on practice'
            ],
            'optional': [
                'Advanced theory',
                'Historical background',
                'Edge cases'
            ],
            'real_life_example': 'Learning this is like building a house - start with a strong foundation before adding decorations.',
            'time_estimate': module['duration'],
            'difficulty': 'Medium'
        }
    
    def _technical_summary(self, content):
        """Summarize technical content"""
        return {
            'type': 'technical',
            'summary': content[:200] + '...' if len(content) > 200 else content,
            'key_takeaways': ['Technical point 1', 'Technical point 2'],
            'code_snippets': []
        }
    
    def _conceptual_summary(self, content):
        """Summarize conceptual content"""
        return {
            'type': 'conceptual',
            'summary': content[:200] + '...' if len(content) > 200 else content,
            'analogies': ['Simple analogy 1', 'Simple analogy 2'],
            'examples': []
        }
    
    def _practical_summary(self, content):
        """Summarize practical content"""
        return {
            'type': 'practical',
            'summary': content[:200] + '...' if len(content) > 200 else content,
            'steps': ['Step 1', 'Step 2', 'Step 3'],
            'exercises': []
        }
