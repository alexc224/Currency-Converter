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