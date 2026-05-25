#!/bin/bash

# Activate the virtual environment
# Note: Using venv/Scripts/activate for Windows (e.g., Git Bash) 
# If running on Linux/Mac, this would be venv/bin/activate
if [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate
elif [ -d "venv/bin" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found!"
    exit 1
fi

echo "Running test suite..."
# Execute the test suite
pytest test_app.py

# Capture the exit code of pytest
TEST_RESULT=$?

# Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "One or more tests failed!"
    exit 1
fi
