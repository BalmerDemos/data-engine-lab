# BalmerDemos contribution
# Use Python 3.10-slim as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Update the package list and install utilities in one layer
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    vim \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install dependencies in one layer
RUN pip install --no-cache-dir \
    Flask==3.1.0 \
    h2==4.1.0 \
    pandas==2.2.3 \
    pipdeptree==2.24.0 \
    prefect==3.1.12 \
    pymongo==4.10.1 \
    pyspark==3.5.4 \
    scikit-learn==1.6.1 \
    setuptools==65.5.0 \
    numpy==2.2.1  # Add numpy explicitly

# Upgrade pip to the latest version
RUN pip install --upgrade pip


# Copy your Prefect flows and scripts into the container
COPY ./flows /app/flows

# Set environment variables
ENV PREFECT_BACKEND="server"

# Expose the Prefect API server port
EXPOSE 4200

#CMD ["bash",]
CMD ["tail", "-f", "/dev/null"]


