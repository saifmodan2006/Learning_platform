"""Practical Learning Engine - Extract and simplify code examples"""

class PracticalEngine:
    def __init__(self):
        self.code_examples = {
            'python': self._get_python_examples(),
            'javascript': self._get_js_examples(),
            'data': self._get_data_examples(),
            'web': self._get_web_examples()
        }
    
    def extract_examples(self, course_data):
        """Extract practical code examples from course"""
        title = course_data.get('overview', {}).get('title', '').lower()
        
        if 'python' in title:
            return self.code_examples['python']
        elif 'javascript' in title or 'react' in title or 'web' in title:
            return self.code_examples['javascript'] + self.code_examples['web']
        elif 'data' in title or 'analytics' in title:
            return self.code_examples['data']
        else:
            return self._get_generic_examples()
    
    def generate_tasks(self, practical_content):
        """Generate practice tasks from examples"""
        tasks = []
        for i, example in enumerate(practical_content, 1):
            task = {
                'task_id': i,
                'title': f"Practice: {example['title']}",
                'description': example['description'],
                'starter_code': example.get('starter_code', ''),
                'expected_output': example.get('expected_output', ''),
                'difficulty': example.get('difficulty', 'Medium'),
                'hints': example.get('hints', [])
            }
            tasks.append(task)
        
        # Add additional challenge tasks
        tasks.append({
            'task_id': len(tasks) + 1,
            'title': 'Challenge: Build Something New',
            'description': 'Combine what you learned to create a unique project',
            'starter_code': '# Start with a blank slate\n',
            'expected_output': 'A working application',
            'difficulty': 'Hard',
            'hints': ['Review previous examples', 'Break the problem into smaller parts', 'Test incrementally']
        })
        
        return tasks
    
    def _get_python_examples(self):
        return [
            {
                'title': 'Variables and Data Types',
                'description': 'Learn to work with different data types',
                'code': '''# Variables and Data Types
name = "Alice"           # String
age = 25                 # Integer
height = 5.7             # Float
is_student = False       # Boolean

print(f"{name} is {age} years old")''',
                'explanation': 'Python automatically detects data types. Use f-strings for clean formatting.',
                'common_mistakes': ['Forgetting quotes for strings', 'Using = instead of == for comparison'],
                'difficulty': 'Easy'
            },
            {
                'title': 'Functions and Return Values',
                'description': 'Create reusable code blocks',
                'code': '''def calculate_discount(price, discount_percent):
    """Calculate final price after discount"""
    if discount_percent < 0 or discount_percent > 100:
        return "Invalid discount"
    
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

# Usage
original = 100
final = calculate_discount(original, 20)
print(f"Final price: ${final}")''',
                'explanation': 'Functions help avoid repetition. Always validate inputs and add docstrings.',
                'common_mistakes': ['Forgetting return statement', 'Not handling edge cases'],
                'difficulty': 'Medium'
            },
            {
                'title': 'List Comprehensions',
                'description': 'Write concise loops',
                'code': '''# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)

# Pythonic way (List Comprehension)
squares = [i ** 2 for i in range(10)]

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]

print(even_squares)  # [0, 4, 16, 36, 64]''',
                'explanation': 'List comprehensions are faster and more readable than traditional loops.',
                'common_mistakes': ['Making them too complex', 'Forgetting when to use regular loops'],
                'difficulty': 'Medium'
            },
            {
                'title': 'File Handling',
                'description': 'Read and write files safely',
                'code': '''# Reading a file
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('output.txt', 'w') as file:
    file.write("Hello, World!\\n")
    file.write("Second line\\n")

# The 'with' statement automatically closes the file''',
                'explanation': 'Always use "with" for file operations - it handles closing automatically.',
                'common_mistakes': ['Forgetting to close files', 'Using wrong mode (r/w/a)'],
                'difficulty': 'Medium'
            },
            {
                'title': 'Error Handling',
                'description': 'Handle exceptions gracefully',
                'code': '''def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Please use numbers only!"
    finally:
        print("Division attempt completed")

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error message''',
                'explanation': 'Try-except blocks prevent crashes. Use specific exceptions, not bare except.',
                'common_mistakes': ['Using bare except:', 'Ignoring errors silently'],
                'difficulty': 'Medium'
            }
        ]
    
    def _get_js_examples(self):
        return [
            {
                'title': 'DOM Manipulation',
                'description': 'Interact with HTML elements',
                'code': '''// Select element
const button = document.querySelector('#myButton');

// Add event listener
button.addEventListener('click', () => {
    const heading = document.querySelector('h1');
    heading.textContent = 'Clicked!';
    heading.style.color = 'blue';
});

// Create new element
const newDiv = document.createElement('div');
newDiv.textContent = 'New Content';
document.body.appendChild(newDiv);''',
                'explanation': 'Always cache DOM selections. Use event delegation for dynamic content.',
                'common_mistakes': ['Querying DOM inside loops', 'Forgetting to wait for DOM load'],
                'difficulty': 'Medium'
            },
            {
                'title': 'Async/Await',
                'description': 'Handle asynchronous operations',
                'code': '''async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Usage
fetchData().then(data => console.log(data));''',
                'explanation': 'Async/await makes async code look synchronous. Always handle errors with try-catch.',
                'common_mistakes': ['Forgetting await', 'Not handling errors'],
                'difficulty': 'Hard'
            }
        ]
    
    def _get_data_examples(self):
        return [
            {
                'title': 'Pandas DataFrame Basics',
                'description': 'Work with tabular data',
                'code': '''import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)

# Basic operations
print(df.head())           # First rows
print(df.info())           # Data info
print(df.describe())       # Statistics

# Filter data
adults = df[df['Age'] > 30]

# Group by
city_avg = df.groupby('City')['Age'].mean()''',
                'explanation': 'DataFrames are like smart Excel sheets. Use vectorized operations for speed.',
                'common_mistakes': ['Using loops instead of vectorization', 'Modifying original data accidentally'],
                'difficulty': 'Medium'
            },
            {
                'title': 'Data Cleaning',
                'description': 'Handle missing and dirty data',
                'code': '''import pandas as pd
import numpy as np

# Create sample data with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [10, 20, 30, 40]
})

# Check missing values
print(df.isnull().sum())

# Fill missing values
df['A'] = df['A'].fillna(df['A'].mean())
df['B'] = df['B'].fillna(0)

# Drop rows with too many missing
df_clean = df.dropna(thresh=2)

# Remove duplicates
df_clean = df_clean.drop_duplicates()''',
                'explanation': 'Always explore missing data patterns before deciding how to handle them.',
                'common_mistakes': ['Dropping too much data', 'Filling with wrong values'],
                'difficulty': 'Medium'
            }
        ]
    
    def _get_web_examples(self):
        return [
            {
                'title': 'Responsive CSS',
                'description': 'Make websites mobile-friendly',
                'code': '''/* Mobile-first approach */
.container {
    width: 100%;
    padding: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        max-width: 750px;
        margin: 0 auto;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        max-width: 1200px;
    }
}''',
                'explanation': 'Start with mobile styles, then add media queries for larger screens.',
                'common_mistakes': ['Desktop-first approach', 'Too many breakpoints'],
                'difficulty': 'Easy'
            }
        ]
    
    def _get_generic_examples(self):
        return [
            {
                'title': 'Basic Example',
                'description': 'Fundamental concept demonstration',
                'code': '# Your code here\nprint("Hello, World!")',
                'explanation': 'Start with the basics and build up gradually.',
                'common_mistakes': ['Skipping fundamentals', 'Not practicing enough'],
                'difficulty': 'Easy'
            }
        ]
