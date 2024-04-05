#!/bin/bash

# Function to check if a command exists
command_exists () {
    type "$1" &> /dev/null ;
}

# Update package list
echo "Updating package list..."
sudo apt-get update

# Check for Python 3 and install if not exists
if command_exists python3; then
    echo "Python 3 is already installed."
else
    echo "Installing Python 3..."
    sudo apt-get install python3
fi

# Check for pip and install if not exists
if command_exists pip3; then
    echo "pip is already installed."
else
    echo "Installing pip..."
    sudo apt-get install python3-pip
fi

# Check for virtualenv and install if not exists
if command_exists virtualenv; then
    echo "virtualenv is already installed."
else
    echo "Installing virtualenv..."
    pip3 install virtualenv
fi

# Create a virtual environment named 'env' if it doesn't already exist
if [ ! -d "env" ]; then
    virtualenv env
fi

# Activate the virtual environment
echo "Activating the virtual environment..."

sleep 10
# Rerun this line in the terminal if you are not in the virtual environment
source env/bin/activate

# Check for Jupyter and install if not exists
if command_exists jupyter; then
    echo "Jupyter is already installed in the virtual environment."
else
    echo "Installing Jupyter..."
    pip install jupyter
fi

echo "Setup completed. Virtual environment 'env' is now active."
echo "You can start Jupyter Notebook by running 'jupyter notebook' command."