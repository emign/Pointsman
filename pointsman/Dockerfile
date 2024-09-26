ARG BUILD_FROM
FROM $BUILD_FROM

# Install necessary packages
RUN apk add --no-cache python3 py3-pip  # Für Alpine Linux-basierte Basis-Images
# oder
# RUN apt-get update && apt-get install -y python3 python3-pip  # Für Debian/Ubuntu-basierte Basis-Images

# Install Streamlit
RUN pip install streamlit

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]