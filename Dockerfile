# Pull official base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update \
    && apt-get install -y python3-dev build-essential \
    && apt-get clean

# Create and activate virtual environment
RUN pip install --upgrade pip \
    && pip install virtualenv \
    && python -m virtualenv /opt/venv

# Ensure the virtual environment is used:
ENV PATH="/opt/venv/bin:$PATH"

# Copy the requirements file and install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy project files
COPY . /srv/app
WORKDIR /srv/app

# Run the Django development server (this command will be run when the container starts)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
