ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python 3.9 and pip
RUN apk add --no-cache python3 py3-pip

# Install Streamlit using pip
RUN pip3 install streamlit

# Copy data for add-on
COPY run.sh /run.sh
RUN chmod a+x /run.sh

# Set the default command to execute the run script
CMD [ "/run.sh" ]