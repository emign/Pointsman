# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install virtualenv and set up the virtual environment
RUN pip install --no-cache-dir virtualenv && \
    virtualenv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code into the container
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app within the virtual environment
CMD ["/app/venv/bin/streamlit", "run", "app/app.py"]