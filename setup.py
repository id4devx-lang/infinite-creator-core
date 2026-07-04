from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="infinite-creator-core",
    version="32.0.0",
    author="Pisut Somwang",
    author_email="id4.dev.x@gmail.com",
    description="The Infinite Creator - Sovereign AI Core Engine with Quantum-Safe Cryptography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/id4devx-lang/infinite-creator-core",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-benchmark>=4.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "infinite-creator=infinite_creator_sdk:InfiniteCreatorSDK.deploy_sovereign_node",
        ],
    },
)
