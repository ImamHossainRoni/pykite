from setuptools import setup, find_packages

__author__ = 'Imam Hossain Roni'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pykite",
    version="1.0.0",
    description="A Python-centric micro-framework for building web applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Imam Hossain Roni",
    author_email="imamhossainroni95@gmail.com",
    url="https://github.com/imamhossainroni/pykite",
    packages=find_packages(),
    install_requires=[
        "parse",
        "werkzeug",
    ],
    entry_points={
        "console_scripts": [
            "pykite = pykite.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "pykite",
        "web framework",
        "micro framework",
        "web applications",
        "Python",
        "HTTP",
        "WSGI",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/imamhossainroni/pykite/issues",
        "Source Code": "https://github.com/imamhossainroni/pykite",
        "Documentation": "https://github.com/imamhossainroni/pykite/blob/main/README.md",
        "Icon Image": "https://raw.githubusercontent.com/ImamHossainRoni/pykite/main/extras/yellow-kite.png",
    },
)
