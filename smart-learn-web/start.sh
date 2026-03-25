#!/bin/bash

echo "🚀 Starting Smart Learning System..."
echo ""

# Check if Flask is installed
if ! python -c "import flask" 2>/dev/null; then
    echo "⚠️  Installing dependencies..."
    pip install flask flask-cors -q
fi

# Start backend
echo "📦 Starting Backend Server on http://localhost:5000"
cd backend
python app.py > /tmp/flask.log 2>&1 &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Check if backend is running
if curl -s http://localhost:5000/api/profile > /dev/null; then
    echo "✅ Backend is running!"
    echo ""
    echo "🌐 Frontend available at: file://$(pwd)/frontend/index.html"
    echo ""
    echo "📝 To view logs: cat /tmp/flask.log"
    echo "🛑 To stop: kill $BACKEND_PID"
    echo ""
    echo "🎯 Open frontend/index.html in your browser to start learning!"
else
    echo "❌ Failed to start backend. Check /tmp/flask.log for errors."
    exit 1
fi
