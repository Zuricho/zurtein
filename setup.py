# setup.py
from setuptools import setup, find_packages

setup(
    name='zurtein',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # dependencies here, e.g.,
        'scipy>=1.4',
        'numpy>=1.18',
        'pandas>=1.0',
        'matplotlib>=3.1',
        'scikit-learn>=0.22',
    ],
)