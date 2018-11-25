#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    """ Reads a file; Used everywhere.

    :param fname: The name of a file relative to the root path
    :return: The string contents of the file
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Airflow Houry Job Test',
    version='1.0',
    description='Docker Exaple with Airflow',
    long_description=read('README.md'),
    author='Ravi H',
    author_email='hravi.zip@gmail.com',
    url='',
    packages=['dags'],
    install_requires=read('requirements.txt'),
)
