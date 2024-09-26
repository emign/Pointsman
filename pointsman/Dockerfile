ARG BUILD_FROM
FROM $BUILD_FROM

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Copy Python requirements file
COPY requirements.txt .


RUN \
    apk add --no-cache --virtual .build-dependencies \
    build-base=0.5-r3 \
    python3-dev=3.11.10-r0 \
    \
    && apk add --no-cache \
    py3-pip=23.3.1-r0 \
    py3-wheel=0.42.0-r0 \
    python3=3.11.10-r0 \
    \
    && pip install -r /tmp/requirements.txt \
    \
    && cd /usr/lib/python3.11/site-packages/ \
    && patch -p1 < /patches/force_recompile.patch \
    \
    && find /usr \
    \( -type d -a -name test -o -name tests -o -name '__pycache__' \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' + \
    \
    && apk del --no-cache --purge .build-dependencies

# Install Streamlit
RUN pip install streamlit

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

LABEL \
    io.hass.version="VERSION" \
    io.hass.type="addon" \
    io.hass.arch="armhf|aarch64|i386|amd64"