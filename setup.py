  
from setuptools import setup
import os

with open('README.md') as f:
    long_description = f.read()

setup(
    name='fstelemetry',
    version='0.1.1',
    packages=['fstelemetry'],
    url='https://github.com/jbencina/fstelemetry',
    download_url='https://github.com/jbencina/fstelemetry/archive/v0.1.1.tar.gz',
    license='MIT',
    author='John Bencina',
    keywords=['flight', 'simulator', 'simconnect', 'flightsim'],
    description='Capture FS2020 telemery to a csv file',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'SimConnect==0.4.23',
        'pyyaml'
    ],
    include_package_data=True,
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['fstelemetry=fstelemetry.__main__:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)