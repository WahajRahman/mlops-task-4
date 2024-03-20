# Makefile for building and running the application

# Define targets
.PHONY: all clean run

# Default target
all: run

# Build and run the Docker container
run:
    docker build -t your_docker_image_name .
    docker run -p 5000:5000 your_docker_image_name

# Clean up Docker images and containers
clean:
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker rmi $(docker images -q)
