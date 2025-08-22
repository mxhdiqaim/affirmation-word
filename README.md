# Affirmation Word

A simple Flask application for serving affirmation words.

## Features

- REST API built with Flask
- Dockerized for easy deployment

## Requirements

- Python 3.11+
- Docker

## Setup

### Local Development

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Run the app:
    ```sh
    python main.py
    ```

### Docker

1. Build the Docker image:
    ```sh
    docker build -t affirmation-word .
    ```
2. Run the container:
    ```sh
    docker run -p 5000:5000 affirmation-word
    ```

## Project Structure

- `main.py` — Application entry point
- `requirements.txt` — Python dependencies
- `Dockerfile` — Docker build instructions
- `.dockerignore` — Files excluded from Docker build
- `.gitignore` — Files excluded from Git

## License

MIT