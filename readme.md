🧮 Python CLI Calculator

A simple and interactive command-line calculator written in Python.
This calculator performs basic arithmetic operations and allows the user to continue calculating using the previous result, just like a real calculator memory feature.

📌 Features

➕ Addition

➖ Subtraction

✖️ Multiplication

➗ Division

🔁 Continue calculations using previous results

📟 Clean and user-friendly CLI interaction

🖼️ Includes ASCII art logo support (logo.py)

📂 Project Structure
.
├── calculator.py     # Main program
├── logo.py           # Contains ASCII art for the calculator logo
└── README.md         # Project documentation

🚀 How It Works

The user inputs two numbers and selects an arithmetic operation.

The program displays the result.

The user can choose to:

Continue calculating using the previous result, or

Exit the program

The loop continues until the user types "no".

📜 Code Overview
🔧 calculator(n1, n2, operation)

A function that performs the selected arithmetic operation and returns the result.

🔁 user_same_calculator(result)

A loop that allows continuous calculations using the previously obtained result.

▶️ Program Flow

Print logo

Ask for first numbers

Calculate

Ask if user wants to continue using result

Exit and print final value

🖥️ Usage

Run the script using:

python calculator.py


Example interaction:

Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): *
Result: 50

Do you want to perform another calculation using this result? yes
Current result: 50
Enter next number: 2
Enter operation (+, -, *, /): +
New result: 52

🧵 Sample Output
  _____________________
 |  _________________  |
 | | Python Calc     | |
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| |
 ...

Enter first number: 12
Enter second number: 3
Enter operation: /
Result: 4.0

💡 Future Improvements

Add support for exponentiation

Add clear screen functionality

Add error handling for invalid inputs

Convert to GUI version

🤝 Contributing

Pull requests are welcome!
If you’d like to improve the code or add new features, feel free to submit a PR.

📜 License

This project is open-source and available under the MIT License.