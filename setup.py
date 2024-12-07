from setuptools import setup, find_packages

setup(
    name="OSS_Library",
    version="1.0.0",
    description="A library for audio processing",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pydub>=0.25.1",
        "ffmpeg-python>=0.2.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.12, < 3.13",
)
