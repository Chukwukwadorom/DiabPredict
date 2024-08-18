# Using Python 3.10.14 as a parent image
FROM python:3.10.14-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y gcc build-essential


RUN pip install --no-cache-dir -r requirements-streamlit.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
