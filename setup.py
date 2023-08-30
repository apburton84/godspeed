from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

print(README)

setup(
    name="godspeedio",
    packages=["godspeedio"],
    version="0.1.1",
    license="MIT",
    description="memory efficient, fast, and easy to use stream processing library",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Anthony Burton",
    author_email="apburton84@gmail.com",
    url="https://github.com/apburton84/godspeed",
    download_url="https://codeload.github.com/apburton84/godspeed/zip/refs/heads/main",
    keywords=[
        "STREAM",
        "PROCESSING",
        "MEMORY",
        "EFFICIENT",
        "FAST",
        "EASY",
        "USE",
        "LIBRARY",
    ],
    install_requires=["decorator"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Typing :: Typed",
    ],
)
