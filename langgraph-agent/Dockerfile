ARG PYTHON_VERSION=3.11.10
FROM python:${PYTHON_VERSION} as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache for dependencies
COPY langgraph-agent/requirements.txt /app/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install -r /app/requirements.txt

# Copy only the relevant files and directories
COPY langgraph-agent/ /app/

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD chainlit run -h --host 0.0.0.0 --port 8000 chainlit_ui.py