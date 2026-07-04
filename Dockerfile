FROM python:3.11-slim

# Set metadata
LABEL maintainer="Pisut Somwang <id4.dev.x@gmail.com>"
LABEL description="The Infinite Creator - Sovereign AI Core Engine with Quantum-Safe Cryptography"
LABEL version="32.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -e ".[dev]"

# Create non-root user for security
RUN useradd -m -u 1000 creator && \
    chown -R creator:creator /app

USER creator

# Expose port for documentation (if needed)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from infinite_creator_sdk import InfiniteCreatorSDK; print('✅ Healthy')" || exit 1

# Default command
CMD ["/bin/bash"]
