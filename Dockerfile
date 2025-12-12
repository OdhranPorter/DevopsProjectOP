# Use python 3.10 to match the CI environment
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run the test suite runner by default
CMD ["python", "tests/testSuiteRunner.py"]