# Installation Guide

## Prerequisites

- Python 3.9 or higher
- pip or conda
- Git (for development installation)

## From PyPI (Recommended)

Install the stable release from PyPI:

```bash
pip install infinite-creator-core
```

## From Source (Development)

For development or to use the latest features:

```bash
# Clone the repository
git clone https://github.com/id4devx-lang/infinite-creator-core.git
cd infinite-creator-core

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Docker Installation

### Build Docker Image

```bash
docker build -t infinite-creator:latest .
```

### Run Container

```bash
docker run -it infinite-creator:latest
```

### Docker Compose (Optional)

```yaml
version: '3.8'
services:
  creator:
    build: .
    volumes:
      - .:/app
    command: /bin/bash
```

Then run:
```bash
docker-compose up -d
docker-compose exec creator /bin/bash
```

## Verify Installation

After installation, verify everything works:

```python
from infinite_creator_sdk import InfiniteCreatorSDK

sdk = InfiniteCreatorSDK(master_name="Test")
print("✅ Installation successful!")
```

Or run tests:

```bash
pytest -v
```

## Optional Dependencies

Install development/testing dependencies:

```bash
# For development
pip install -e ".[dev]"

# Includes:
# - pytest >= 8.0.0
# - pytest-benchmark >= 4.0.0
# - pytest-cov >= 4.0.0
# - black >= 23.0.0
# - flake8 >= 6.0.0
# - mypy >= 1.0.0
```

## Troubleshooting

### Python Version Issue

If you get a Python version error:

```bash
python3.11 -m pip install infinite-creator-core
```

### Permission Error

On Linux/Mac:

```bash
pip install --user infinite-creator-core
```

### Module Not Found

Ensure virtual environment is activated:

```bash
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

## Next Steps

- [Quick Start Guide](quickstart.md)
- [API Reference](api/reference.md)
- [Examples](api/examples.md)

---

For more help, see the [GitHub Issues](https://github.com/id4devx-lang/infinite-creator-core/issues).
