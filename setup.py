from setuptools import setup

setup(
    name='facebook-sdk',
    version="0.0.1",
    description='The Facebook graph api sdk',
    author='mantvmass',
    maintainer='Phumin-DEV',
    maintainer_email='kliop2317@gmail.com',
    url='https://github.com/mantvmass/facebook-sdk',
    license='Apache',
    packages=["facebook"],
    long_description=open("README.md").read(),
    install_requires=['requests'],
)