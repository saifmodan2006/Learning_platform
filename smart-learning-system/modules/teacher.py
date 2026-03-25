"""AI Teacher Mode - Explain concepts like a human teacher"""

class AITeacher:
    def __init__(self):
        self.explanation_modes = {
            'eli5': self._explain_like_5,
            'interview': self._interview_mode,
            'coding': self._coding_mode,
            'normal': self._normal_explanation,
            'analogy': self._analogy_mode
        }
    
    def explain(self, concept, mode='normal'):
        """Explain concept in specified mode"""
        mode_func = self.explanation_modes.get(mode.lower(), self._normal_explanation)
        return mode_func(concept)
    
    def _explain_like_5(self, concept):
        """Ultra-simple explanation for beginners"""
        explanations = {
            'variable': 'A variable is like a labeled box where you can store things. You write a name on the box (like "age") and put something inside (like 25).',
            'function': 'A function is like a recipe. You write down the steps once, and whenever you want to make that dish, you just follow the recipe instead of figuring it out again.',
            'loop': 'A loop is like doing push-ups. Instead of saying "do one push-up" ten times, you say "do 10 push-ups" and your body repeats the same action.',
            'array': 'An array is like an egg carton. It holds multiple items (eggs) in organized slots, and you can count them or pick specific ones.',
            'object': 'An object is like a character card in a game. It has properties (name, strength, color) and actions (attack, defend, run).',
            'api': 'An API is like a waiter in a restaurant. You tell the waiter what you want (request), they go to the kitchen (server), and bring back your food (response).',
            'database': 'A database is like a super-organized library. Instead of books, it stores information, and you can find exactly what you need really fast.',
            'class': 'A class is like a blueprint for a house. The blueprint itself isn\'t a house, but you can use it to build many houses that look similar.',
            'recursion': 'Recursion is like Russian nesting dolls. Each doll contains a smaller version of itself, until you reach the tiniest one.',
            'algorithm': 'An algorithm is like a treasure map. It\'s a step-by-step set of instructions to find the treasure (solve the problem).'
        }
        
        concept_lower = concept.lower()
        for key in explanations:
            if key in concept_lower:
                return f"🧒 ELI5 Explanation:\n\n{explanations[key]}\n\nThink about it next time you see this in real life!"
        
        return f"🧒 ELI5 Explanation:\n\nImagine {concept} is like a tool in a toolbox. You don't need to know how it's made, just when and how to use it to fix things!\n\nLet me know if you want a more specific example."
    
    def _interview_mode(self, concept):
        """Interview-focused explanation with Q&A"""
        interviews = {
            'python': {
                'common_questions': [
                    {'q': 'What is the difference between list and tuple?', 'a': 'Lists are mutable (can change), tuples are immutable (cannot change). Tuples are faster and used for fixed data.'},
                    {'q': 'Explain decorators.', 'a': 'Decorators are functions that modify other functions without changing their code. They start with @ symbol.'},
                    {'q': 'What is GIL?', 'a': 'Global Interpreter Lock - allows only one thread to execute Python bytecode at a time.'}
                ],
                'tips': ['Focus on practical examples', 'Mention time complexity', 'Show problem-solving approach']
            },
            'javascript': {
                'common_questions': [
                    {'q': 'Difference between let, const, and var?', 'a': 'var is function-scoped, let/const are block-scoped. const cannot be reassigned.'},
                    {'q': 'What is closure?', 'a': 'A closure is a function that remembers its outer variables even when called outside that scope.'},
                    {'q': 'Explain event loop.', 'a': 'Event loop handles async operations by moving callbacks from task queue to call stack when stack is empty.'}
                ],
                'tips': ['Understand hoisting', 'Know promises deeply', 'Practice DOM questions']
            },
            'data science': {
                'common_questions': [
                    {'q': 'How do you handle missing data?', 'a': 'Options: drop rows, fill with mean/median, predict values, or use algorithms that handle missing data.'},
                    {'q': 'Explain overfitting.', 'a': 'Model performs well on training data but poorly on new data. Prevent with cross-validation, regularization, more data.'},
                    {'q': 'What is p-value?', 'a': 'Probability of observing results as extreme as yours if null hypothesis is true. <0.05 typically means significant.'}
                ],
                'tips': ['Know your projects inside-out', 'Explain business impact', 'Show statistical thinking']
            }
        }
        
        concept_lower = concept.lower()
        for key in interviews:
            if key in concept_lower:
                info = interviews[key]
                result = f"🎯 Interview Preparation for {concept.title()}:\n\n"
                result += "Common Questions:\n"
                for i, qa in enumerate(info['common_questions'], 1):
                    result += f"\n{i}. Q: {qa['q']}\n   A: {qa['a']}"
                result += f"\n\n💡 Pro Tips:\n"
                for tip in info['tips']:
                    result += f"• {tip}\n"
                return result
        
        return f"🎯 Interview Tips for {concept}:\n\n1. Understand the fundamentals deeply\n2. Prepare real project examples\n3. Practice explaining your thought process\n4. Know common pitfalls and how to avoid them\n\nWould you like specific questions on this topic?"
    
    def _coding_mode(self, concept):
        """Only coding examples and exercises"""
        codes = {
            'function': '''# Function Example
def greet(name, greeting="Hello"):
    """Return a greeting message"""
    return f"{greeting}, {name}!"

# Usage
print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!

# Lambda (anonymous function)
square = lambda x: x ** 2
print(square(5))                # 25''',
            
            'loop': '''# For Loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# List Comprehension (Pythonic loop)
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]''',
            
            'class': '''# Class Definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_human_age(self):
        return self.age * 7

# Usage
my_dog = Dog("Buddy", 3)
print(my_dog.bark())           # Buddy says Woof!
print(my_dog.get_human_age())  # 21'''
        }
        
        concept_lower = concept.lower()
        for key in codes:
            if key in concept_lower:
                return f"💻 Code Example for {concept.title()}:\n\n```python\n{codes[key]}\n```\n\nTry modifying this code and see what happens!"
        
        return f"""💻 Coding Exercise for {concept}:

```python
# Your turn! Implement {concept} below

# Start with this template:
def solve():
    pass

# Test your solution:
if __name__ == "__main__":
    solve()
```"""
    
    def _analogy_mode(self, concept):
        """Explain using analogies"""
        analogies = {
            'inheritance': 'Inheritance is like genetic traits. Children inherit features from parents (eye color, height) but can also have unique traits.',
            'polymorphism': 'Polymorphism is like a universal remote. Same buttons (interface) work differently for TV, AC, or sound system (different objects).',
            'encapsulation': 'Encapsulation is like a capsule medicine. The inside (data) is protected by the outer shell (methods). You swallow the capsule, not the powder directly.',
            'stack': 'A stack is like a stack of plates. You add to the top (push) and remove from the top (pop). Last In, First Out (LIFO).',
            'queue': 'A queue is like a line at a ticket counter. First person in line gets served first. First In, First Out (FIFO).',
            'binary search': 'Binary search is like finding a word in a dictionary. You open in the middle, see if your word is before or after, and repeat with half the book.'
        }
        
        concept_lower = concept.lower()
        for key in analogies:
            if key in concept_lower:
                return f"🔗 Analogy for {concept.title()}:\n\n{analogies[key]}\n\nThis real-world comparison helps you remember how it works!"
        
        return f"🔗 Think of {concept} like a Swiss Army knife - one tool with multiple uses depending on what you need!"
    
    def _normal_explanation(self, concept):
        """Standard detailed explanation"""
        return f"""📚 Understanding {concept}:

**What is it?**
{concept} is a fundamental concept used across programming and technology.

**Why is it important?**
- Makes code more efficient
- Solves common problems elegantly
- Essential for technical interviews
- Used in real-world applications daily

**Key Points:**
1. Start with the basics
2. Practice with simple examples
3. Gradually increase complexity
4. Apply in real projects

**Common Use Cases:**
- Building applications
- Data processing
- Automation
- Problem-solving

**Next Steps:**
- Try the coding examples
- Complete practice exercises
- Build a small project using this concept

Would you like me to explain any specific aspect in more detail?"""
