# In sys-explorer/setup.py

from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read the requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    # The name of the project on PyPI and for pip
    name='sys-explorer',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A web-based tool to explore local files and generate a combined markdown document.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # The URL to your GitHub repo
    url='https://github.com/your-username/sys-explorer',
    # find_packages() will automatically discover the 'sysexplore' package
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    # This creates the command-line tool
    entry_points={
        'console_scripts': [
            # 'command_name = package_name.module_name:function_name'
            'sysexplorer=sysexplore.app:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Flask',
        'Topic :: Text Processing',
        'Environment :: Web Environment',
    ],
    python_requires='>=3.7',
)
