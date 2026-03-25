"""Notes Generator - Create short notes, detailed notes, cheatsheets"""

class NotesGenerator:
    def __init__(self):
        self.note_types = ['short', 'detailed', 'cheatsheet', 'interview_qa']
    
    def generate(self, summaries):
        """Generate all types of notes from summaries"""
        notes = {
            'short_notes': self._generate_short_notes(summaries),
            'detailed_notes': self._generate_detailed_notes(summaries),
            'cheatsheet': self._generate_cheatsheet(summaries),
            'interview_qa': self._generate_interview_qa(summaries)
        }
        return notes
    
    def _generate_short_notes(self, summaries):
        """Generate concise revision notes"""
        short_notes = "📝 SHORT NOTES (5-Min Revision)\n" + "="*50 + "\n\n"
        
        for summary in summaries:
            title = summary.get('title', 'Topic')
            key_points = summary.get('key_points', [])[:3]  # Top 3 points
            
            short_notes += f"• {title}:\n"
            for point in key_points:
                short_notes += f"  - {point}\n"
            short_notes += "\n"
        
        return short_notes
    
    def _generate_detailed_notes(self, summaries):
        """Generate comprehensive study notes"""
        detailed_notes = "📚 DETAILED NOTES\n" + "="*50 + "\n\n"
        
        for i, summary in enumerate(summaries, 1):
            detailed_notes += f"MODULE {i}: {summary.get('title', 'Topic')}\n"
            detailed_notes += "-"*40 + "\n\n"
            
            # Key Points
            detailed_notes += "KEY CONCEPTS:\n"
            for point in summary.get('key_points', []):
                detailed_notes += f"✓ {point}\n"
            
            # Must Learn
            detailed_notes += "\nMUST LEARN:\n"
            for item in summary.get('must_learn', []):
                detailed_notes += f"  • {item}\n"
            
            # Real Life Example
            if 'real_life_example' in summary:
                detailed_notes += f"\n💡 REAL-LIFE EXAMPLE:\n  {summary['real_life_example']}\n"
            
            # Common Mistakes
            if 'common_mistakes' in summary:
                detailed_notes += f"\n⚠️  AVOID THESE MISTAKES:\n"
                for mistake in summary['common_mistakes']:
                    detailed_notes += f"  ✗ {mistake}\n"
            
            detailed_notes += "\n" + "="*50 + "\n\n"
        
        return detailed_notes
    
    def _generate_cheatsheet(self, summaries):
        """Generate quick reference cheatsheet"""
        cheatsheet = "🎯 QUICK CHEATSHEET\n" + "="*50 + "\n\n"
        
        cheatsheet += "SYNTAX REFERENCE:\n"
        cheatsheet += "-"*30 + "\n"
        
        # Generic cheatsheet entries (would be customized based on topic)
        cheatsheet += """
VARIABLES & DATA TYPES:
  x = 5              # Integer
  name = "John"      # String
  pi = 3.14          # Float
  active = True      # Boolean

CONTROL FLOW:
  if condition:
      # do something
  elif other:
      # do other
  else:
      # default

LOOPS:
  for item in items:
      print(item)
  
  while condition:
      # repeat

FUNCTIONS:
  def func(param=default):
      return param

ERROR HANDLING:
  try:
      risky_operation()
  except Error as e:
      handle(e)
  finally:
      cleanup()

DATA STRUCTURES:
  list = [1, 2, 3]           # Ordered, mutable
  tuple = (1, 2, 3)          # Ordered, immutable
  dict = {'key': 'value'}    # Key-value pairs
  set = {1, 2, 3}            # Unique items

FILE OPERATIONS:
  with open('file.txt', 'r') as f:
      content = f.read()
"""
        
        cheatsheet += "\n" + "="*50 + "\n"
        cheatsheet += "Pro Tip: Save this and keep it handy while coding!\n"
        
        return cheatsheet
    
    def _generate_interview_qa(self, summaries):
        """Generate interview questions and answers"""
        interview_qa = "💼 INTERVIEW Q&A PREPARATION\n" + "="*50 + "\n\n"
        
        interview_qa += """COMMON INTERVIEW QUESTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1: Explain [Core Concept] in simple terms.
A: Start with a simple definition, give a real-world analogy,
   then explain technical details with an example.

Q2: What's the difference between X and Y?
A: Compare them on:
   - Purpose/Use case
   - Performance
   - Syntax/Implementation
   - When to use which

Q3: How do you handle [Common Problem]?
A: Describe your approach:
   1. Understand the problem
   2. Consider multiple solutions
   3. Choose based on constraints
   4. Implement and test
   5. Optimize if needed

Q4: Tell me about a challenging project.
A: Use STAR method:
   - Situation: What was the context?
   - Task: What was your responsibility?
   - Action: What did you do?
   - Result: What was the outcome?

Q5: How do you stay updated with technology?
A: Mention:
   - Blogs/newsletters you follow
   - Projects you've built
   - Communities you're part of
   - Recent things you learned

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CODING INTERVIEW TIPS:
✓ Think aloud while solving
✓ Ask clarifying questions
✓ Start with brute force, then optimize
✓ Test with edge cases
✓ Discuss time/space complexity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BEHAVIORAL QUESTIONS:
• "Tell me about yourself" → 2-min elevator pitch
• "Why do you want to work here?" → Show research
• "What's your weakness?" → Show self-awareness + improvement
• "Where in 5 years?" → Show ambition aligned with company

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        return interview_qa
