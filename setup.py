from setuptools import setup, find_packages

setup(
    name="oss_library", 
    version="0.0.2",
    description="A library for audio processing",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Leejaeman1",
    author_email="zr250vsd21@gmail.com",
    url="https://github.com/Leejaeman1/OSS_Library",
    license="MIT",
    packages=find_packages(),
    install_requires=["pydub"],
    python_requires=">=3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
