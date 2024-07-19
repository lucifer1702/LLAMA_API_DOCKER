FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip git

# Copy LLaMA code
WORKDIR /llama_swagger
COPY . /llama_swagger

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]

