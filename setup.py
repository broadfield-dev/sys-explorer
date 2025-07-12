# In sys-explorer/setup.py

from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# We no longer need to read requirements.txt for install_requires
# as we will define them directly here.

setup(
    name='sys-explorer',
    version='0.1.1', # Bumped version for the change
    author='Your Name',
    author_email='your.email@example.com',
    description='A web-based tool to explore local files and generate a combined markdown document.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/broadfield-dev/sys-explorer',
    packages=find_packages(),
    include_package_data=True,
    
    # --- THIS IS THE KEY CHANGE ---
    install_requires=[
        'Flask',
        'repo-to-md @ git+https://github.com/broadfield-dev/repo_to_md.git'
    ],
    
    entry_points={
        'console_scripts': [
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
