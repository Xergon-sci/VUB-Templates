from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vubTemplates',
    url='https://github.com/Xergon-sci/VUB-Templates',
    author='Michiel Jacobs',
    author_email='michiel.jacobs@vub.be',
    packages=['vubTemplates'],
    install_requires=['fpdf2'],
    version='0.1',
    license='MIT',
    description='A package to dynamically generate reports in the VUB house style.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
