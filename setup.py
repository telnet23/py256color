from pathlib import Path
from setuptools import setup

with open(Path(__file__).parent.joinpath("README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="py256color",
    description="Convert between 256 colors and RGB.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/telnet23/py256color",
    license="Apache License 2.0",
    use_scm_version=True,
    setup_requires=[
        "setuptools_scm",
    ],
    packages=[
        "py256color",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
