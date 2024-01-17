# Define a list of dictionaries for cars
cars = [
    {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue', 'motor_type': 'Gasoline', 'price': 25000},
    {'make': 'Honda', 'model': 'Civic', 'year': 2019, 'color': 'Red', 'motor_type': 'Hybrid', 'price': 22000},
    {'make': 'Ford', 'model': 'Mustang', 'year': 2022, 'color': 'Yellow', 'motor_type': 'Gasoline', 'price': 35000},
    {'make': 'Chevrolet', 'model': 'Malibu', 'year': 2021, 'color': 'Silver', 'motor_type': 'Electric', 'price': 30000},
    {'make': 'Tesla', 'model': 'Model 3', 'year': 2023, 'color': 'Black', 'motor_type': 'Electric', 'price': 45000}
]

# Function to sort cars by a specified key
def sort_cars_by_key(cars_list, key):
    return sorted(cars_list, key=lambda x: x[key])

# Get user input for sorting criterion
sorting_criterion = input("Enter sorting criterion (make, model, year, color, motor_type, price): ")

# Check if the entered sorting criterion is valid
if sorting_criterion in cars[0].keys():
    # Sort the list of cars based on the user-specified criterion
    sorted_cars = sort_cars_by_key(cars, sorting_criterion)

    # Print information about each sorted car
    print(f"Cars sorted by {sorting_criterion}:")
    for car in sorted_cars:
        print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, Color: {car['color']}, Motor Type: {car['motor_type']}, Price: ${car['price']}")
else:
    print("Invalid sorting criterion. Please choose a valid criterion.")