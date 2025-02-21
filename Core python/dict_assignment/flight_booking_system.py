# ✈️ Flight Booking System

# 🟢 Step 1: Define available seats (Dictionary where keys are seat numbers and values are availability)
available_seats = {
    "1A": True,
    "1B": True,
    "1C": True,
    "2A": True,
    "2B": True,
    "2C": True
}

# 🔄 Step 2: Function to display available seats
def display_seats():
    print("\n💺 Available Seats:")
    for seat, is_available in available_seats.items():
        status = "Available" if is_available else "Booked"
        print(f"Seat {seat}: {status}")

# 🛫 Step 3: Function to book a seat
def book_seat(seat_number):
    if seat_number in available_seats:  # Check if the seat exists
        if available_seats[seat_number]:  # Check if the seat is available
            available_seats[seat_number] = False  # Book the seat (set to False)
            print(f"\n✅ Seat {seat_number} has been successfully booked.")
        else:
            print(f"\n❌ Seat {seat_number} is already booked.")
    else:
        print(f"\n❌ Invalid seat number. Please choose a valid seat.")

# 🔄 Step 4: Main Program Loop
while True:
    display_seats()  # Show current seat status
    choice = input("\n🎫 Enter seat number to book (or 'exit' to stop): ").upper()

    if choice == "EXIT":
        print("\n✈️ Thank you for using the Flight Booking System. Safe travels!")
        break  # Exit the loop

    book_seat(choice)  # Attempt to book the chosen seat
