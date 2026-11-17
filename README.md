
# Hotel Room Booking Management System

## Project Overview

The Hotel Room Booking Management System is a Python-based desktop application developed using Tkinter. It provides a simple graphical interface to manage hotel room reservations efficiently.

The application allows users to add, search, update, cancel and display hotel bookings. It also uses JSON file handling to store booking information permanently.

## Team Members

1. Antony Joel A
2. Priyansu Samal
3. Aritra Saha

## Technologies Used

- Python
- Tkinter (GUI Development)
- JSON (Data Storage)
- Object-Oriented Programming
- File Handling

## Features

### 1. Add Booking
- Add new hotel reservations.
- Enter Booking ID and Customer Name.
- Specify the number of guests and days.
- Select room type and room facility.
- Prevent duplicate Booking IDs.

### 2. Search Booking
- Search for an existing booking using Booking ID.
- Display the corresponding booking details.

### 3. Update Booking
- Modify existing customer and room details.
- Update the booking information.

### 4. Cancel Booking
- Cancel an existing reservation.
- Remove the cancelled booking from the records.

### 5. Display All Bookings
- Display all existing reservations in a Listbox.
- View booking details in the application.

### 6. Input Validation
- Booking ID cannot be empty.
- Customer Name cannot be empty.
- Number of Guests must be a positive integer.
- Number of Days must be a positive integer.
- Duplicate Booking IDs are not allowed.

### 7. Permanent Data Storage
- Store booking records in a JSON file.
- Automatically save changes when bookings are added, updated or cancelled.
- Load previously saved bookings when the application starts.

## Project Structure

```text
Hotel_Room_Booking_System/
│
├── main.py
├── booking.py
├── bookings.json
└── README.md
```

### File Description

- **main.py:** Contains the Tkinter graphical user interface and connects user actions to the booking operations.
- **booking.py:** Contains the BookingManager class responsible for managing booking records.
- **bookings.json:** Stores booking information permanently in JSON format.
- **README.md:** Contains project information and instructions.

## Installation and Execution

### Prerequisites

- Python 3.x
- Tkinter (included with most standard Python installations)

### Steps to Run

1. Download or clone the project.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. The Hotel Room Booking Management System GUI will open.

## Data Storage

The application uses a Python dictionary to manage booking records during execution.

The JSON module is used to save and retrieve booking information from `bookings.json`.

This ensures that booking records remain available even after closing and reopening the application.

## Conclusion

The Hotel Room Booking Management System provides a simple and efficient way to manage hotel reservations through a graphical interface.

The project demonstrates Python programming concepts, Object-Oriented Programming, GUI development using Tkinter, input validation, CRUD operations and JSON file handling.
