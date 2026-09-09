# Currency-Converter
curency

## WHAT IT IS!!!!
In this Lab we wrote code to make a currency converter that uses USD as a baseline. The converter should be able to add custom currencies to the already existing list.

## CODE

The following code is what i wrote inside of ```currency_converter.py```:

```python
import time
import sys
class currency_converter:
    def __init__(self, exchange_rates=None):
        self.exchange_rates = exchange_rates or {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.78,
            "JPY": 150.50,
            "INR": 83.30,
        }
    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("nNOT IN KNOWN EXCHANGE RATES")
        converted = amount * (self.exchange_rates[to_currency] / self.exchange_rates[from_currency])
        return round(converted, 2)
    def add_rate(self, currency, rate):
        if currency in self.exchange_rates:
            raise ValueError("no, already in there sonion")
        self.exchange_rates[currency] = float(rate)

converter = currency_converter()
def user_questions ():
    what = input("WHICH DO YOU WANNA DO\n============================\n\n1) CONVERT CURRENCY\n2) ADD CURENCY CONVERSION\n3) EXIT :(\n->")
    if what == "1":
        print(f"RATES:\n{converter.exchange_rates}")
        try:
            converting = float(input("HOW MUCH IS BEING CONVERTED: "))
            start = input("FROM WHAT CURRENCY (USE ABBREVIATIONS): ").upper()
            end = input("TO WHAT CURRENCY (USE ABBREVIATIONS): ").upper()
            converted = converter.convert(converting, start, end)
            print(f"{converting:.2f} {start} is {converted:.2f} {end}")
        except ValueError:
            print("idk what wrong twin")
            user_questions()
        user_questions()

    elif what == "2":
        try:
            print(f"RATES:\n{converter.exchange_rates}")
            currency = input("WHAT CURRENCY YOU WANT? (USE ABBREVIATIONS): ").upper()
            rate = float(input("WHAT IS THE RATE????? (TO USD): "))
            converter.add_rate(currency, rate)
            print(f"added{currency} as {converter.exchange_rates[currency]}")
        except ValueError:
            print("couldnt add, sonion")
        user_questions()


    elif what == "3":
        print("exiting...")
        time.sleep(1)
        sys.exit("im done with you...")
    else:
        print("NONONONON ON ONON ONNON NOOO YOU CANT DO TAT")
        user_questions()


if __name__ == "__main__":
    user_questions()
```

### HOW TO USE:
1) When executing the code, you will be met with the following interface:
```
WHICH DO YOU WANNA DO
============================

1) CONVERT CURRENCY
2) ADD CURENCY CONVERSION
3) EXIT 😢
->
```
2) input the numbers to use the currency converter.
    - inputting "1" will give the following prompts, they have been filled out with an example:
    ```
    RATES:
    {'USD': 1.0, 'EUR': 0.92, 'GBP': 0.78, 'JPY': 150.5, 'INR': 83.3}
    HOW MUCH IS BEING CONVERTED: 1000
    FROM WHAT CURRENCY (USE ABBREVIATIONS): usd
    TO WHAT CURRENCY (USE ABBREVIATIONS): JPY
    1000.00 USD is 150500.00 JPY
    ```
    - inputting "2" will give the following prompts, they have been filled out with an example:
    ```
    {'USD': 1.0, 'EUR': 0.92, 'GBP': 0.78, 'JPY': 150.5, 'INR': 83.3}
    WHAT CURRENCY YOU WANT TO ADD? (USE ABBREVIATIONS): sonion
    WHAT IS THE RATE????? (TO USD): 342  
    added SONION as 342.0
    ```
3) inputting "3" will exit the program but won't save the currencies that you have added. It outputs the following statement:
```
exiting...
im done with you...
```

## SETTING UP AUDTOMATIC TESTS WITH GITHUB ACTIONS

To make automatic tests with GitHubActions, you first need to have ```pytest``` installed. If you do not have ```pytest``` installed use the command ```pip install pytest``` first. In the same folder as your test 

![alt text](<Screenshot From 2026-09-04 14-57-45.png>)