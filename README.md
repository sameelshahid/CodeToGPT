# CodeToGPT

Welcome to **CodeToGPT**, a powerful tool designed to simplify the process of preparing codebases for interactions with AI models like ChatGPT. By concatenating multiple code files into well-organized documents, this application enhances the ease and efficiency of providing complex code contexts to AI, facilitating more accurate and context-aware responses.

## Features

- **Multi-Language Support**: Handles both Python (`*.py`) and Java (`*.java`), creating separate output files for each language to ensure clarity and organization.
- **Automated Concatenation**: Automatically combines all code files from a specified directory into concise, single documents—ideal for large projects.
- **Ease of Use**: Offers a simple command-line interface that allows for straightforward operations without the need for complex GUIs.

## Getting Started

### Prerequisites

Before you start using **CodeToGPT**, make sure you have Python 3.6 or higher installed on your machine.

### Installation

To install **CodeToGPT**, follow these steps:

```bash
pip install code-to-gpt
```


## Usage

To run **CodeToGPT**, navigate to your project directory and execute:

```bash
codetogpt '/path/to/source/folder'
```

## Usage

This command will generate:
- `combined_python_code.txt` for Python files.
- `combined_java_code.txt` for Java files.

These files will be created in the specified source folder, containing all the code from files of the respective languages found within that directory and its subdirectories.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

Sameel Shahid - [@sameelshahid](https://www.linkedin.com/in/sameel-shahid/)

Abdul Jaleel Khan- [@ajk](https://www.linkedin.com/in/abdul-jaleel-khan/)

Project Link: [https://github.com/sameelshahid/codetogpt](https://github.com/sameelshahid/codetogpt)
