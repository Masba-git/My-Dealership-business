# Import the fuel cost calculator from bike_fuel_cost.py
from bike_fuel_cost import calculator_fuel_cost

# Define product details
products = {
    "B.Coffee": {"buying_price": 360},
    "B.Red": {"buying_price": 240},
    "C.Milk": {"buying_price": 330},
    "C.Red": {"buying_price": 230},
    "C.Coffee": {"buying_price": 350},
}

def calculate_profit():
    print("\nWelcome to the Profit Calculator!\n")
    total_profit_from_products = 0  # Tracks profit from products only
    total_selling_price = 0  # Tracks total selling price
    total_product_cost = 0  # Tracks total buying cost

    while True:
        # Display product list
        print("Available products:")
        for index, product in enumerate(products.keys(), start=1):
            print(f"{index}. {product}")
        
        # Input product number
        try:
            product_number = int(input("\nEnter the product number (or 0 to finish): "))
            if product_number == 0:
                break
            product_name = list(products.keys())[product_number - 1]
        except (ValueError, IndexError):
            print("Invalid product number. Please try again.")
            continue
        
        # Input quantity
        try:
            quantity = int(input(f"Enter the quantity for {product_name}: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Please enter a positive integer.")
            continue
        
        # Input selling price
        try:
            selling_price = float(input(f"Enter the selling price for {product_name}: "))
            if selling_price <= 0:
                raise ValueError
        except ValueError:
            print("Invalid selling price. Please enter a positive number.")
            continue
        
        # Calculate profit for the product
        buying_price = products[product_name]["buying_price"]
        product_cost = buying_price * quantity  # Total cost for the product
        profit = (selling_price - buying_price) * quantity
        
        total_profit_from_products += profit
        total_selling_price += selling_price * quantity  # Add to total selling price
        total_product_cost += product_cost  # Add to total buying cost
        
        print(f"Profit for {product_name}: {profit:.2f}\n")
    
    # Get the bike fuel cost
    try:
        distance = float(input("Enter the distance traveled for delivery (in km): "))
        if distance >= 0:
            fuel_cost = calculator_fuel_cost(distance)
            print(f"Fuel cost for traveling {distance} km: {fuel_cost:.2f} Tk")
        else:
            print("Distance cannot be negative. Skipping fuel cost calculation.")
            fuel_cost = 0
    except ValueError:
        print("Invalid input for distance. Skipping fuel cost calculation.")
        fuel_cost = 0

    # Calculate actual profit after deducting fuel cost
    actual_profit_after_fuel = total_profit_from_products - fuel_cost

    # Display results
    print(f"\nTotal selling price: {total_selling_price:.2f} Tk")
    print(f"Total product cost: {total_product_cost:.2f} Tk")
    print(f"Total profit from products: {total_profit_from_products:.2f} Tk")
    print(f"Fuel cost deducted: {fuel_cost:.2f} Tk")
    print(f"Actual profit after fuel cost: {actual_profit_after_fuel:.2f} Tk\n")
    print("Thank you for using the Profit Calculator!")

# Run the program
if __name__ == "__main__":
    calculate_profit()
