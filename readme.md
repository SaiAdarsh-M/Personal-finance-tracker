# 📊 Personal Finance Tracker (CLI)

A menu-driven command-line Personal Finance Tracker built using Python. The application allows users to record income and expenses, store them persistently, and analyze their financial balance through transaction history.

## 🚀 Features
- Add income transactions  
- Add expense transactions  
- Dynamically calculate current balance  
- View complete transaction history  
- Persistent data storage using file handling  
- Simple and user-friendly CLI interface  

## 🛠️ Tech Stack
- **Language:** Python  
- **Concepts Used:** Functions & modular programming, file handling (`read`, `write`, `append`), loops (`while True`), conditional logic, string parsing, user input handling  

## 📂 Project Structure
personal_finance/
│
├── main.py
├── data.txt
└── README.md

🧾 How Data is Stored

Each transaction is stored in the following format inside data.txt:
INCOME:23.0 salary
EXPENSE:100.0 fees
This allows easy parsing to:
	•	Identify transaction type (INCOME / EXPENSE)
	•	Extract amount
	•	Maintain transaction history
▶️ How to Run
	1.	Clone or download the repository
	2.	Navigate to the project directory
	3.	Run the program:
         using python3 main.py
📋 Menu Options
    1. Add Income
    2. Add Expense
    3. Show Balance
    4. Show History
    5. Exit 
📈 Sample Output
Welcome to the expense tracker
1. Add Income
2. Add Expense
3. Show Balance
4. Show History
5. Exit

Transaction History:
INCOME: 23.0 - salary
EXPENSE: 100.0 - fees

Current Balance: -77.0



🧠 Learning Outcomes
	•	Practical understanding of file-based data persistence
	•	Parsing structured text data
	•	Building menu-driven CLI applications
	•	Writing clean and modular Python code

⸻

🔮 Future Enhancements
	•	Expense categorization
	•	Spending pattern analysis
	•	Graphical visualization (charts & graphs)
	•	Database integration
	•	GUI or web-based interface

⸻

👤 Author

Mittapally Sai Adarsh
B.Tech CSE, NIT Silchar
Email: saiadarsh.work@gmail.com
LinkedIn: https://www.linkedin.com/in/sai-adarsh-mittapally-523b98325    
