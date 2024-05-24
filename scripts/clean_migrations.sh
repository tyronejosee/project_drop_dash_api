#!/bin/bash

# Define the base directory
BASE_DIR="apps"

# Print a warning message
echo "WARNING: This will delete all 'migrations' directories in $BASE_DIR and cannot be undone."
read -p "Are you sure you want to continue? (y/N): " confirm

# Check if the user confirmed
if [[ $confirm != [yY] ]]; then
    echo "Operation cancelled."
    exit 1
fi

# Find and remove all 'migrations' directories within the base directory
find "$BASE_DIR" -type d -name 'migrations' -exec rm -rf {} +

# Print a message indicating completion
echo "All 'migrations' directories have been removed."

# Prompt to make new migrations
read -p "Do you want to create new migrations now? (y/N): " new_migrations

if [[ $new_migrations == [yY] ]]; then
    # Apply the make migrations command
    python manage.py makemigrations
    echo "New migrations created."
fi
