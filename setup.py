from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wpinfo",
    version="0.1.0",
    author="Deadpool2k",
    author_email="d2kyt@protonmail.com",
    description="WordPress information enumeration and scraping tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Deadpool2000/wpinfo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="wordpress info enumeration scraping web, scraping, wordpress, web scraping, wordpress info enumeration, wordpress scraping, wordpress info, wordpress enumeration, wordpress web scraping, wordpress web info, wordpress web enumeration, wordpress web info enumeration, wordpress web scraping info, wordpress web scraping enumeration, wordpress web scraping info enumeration",
)
