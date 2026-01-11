# We use the full image (not slim) so we don't need to run apt-get install
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy just the requirements first (to cache them)
COPY requirements.txt .

# Install dependencies
# We upgrade pip first to avoid wheel build errors
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]