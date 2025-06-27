# Use official Python image
FROM python:3.11-slim

# Install Poetry globally
RUN pip install --no-cache-dir poetry

# Set working directory
WORKDIR /app

# Copy only the dependency files first (for better Docker caching)
COPY pyproject.toml poetry.lock ./

# Install dependencies — disable venvs so it's global
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the app
COPY app/ ./app/

# Expose the FastAPI default port
EXPOSE 8000

# Run the app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
