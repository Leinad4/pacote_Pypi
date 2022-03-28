from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='smd',
    version='0.0.6',
    author='Daniel',
    long_description=readme,
    long_description_content_type='text/markdown',
    description=u'Primeiro pacote PyPi',
    packages=['smd'],
    install_requires=['numpy'],)