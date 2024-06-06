from setuptools import setup, find_packages

import os

# Read the contents of your README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='code-to-gpt',
    version='0.6',
    packages=find_packages(),
    description='A simple tool to concatenate code files for ChatGPT prompts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sameel Shahid',
    author_email='sameelshahid@hotmail.com',
    url='https://github.com/yourusername/codepackager',
    entry_points={
        'console_scripts': [
            'codetogpt=codetogpt.packager:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
