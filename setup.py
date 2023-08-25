# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from setuptools import find_packages, setup


def get_requirements(path: str):
    """
    This function reads a file and returns a list of its lines, each stripped of leading/trailing whitespace.
    
    Args:
        path (str): The path to the file to be read.
    
    Returns:
        list: A list of strings, each representing a line in the file, stripped of leading/trailing whitespace.
    """
    return [l.strip() for l in open(path)]


setup(
    name="llama",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
