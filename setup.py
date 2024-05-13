from setuptools import setup, find_packages

setup(
    name='codegpt',
    version='0.1',
    packages=find_packages(),
    description='A simple tool to concatenate code files for ChatGPT prompts',
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
