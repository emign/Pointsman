ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python 3.9, pip, and virtualenv
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Copy requirements.txt to the container
COPY requirements.txt /requirements.txt

# Activate the virtual environment and install the packages from requirements.txt
RUN /opt/venv/bin/pip install -r /requirements.txt

# Copy data for add-on
COPY run.sh /run.sh
RUN chmod a+x /run.sh

# Set the default command to execute the run script
CMD [ "/run.sh" ]