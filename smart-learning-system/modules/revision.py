"""Revision System - Create revision plans for different schedules"""

from utils.config import SystemConfig

class RevisionSystem:
    def __init__(self):
        self.config = SystemConfig()
    
    def create_plan(self, modules):
        """Create comprehensive revision plan"""
        plan = {
            'quick_revision': self._create_quick_revision(modules),
            'one_day_revision': self._create_one_day_revision(modules),
            'exam_revision': self._create_exam_revision(modules),
            'spaced_repetition': self._create_spaced_repetition(modules)
        }
        return plan
    
    def _create_quick_revision(self, modules):
        """5-minute quick revision plan"""
        revision = "⚡ 5-MINUTE QUICK REVISION\n" + "="*50 + "\n\n"
        revision += "Perfect for: Daily review before starting new content\n\n"
        
        for i, module in enumerate(modules[:5], 1):  # Top 5 modules
            revision += f"{i}. {module['title']}\n"
            revision += f"   → Remember: Key concept in one line\n"
            revision += f"   → Time: 1 min\n\n"
        
        revision += "💡 Tip: Focus on concepts you use most often!\n"
        return revision
    
    def _create_one_day_revision(self, modules):
        """1-day comprehensive revision plan"""
        revision = "📅 1-DAY REVISION PLAN\n" + "="*50 + "\n\n"
        revision += "Perfect for: Weekend review or before interviews\n\n"
        
        total_modules = len(modules)
        time_per_module = 30  # minutes
        
        revision += "MORNING SESSION (2 hours):\n"
        revision += "-"*30 + "\n"
        for module in modules[:total_modules//2]:
            revision += f"• {module['title']} ({time_per_module} min)\n"
            revision += f"  - Review key concepts\n"
            revision += f"  - Solve 1-2 practice problems\n\n"
        
        revision += "\nAFTERNOON SESSION (2 hours):\n"
        revision += "-"*30 + "\n"
        for module in modules[total_modules//2:]:
            revision += f"• {module['title']} ({time_per_module} min)\n"
            revision += f"  - Review key concepts\n"
            revision += f"  - Solve 1-2 practice problems\n\n"
        
        revision += "\nEVENING SESSION (1 hour):\n"
        revision += "-"*30 + "\n"
        revision += "• Take a mock test (30 min)\n"
        revision += "• Review mistakes (30 min)\n"
        
        return revision
    
    def _create_exam_revision(self, modules):
        """Exam-focused revision plan"""
        revision = "🎯 EXAM-FOCUSED REVISION PLAN\n" + "="*50 + "\n\n"
        revision += "Perfect for: Before certifications or technical tests\n\n"
        
        revision += "PRIORITY ORDER:\n"
        revision += "-"*30 + "\n"
        
        # Sort by priority
        critical = [m for m in modules if m.get('priority') == 'CRITICAL']
        high = [m for m in modules if m.get('priority') == 'HIGH']
        medium = [m for m in modules if m.get('priority') == 'MEDIUM']
        
        revision += "\n🔴 CRITICAL (Must Know - 60% of time):\n"
        for module in critical:
            revision += f"  ✓ {module['title']}\n"
        
        revision += "\n🟠 HIGH PRIORITY (Should Know - 30% of time):\n"
        for module in high:
            revision += f"  ✓ {module['title']}\n"
        
        revision += "\n🟡 MEDIUM (Nice to Know - 10% of time):\n"
        for module in medium:
            revision += f"  ✓ {module['title']}\n"
        
        revision += "\n\nEXAM STRATEGY:\n"
        revision += "-"*30 + "\n"
        revision += "1. Start with questions you know\n"
        revision += "2. Mark difficult ones and return later\n"
        revision += "3. Manage time: Don't spend too long on one question\n"
        revision += "4. Read questions carefully\n"
        revision += "5. Review answers if time permits\n"
        
        return revision
    
    def _create_spaced_repetition(self, modules):
        """Spaced repetition schedule for long-term retention"""
        revision = "🔄 SPACED REPETITION SCHEDULE\n" + "="*50 + "\n\n"
        revision += "Perfect for: Long-term memory retention\n\n"
        
        revision += "REVISION TIMELINE:\n"
        revision += "-"*30 + "\n\n"
        
        revision += "Day 0 (Today): Learn the concept\n"
        revision += "  → Study module thoroughly\n"
        revision += "  → Take notes\n"
        revision += "  → Do practice exercises\n\n"
        
        revision += "Day 1 (Tomorrow): First Review\n"
        revision += "  → Quick 10-min review of notes\n"
        revision += "  → Re-solve one problem\n"
        revision += "  → Teach it to someone (or rubber duck)\n\n"
        
        revision += "Day 3: Second Review\n"
        revision += "  → 15-min review\n"
        revision += "  → Try harder problems\n"
        revision += "  → Connect with other concepts\n\n"
        
        revision += "Day 7: Third Review\n"
        revision += "  → 20-min review\n"
        revision += "  → Build something with it\n"
        revision += "  → Explain without notes\n\n"
        
        revision += "Day 14: Fourth Review\n"
        revision += "  → Quick refresher\n"
        revision += "  → Interview-style questions\n\n"
        
        revision += "Day 30: Final Review\n"
        revision += "  → Should be solid now!\n"
        revision += "  → Just occasional practice\n\n"
        
        revision += "💡 SCIENCE BEHIND IT:\n"
        revision += "Spaced repetition exploits the psychological spacing effect.\n"
        revision += "Reviewing at increasing intervals strengthens memory traces.\n"
        
        return revision
