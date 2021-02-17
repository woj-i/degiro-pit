import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="degiro-pit-woj-i",
    version="0.1.0",
    author="Wojciech Indyk",
    description="Application for get EUR/PLN value for the last working day of DeGiro transaction. "
                "It helps to prepare PIT for The National Revenue Administration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woj-i/degiro-pit/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)