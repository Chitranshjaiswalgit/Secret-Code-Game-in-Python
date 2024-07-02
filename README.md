# Secret-Code-Game-in-Python

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contribution](#contribution)


## Project Overview
The Secret Code Game is a Python script that allows users to encode or decode messages based on a specific pattern. This interactive program provides users with the ability to transform text messages into coded formats and vice versa.


## Installation
This project requires Python 3.12.1 or later.
To set up the project:
1. Ensure Python 3.12.1 or a later version is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository to your local machine.
      - git clone <https://github.com/jaiswalchitransh/Secret-Code-Game-in-Python>
4. Open the project in your preferred Python environment (e.g., IDE or terminal).
5. Run the script (`game.py`) and observe the output.


## Usage
Ensure Python 3.x is installed. Run the script:

- python game.py
  
Upon starting the Secret Code Game, you will be prompted with options to either encode or decode a message:
- Enter `1` for Coding (encoding).
- Enter `0` for Decoding (decoding).

Depending on your choice, follow the instructions to input the message you want to process. The script will apply the encoding or decoding rules described below:

### Encoding (Coding)

Each word in the message is transformed based on the following rules:
- Words with three or more characters are rearranged: the first and last characters are placed at alternating positions, with specific characters ('aix' and 'zof') added.
- Words with less than three characters are simply reversed.

The resulting encoded message is printed to the console.

### Decoding

The script attempts to reverse the encoding process:
- For words with three or more characters, it adjusts the positions of specific characters to reconstruct the original message.
- If an error occurs during decoding (such as an IndexError), a warning message is displayed, and the user is prompted to input a valid decoded message.

The decoded message is then printed to the console.


## Features
- **Interactive Interface**: Users can choose between encoding and decoding modes.
- **Flexible Input Handling**: Supports various message lengths and characters.
- **Error Handling**: Alerts users to input errors during decoding.


## Contribution
I, **Chitransh Jaiswal** developed this Project Individually. I was responsible for all aspects of the project, including design, development, testing, and documentation.
Contributions to improve the efficiency, readability, or functionality of the code are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

Please ensure your contributions adhere to the coding standards and follow the existing style and structure.

---

Thank you for your interest in the Secret Code Game. Have fun encoding and decoding messages!
