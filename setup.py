import setuptools
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name="duplauth",
    version="0.0.1",
    description="A python3 client for the auth.dupl.tech api",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/AgeOfMarcus/duplauth",
    author="AgeOfMarcus",
    author_email="marcus@marcusweinberger.com",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=['requests'],
)