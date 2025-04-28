
# Use a minimal Python image with dependencies only for runtime
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage caching
COPY requirements.txt .

# Install only necessary runtime dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the application port
EXPOSE 5000

# Set the entrypoint
CMD ["python", "app.py"]

# Use a .dockerignore file to reduce unnecessary file copies
