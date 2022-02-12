from setuptools import setup, find_packages
from selsearch import __version__ as version


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="selsearch",
    author="Jérome Eertmans",
    author_email="jeertmans@icloud.com",
    version=version,
    packages=find_packages(),
    description="Internet search based on selected text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeertmans/selsearch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.6",
    install_requires=[
        "click==8.0.3",
        "pyperclip==1.8.2",
        "keyboard==0.13.5",
    ],
    entry_points="""
        [console_scripts]
        selsearch=selsearch.main:main
    """,
)
