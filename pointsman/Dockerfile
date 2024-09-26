ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python 3.9, pip, and venv
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-venv \
    python3.9-dev \
    python3-pip \
    build-essential \
    libarrow-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3.9 -m venv /opt/venv

# Copy requirements.txt to the container
COPY requirements.txt /requirements.txt

# Activate the virtual environment and install the packages from requirements.txt
RUN /opt/venv/bin/pip install --upgrade pip setuptools wheel \
    && /opt/venv/bin/pip install -r /requirements.txt

# Copy data for add-on
COPY run.sh /run.sh
RUN chmod a+x /run.sh

# Set the default command to execute the run script
CMD [ "/run.sh" ]