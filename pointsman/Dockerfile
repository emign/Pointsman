ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python 3.9, pip, and other dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv \
    build-base \
    py3-numpy \
    py3-pandas \
    cmake \
    ninja \
    python3-dev \
    linux-headers \
    musl-dev \
    libffi-dev \
    zlib-dev \
    git \
    boost-dev \
    gflags-dev \
    glog-dev \
    snappy-dev \
    lz4-dev \
    zstd-dev \
    brotli-dev \
    jemalloc-dev \
    rapidjson-dev

# Set environment variables for Arrow installation
ENV ARROW_VERSION=10.0.1
ENV ARROW_HOME=/usr/local
ENV PARQUET_HOME=/usr/local

# Download and build Apache Arrow
RUN git clone https://github.com/apache/arrow.git \
    && cd arrow \
    && git checkout apache-arrow-${ARROW_VERSION} \
    && mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=${ARROW_HOME} -DARROW_PARQUET=ON -DARROW_PYTHON=ON -DARROW_BUILD_TESTS=OFF .. \
    && make -j$(nproc) \
    && make install

# Create a virtual environment
RUN python3 -m venv /opt/venv

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