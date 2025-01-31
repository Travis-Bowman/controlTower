from setuptools import setup, find_packages

setup(
    name="controlTower",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pigpio",
        "serial",
    ],
    python_requires=">=3.6",
)