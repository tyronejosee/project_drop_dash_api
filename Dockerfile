FROM python:3.12.2-slim-bullseye

# Disable pip's version check to avoid version-related warnings during installation.
ENV PIP_DISABLE_PIP_VERSION_CKECK 1

# Prevent Python from writing .pyc files to the container's filesystem.
ENV PYTHONDONTWRITEBYTECODE 1

# Ensure that Python output is sent straight to the terminal (stdout) without buffering.
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container to /app.
WORKDIR /app

# Copy the requirements directory from the host to /app/requirements/ in the container.
COPY requirements/ /app/requirements/

# Install Python dependencies from the production.txt file located in /app/requirements/.
RUN pip install -r requirements/production.txt

# Copy the rest of the application files from the host to /app in the container.
COPY . /app

# Copy the entrypoint script from the host to /app/entrypoint.sh in the container.
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable.
RUN chmod +x /app/entrypoint.sh

# Expose port 8000 on the container to allow communication to and from this port.
EXPOSE 8000

# Set the entrypoint for the container to execute the entrypoint.sh script when the container starts.
ENTRYPOINT ["/app/entrypoint.sh"]
