# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Copy the add-on's run script to the container
COPY run.sh /run.sh

# Make the run script executable
RUN chmod a+x /run.sh

# Install Streamlit
RUN pip install streamlit

# Set the default command to execute the run script
CMD [ "/run.sh" ]