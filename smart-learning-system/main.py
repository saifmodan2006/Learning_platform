"""
Smart Learning System - Main Entry Point
Transforms any course into a fast, practical, job-ready learning ecosystem.
"""

import sys
from modules.analyzer import CourseAnalyzer
from modules.summarizer import AISummarizer
from modules.adaptive import AdaptiveLearning
from modules.practical import PracticalEngine
from modules.teacher import AITeacher
from modules.doubt import DoubtSolver
from modules.notes import NotesGenerator
from modules.revision import RevisionSystem
from modules.tracker import ProgressTracker
from modules.optimizer import SkipOptimizer
from modules.project import ProjectBuilder
from modules.career import CareerMode
from utils.config import SystemConfig

class SmartLearningSystem:
    def __init__(self):
        self.config = SystemConfig()
        self.analyzer = CourseAnalyzer()
        self.summarizer = AISummarizer()
        self.adaptive = AdaptiveLearning()
        self.practical = PracticalEngine()
        self.teacher = AITeacher()
        self.doubt_solver = DoubtSolver()
        self.notes_gen = NotesGenerator()
        self.revision = RevisionSystem()
        self.tracker = ProgressTracker()
        self.optimizer = SkipOptimizer()
        self.project_builder = ProjectBuilder()
        self.career = CareerMode()
        
    def process_course(self, input_source, user_profile=None):
        """Main pipeline to process any course input"""
        print("🚀 Smart Learning System Initialized")
        print("=" * 50)
        
        # Step 1: Analyze Course
        print("\n📊 Step 1: Analyzing Course Structure...")
        course_data = self.analyzer.analyze(input_source)
        
        # Step 2: Get User Profile for Adaptation
        if not user_profile:
            user_profile = self.adaptive.get_user_profile()
        
        # Step 3: Create Learning Path
        print("\n🎯 Step 2: Creating Adaptive Learning Path...")
        learning_path = self.adaptive.create_path(course_data, user_profile)
        
        # Step 4: Generate Summaries
        print("\n📝 Step 3: Generating Smart Summaries...")
        summaries = self.summarizer.summarize_modules(learning_path)
        
        # Step 5: Extract Practical Content
        print("\n💻 Step 4: Extracting Practical Examples...")
        practical_content = self.practical.extract_examples(course_data)
        
        # Step 6: Optimize (Skip Unnecessary)
        print("\n⚡ Step 5: Optimizing Content (Skipping Low-Value)...")
        optimized_path = self.optimizer.optimize(learning_path, user_profile)
        
        # Step 7: Generate Outputs
        print("\n📚 Step 6: Generating Complete Learning Package...")
        output_package = {
            'course_overview': course_data['overview'],
            'module_breakdown': optimized_path,
            'summaries': summaries,
            'practical_examples': practical_content,
            'notes': self.notes_gen.generate(summaries),
            'practice_tasks': self.practical.generate_tasks(practical_content),
            'mini_project': self.project_builder.suggest_project(course_data),
            'revision_plan': self.revision.create_plan(optimized_path),
            'career_guidance': self.career.generate_guidance(course_data),
            'skip_recommendations': self.optimizer.get_skip_list()
        }
        
        # Initialize Progress Tracker
        self.tracker.initialize_course(output_package)
        
        return output_package
    
    def explain_concept(self, concept, mode='normal'):
        """Explain any concept with different modes"""
        return self.teacher.explain(concept, mode)
    
    def solve_doubt(self, question):
        """Answer user questions"""
        return self.doubt_solver.answer(question)
    
    def get_quiz(self, topic):
        """Generate quiz for a topic"""
        return self.adaptive.generate_quiz(topic)
    
    def detect_weakness(self, user_answers):
        """Detect user weaknesses based on quiz answers"""
        return self.adaptive.detect_weakness(user_answers)

def main():
    """Interactive CLI for Smart Learning System"""
    system = SmartLearningSystem()
    
    print("\n🎓 SMART LEARNING SYSTEM v1.0")
    print("Transform Courses into Job-Ready Skills")
    print("=" * 50)
    
    while True:
        print("\nCommands:")
        print("  1. Process Course (YouTube/PDF/Topic)")
        print("  2. Explain Concept (ELI5/Interview/Coding)")
        print("  3. Ask Doubt")
        print("  4. Take Quiz")
        print("  5. Check Progress")
        print("  6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            source = input("Enter course URL, file path, or topic: ").strip()
            if not source:
                print("❌ No input provided!")
                continue
                
            print("\nQuick Setup:")
            level = input("Skill Level (beginner/intermediate/advanced): ").strip() or 'beginner'
            goal = input("Goal (job/exam/project): ").strip() or 'job'
            speed = input("Speed (fast/normal/deep): ").strip() or 'fast'
            
            user_profile = {
                'level': level,
                'goal': goal,
                'speed': speed
            }
            
            result = system.process_course(source, user_profile)
            
            # Display Results
            print("\n" + "=" * 50)
            print("✅ COURSE PROCESSED SUCCESSFULLY!")
            print("=" * 50)
            print(f"\n📋 Course: {result['course_overview']['title']}")
            print(f"⏱️  Estimated Time: {result['course_overview']['time_saved']}")
            print(f"📦 Modules: {len(result['module_breakdown'])}")
            print(f"🎯 Projects: {len(result['mini_project'])}")
            
            # Save to file
            import json
            with open('output_package.json', 'w') as f:
                json.dump(result, f, indent=2, default=str)
            print("\n💾 Full package saved to 'output_package.json'")
            
        elif choice == '2':
            concept = input("Enter concept to explain: ").strip()
            mode = input("Mode (eli5/interview/coding/normal): ").strip() or 'normal'
            explanation = system.explain_concept(concept, mode)
            print(f"\n🤖 Explanation:\n{explanation}")
            
        elif choice == '3':
            question = input("Ask your doubt: ").strip()
            answer = system.solve_doubt(question)
            print(f"\n💡 Answer:\n{answer}")
            
        elif choice == '4':
            topic = input("Enter topic for quiz: ").strip()
            quiz = system.get_quiz(topic)
            print(f"\n📝 Quiz for {topic}:")
            print(quiz)
            
        elif choice == '5':
            progress = system.tracker.get_progress()
            print(f"\n📊 Progress: {progress['completed']}/{progress['total']} modules")
            print(f"   Percentage: {progress['percentage']}%")
            
        elif choice == '6':
            print("\n👋 Happy Learning! Come back soon.")
            break
            
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
