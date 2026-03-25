"""Doubt Solver - Answer user questions instantly"""

class DoubtSolver:
    def __init__(self):
        self.common_doubts = {
            'error': self._handle_error_questions,
            'debug': self._handle_debugging,
            'concept': self._explain_concept,
            'howto': self._how_to_guide,
            'best practice': self._best_practices
        }
    
    def answer(self, question):
        """Answer user questions with multiple explanations"""
        question_lower = question.lower()
        
        # Detect question type
        if any(word in question_lower for word in ['error', 'exception', 'traceback', 'failed']):
            return self._handle_error_questions(question)
        elif any(word in question_lower for word in ['debug', 'not working', 'wrong output']):
            return self._handle_debugging(question)
        elif any(word in question_lower for word in ['what is', 'explain', 'define', 'mean']):
            return self._explain_concept(question)
        elif any(word in question_lower for word in ['how to', 'how do i', 'ways to']):
            return self._how_to_guide(question)
        elif any(word in question_lower for word in ['best', 'practice', 'recommend', 'should i']):
            return self._best_practices(question)
        else:
            return self._general_answer(question)
    
    def _handle_error_questions(self, question):
        """Handle error-related questions"""
        return f"""🔍 Error Analysis:

**Common Causes:**
1. Syntax errors (missing brackets, quotes, colons)
2. Type errors (operating on wrong data types)
3. Name errors (using undefined variables)
4. Import errors (missing or incorrect imports)
5. Indentation errors (inconsistent spacing)

**Debugging Steps:**
1. Read the error message carefully - it tells you the line number
2. Check the line above the error (sometimes the issue is there)
3. Print variable values before the error
4. Google the exact error message
5. Use a debugger or add print statements

**Example Fix:**
```python
# Wrong
print("Hello"  # Missing closing bracket

# Right
print("Hello")
```

**Pro Tip:** Copy the last line of the traceback and search it online - someone has already solved this!

Would you like me to look at your specific error code?"""
    
    def _handle_debugging(self, question):
        """Help with debugging"""
        return f"""🐛 Debugging Guide:

**Systematic Approach:**

1. **Reproduce the Issue**
   - Can you make it fail consistently?
   - What are the exact steps?

2. **Isolate the Problem**
   - Comment out sections of code
   - Test small pieces independently

3. **Check Your Assumptions**
   - Print variable types and values
   - Verify input data is what you expect

4. **Rubber Duck Debugging**
   - Explain your code line-by-line out loud
   - Often you'll find the bug yourself!

5. **Common Culprits:**
   - Off-by-one errors in loops
   - Mutable default arguments
   - Variable scope issues
   - Async/await mistakes
   - Forgetting to return values

**Debugging Tools:**
- `print()` statements (simple but effective)
- Python debugger: `import pdb; pdb.set_trace()`
- IDE debugger (breakpoints, step-through)
- Logging module for complex apps

Share your code and I'll help spot the issue!"""
    
    def _explain_concept(self, question):
        """Explain concepts clearly"""
        return f"""📖 Concept Explanation:

I'd be happy to explain this concept! Here's my approach:

**Simple Definition:**
Let me break it down in simple terms first.

**Real-World Analogy:**
Think of it like something you already understand...

**Technical Details:**
Now let's add the technical specifics.

**Code Example:**
```python
# Simple example showing the concept
def example():
    pass
```

**Common Misconceptions:**
- Misconception 1: Actually it works differently
- Misconception 2: Here's the correct understanding

**When to Use It:**
- Scenario 1: Perfect use case
- Scenario 2: Another good application
- When NOT to use: Alternative approaches

**Practice Exercise:**
Try implementing this yourself with a small example.

Which part would you like me to clarify further?"""
    
    def _how_to_guide(self, question):
        """Provide how-to guidance"""
        return f"""🛠️ How-To Guide:

Here's a step-by-step approach:

**Step 1: Setup**
- Install necessary tools/libraries
- Set up your development environment
- Create project structure

**Step 2: Implementation**
```python
# Basic template
def solve_problem():
    # Your code here
    pass
```

**Step 3: Testing**
- Test with sample data
- Check edge cases
- Verify expected output

**Step 4: Optimization**
- Improve performance if needed
- Clean up code
- Add error handling

**Alternative Approaches:**
1. Quick solution (for prototypes)
2. Best practice (for production)
3. Advanced method (for scale)

**Resources:**
- Official documentation
- Tutorial links
- Example projects

What specific aspect are you trying to implement?"""
    
    def _best_practices(self, question):
        """Share best practices"""
        return f"""✨ Best Practices:

**General Guidelines:**

1. **Write Readable Code**
   - Use meaningful variable names
   - Add comments for complex logic
   - Follow style guides (PEP 8 for Python)

2. **Keep It Simple (KISS)**
   - Don't over-engineer
   - Simple solutions are easier to maintain
   - Refactor when needed

3. **Error Handling**
   - Catch specific exceptions
   - Log errors properly
   - Fail gracefully

4. **Testing**
   - Write unit tests
   - Test edge cases
   - Automate testing

5. **Version Control**
   - Commit frequently
   - Write clear commit messages
   - Use branches for features

6. **Documentation**
   - Docstrings for functions
   - README for projects
   - Comments for complex parts

**Code Review Checklist:**
- [ ] Does it work correctly?
- [ ] Is it readable?
- [ ] Are there edge cases handled?
- [ ] Is it efficient enough?
- [ ] Is it tested?

**Pro Tips:**
- Learn from open-source projects
- Pair program when possible
- Continuously refactor

What specific area are you focusing on?"""
    
    def _general_answer(self, question):
        """General answer for any question"""
        return f"""💡 Answer to Your Question:

Great question! Let me help you with this.

**Understanding the Question:**
You're asking about: "{question}"

**Key Points:**
1. First, understand the fundamentals
2. Look at practical examples
3. Practice implementing it
4. Learn from mistakes

**Multiple Explanations:**

*Explanation 1 (Simple):*
Start with the basic concept in simple terms.

*Explanation 2 (Technical):*
Add technical depth and specifics.

*Explanation 3 (Practical):*
Show how it's used in real projects.

**Examples:**
```python
# Example 1: Basic usage
# Example 2: Advanced usage
```

**Next Steps:**
1. Try the examples yourself
2. Modify them to see what happens
3. Build something with this knowledge
4. Ask follow-up questions if stuck

**Additional Resources:**
- Documentation links
- Video tutorials
- Practice platforms

Feel free to ask for clarification on any point!"""
