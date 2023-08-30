from distutils.core import setup

setup(
    name="godspeedio",
    packages=["godspeedio"],
    version="0.1.1",
    license="MIT",
    description="memory efficient, fast, and easy to use stream processing library",
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
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Typing :: Typed",
    ],
)
