import csv

def log_load():
    print("=== New Load Entry ===")
    date = input("Date (YYYY-MM-DD): ")
    customer = input("Customer: ")
    origin = input("Origin: ")
    destination = input("Destination: ")
    miles = input("Miles: ")
    rate = input("Rate ($): ")
    expenses = input("Expenses ($): ")
    profit = float(rate) - float(expenses)
    return [date, customer, origin, destination, miles, rate, expenses, profit]

def save_load(load, filename='trucking_loads.csv'):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(load)

def main():
    print("Welcome to the Trucking & Load Tracker")
    while True:
        load = log_load()
        save_load(load)
        print(f"Saved! Profit for this load: ${load[-1]:.2f}")
        cont = input("Log another? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
