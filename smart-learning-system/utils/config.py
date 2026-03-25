"""System Configuration and Constants"""

class SystemConfig:
    def __init__(self):
        # Learning Modes
        self.MODES = {
            'ELI5': 'Explain Like I\'m 5',
            'INTERVIEW': 'Interview Focused',
            'CODING': 'Only Coding',
            'FAST': '2x Speed Learning',
            'NORMAL': 'Standard Learning',
            'DEEP': 'Comprehensive Deep Dive'
        }
        
        # Priority Levels
        self.PRIORITY = {
            'CRITICAL': 1,
            'HIGH': 2,
            'MEDIUM': 3,
            'LOW': 4,
            'SKIP': 5
        }
        
        # Default Settings
        self.DEFAULT_PROFILE = {
            'level': 'beginner',
            'goal': 'job',
            'speed': 'fast',
            'learning_style': 'practical'
        }
        
        # Revision Intervals (in days)
        self.REVISION_SCHEDULE = {
            'quick': 0,      # Same day
            'day_1': 1,
            'day_3': 3,
            'week_1': 7,
            'exam': -1       # Custom date
        }
        
        # Supported Input Types
        self.SUPPORTED_INPUTS = [
            'youtube_url',
            'youtube_playlist',
            'google_drive',
            'pdf_file',
            'video_file',
            'topic_keyword',
            'course_url'
        ]
        
    def get_mode_description(self, mode):
        return self.MODES.get(mode.upper(), 'Unknown mode')
    
    def get_priority_value(self, priority):
        return self.PRIORITY.get(priority.upper(), 3)
