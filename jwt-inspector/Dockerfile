FROM python:3.11-slim

# Create non-root user
RUN useradd -m jwtuser

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Fix permissions
RUN chown -R jwtuser:jwtuser /app

USER jwtuser

EXPOSE 5000

CMD ["python", "app.py"]
