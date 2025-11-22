This project is a simple and interactive Currency Converter Application built using Python’s Tkinter GUI framework and the CurrencyConverter library.
It allows users to convert any amount from one currency to another with real-time exchange rates.

 
Features:
 User-friendly Tkinter Interface
 Convert between any global currencies (USD, INR, EUR, GBP, AUD, etc.)
 Automatic fetching of exchange rates
 Safe error handling for invalid inputs
 Clean and organized UI layout
 Works offline after initial rate download

 Requirements
   Install the required package:
   pip install currencyconverter

Tkinter is included by default with Python on:
   Windows ️
   macOS

currency-converter/
│
├── currency_converter_app.py   # Main Tkinter program
└── README.md                   # Project documentation

How to Run the Application
Save your Python script as:
currency_converter_app.py


Open your terminal or command prompt.
Run the program:
python currency_converter_app.py

The Currency Converter GUI window will open.
Enter:
Amount
Currency to convert from
Currency to convert to
Click Convert.


GUI Overview

The GUI is built using Tkinter widgets:

Widget	Purpose
Label	Titles and instructions
Entry	Input fields for amount & currency codes
Button	Triggers conversion
grid()	Arranges components neatly

The layout is simple, centered, and easy to interact with.



Example Output

If you enter:

Amount: 100
From: USD
To: INR

The output might look like:
100 USD = 8320.15 INR


1. Invalid Amount
Example:
abc
Displays:
X Please enter valid number
2. Invalid Currency Code
Example:
USDD
