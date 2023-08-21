import os

def create_directory_if_not_exists(directory_path):
    """Ensure a directory exists. If it doesn't, create it."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
