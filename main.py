import tkinter as tk
from tkinter import messagebox, font
from booking import BookingManager

# Backend object
manager = BookingManager()

# ---------------- COLOURS ----------------

BG = "#E4EFF6"
WHITE = "#FFFFFF"
BLUE = "#3F7299"
DARK_BLUE = "#203B56"
LIGHT_BLUE = "#F5F9FC"
TEXT = "#34495E"
GREEN = "#648B78"
RED = "#B96B6B"
GREY = "#718096"

# ---------------- FUNCTIONS ----------------

# Add Booking
def add_booking():

    bid = booking_id.get().strip()
    name = customer_name.get().strip()
    guest = guests.get()
    day = days.get()

    if bid == "" or name == "":
        messagebox.showerror(
            "Error",
            "Booking ID and Customer Name are required!"
        )
        return

    if manager.search_booking(bid) is not None:
        messagebox.showerror(
            "Error",
            "Booking ID already exists!"
        )
        return

    try:
        guest = int(guest)
        day = int(day)

        if guest <= 0 or day <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter valid positive numbers for Guests and Days!"
        )
        return

    result = manager.add_booking(
        bid,
        name,
        guest,
        day,
        room_type.get(),
        facility.get()
    )

    if result:
        messagebox.showinfo(
            "Success",
            "Booking added successfully!"
        )
        display_bookings()
        clear_form()

# Search Booking
def search_booking():

    bid = booking_id.get().strip()

    if bid == "":
        messagebox.showerror(
            "Error",
            "Enter Booking ID!"
        )
        return

    data = manager.search_booking(bid)

    if data is not None:

        clear_form()

        booking_id.insert(0, bid)
        customer_name.insert(0, data["name"])
        guests.insert(0, str(data["guests"]))
        days.insert(0, str(data["days"]))

        room_type.set(data["room"])
        facility.set(data["facility"])

        messagebox.showinfo(
            "Success",
            "Booking found!"
        )

    else:
        messagebox.showerror(
            "Error",
            "Booking not found!"
        )

# Update Booking
def update_booking():

    bid = booking_id.get().strip()
    name = customer_name.get().strip()
    guest = guests.get()
    day = days.get()

    if manager.search_booking(bid) is None:
        messagebox.showerror(
            "Error",
            "Booking ID not found!"
        )
        return

    if name == "":
        messagebox.showerror(
            "Error",
            "Customer Name is required!"
        )
        return

    try:
        guest = int(guest)
        day = int(day)

        if guest <= 0 or day <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter valid positive numbers!"
        )
        return

    result = manager.update_booking(
        bid,
        name,
        guest,
        day,
        room_type.get(),
        facility.get()
    )

    if result:
        messagebox.showinfo(
            "Success",
            "Booking updated successfully!"
        )
        display_bookings()
        clear_form()

# Cancel Booking
def cancel_booking():

    bid = booking_id.get().strip()

    if bid == "":
        messagebox.showerror(
            "Error",
            "Enter Booking ID!"
        )
        return

    if manager.search_booking(bid) is not None:

        answer = messagebox.askyesno(
            "Confirm",
            "Do you want to cancel this booking?"
        )

        if answer:
            manager.cancel_booking(bid)

            messagebox.showinfo(
                "Success",
                "Booking cancelled!"
            )

            display_bookings()
            clear_form()

    else:
        messagebox.showerror(
            "Error",
            "Booking not found!"
        )

# Calculate Table Column Widths
def get_column_widths():

    available_width = max(booking_list.winfo_width() - 25, 700)
    char_width = table_font.measure("0")

    total_chars = max(85, int(available_width / char_width))

    widths = [
        int(total_chars * 0.16),
        int(total_chars * 0.23),
        int(total_chars * 0.12),
        int(total_chars * 0.12),
        int(total_chars * 0.19),
        int(total_chars * 0.18)
    ]

    widths[-1] += total_chars - sum(widths)

    return widths

# Format Table Rows
def format_row(values, widths):

    return "".join(
        str(value)[:width - 1].ljust(width)
        for value, width in zip(values, widths)
    )

# Display All Bookings
def display_bookings():

    booking_list.delete(0, tk.END)

    all_bookings = manager.get_all_bookings()
    widths = get_column_widths()

    columns = [
        "BOOKING ID",
        "CUSTOMER NAME",
        "GUESTS",
        "DAYS",
        "ROOM TYPE",
        "FACILITY"
    ]

    heading.config(text=format_row(columns, widths))

    for bid, data in all_bookings.items():

        details = [
            bid,
            data["name"],
            data["guests"],
            data["days"],
            data["room"],
            data["facility"]
        ]

        booking_list.insert(
            tk.END,
            format_row(details, widths)
        )

    total_label.config(
        text="Total Bookings: " + str(len(all_bookings))
    )

# Select Booking from List
def select_booking(event):

    selected = booking_list.curselection()

    if selected:

        index = selected[0]
        bid = list(manager.get_all_bookings().keys())[index]

        data = manager.search_booking(bid)

        if data is not None:

            clear_form()

            booking_id.insert(0, bid)
            customer_name.insert(0, data["name"])
            guests.insert(0, str(data["guests"]))
            days.insert(0, str(data["days"]))

            room_type.set(data["room"])
            facility.set(data["facility"])

# Clear Form
def clear_form():

    booking_id.delete(0, tk.END)
    customer_name.delete(0, tk.END)
    guests.delete(0, tk.END)
    days.delete(0, tk.END)

    room_type.set("Single")
    facility.set("AC")

    booking_list.selection_clear(0, tk.END)

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Hotel Room Booking System")
root.geometry("1050x780")
root.minsize(900, 700)
root.configure(bg=BG)

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="HOTEL ROOM BOOKING SYSTEM",
    font=("Arial", 23, "bold"),
    bg=BLUE,
    fg=WHITE,
    pady=20
)

title.pack(fill="x")

subtitle = tk.Label(
    root,
    text="Manage Your Hotel Reservations",
    font=("Arial", 11),
    bg=BG,
    fg=DARK_BLUE
)

subtitle.pack(pady=10)

# ---------------- BOOKING FORM ----------------

form_frame = tk.Frame(
    root,
    bg=WHITE,
    padx=25,
    pady=20
)

form_frame.pack(
    padx=35,
    pady=10,
    fill="x"
)

tk.Label(
    form_frame,
    text="BOOKING DETAILS",
    font=("Arial", 14, "bold"),
    bg=WHITE,
    fg=BLUE
).grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="w",
    pady=10
)

# Label Function
def create_label(text, row, column):

    tk.Label(
        form_frame,
        text=text,
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).grid(
        row=row,
        column=column,
        padx=10,
        pady=10,
        sticky="w"
    )

# Entry Function
def create_entry(row, column):

    entry = tk.Entry(
        form_frame,
        font=("Arial", 11),
        width=25,
        bd=1,
        relief="solid",
        bg=LIGHT_BLUE
    )

    entry.grid(
        row=row,
        column=column,
        padx=10,
        pady=10,
        ipady=4
    )

    return entry

# Booking ID
create_label("Booking ID", 1, 0)
booking_id = create_entry(1, 1)

# Customer Name
create_label("Customer Name", 1, 2)
customer_name = create_entry(1, 3)

# Guests
create_label("Number of Guests", 2, 0)
guests = create_entry(2, 1)

# Days
create_label("Number of Days", 2, 2)
days = create_entry(2, 3)

# Room Type
create_label("Room Type", 3, 0)

room_type = tk.StringVar(value="Single")

room_menu = tk.OptionMenu(
    form_frame,
    room_type,
    "Single",
    "Double",
    "Deluxe",
    "Suite"
)

room_menu.config(
    bg=LIGHT_BLUE,
    fg=DARK_BLUE,
    font=("Arial", 10),
    width=18,
    relief="flat"
)

room_menu.grid(
    row=3,
    column=1,
    padx=10,
    pady=10,
    sticky="w"
)

# Facility
create_label("Room Facility", 3, 2)

facility = tk.StringVar(value="AC")

radio_frame = tk.Frame(form_frame, bg=WHITE)
radio_frame.grid(
    row=3,
    column=3,
    sticky="w"
)

tk.Radiobutton(
    radio_frame,
    text="AC",
    variable=facility,
    value="AC",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 10),
    activebackground=WHITE
).pack(side="left")

tk.Radiobutton(
    radio_frame,
    text="Non-AC",
    variable=facility,
    value="Non-AC",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 10),
    activebackground=WHITE
).pack(side="left")

# ---------------- BUTTONS ----------------

button_frame = tk.Frame(root, bg=BG)
button_frame.pack(pady=12)

def create_button(text, command, color, column):

    tk.Button(
        button_frame,
        text=text,
        command=command,
        bg=color,
        fg=WHITE,
        activebackground=DARK_BLUE,
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        width=15,
        height=2,
        relief="flat",
        cursor="hand2"
    ).grid(
        row=0,
        column=column,
        padx=5
    )

create_button("ADD", add_booking, BLUE, 0)
create_button("SEARCH", search_booking, GREEN, 1)
create_button("UPDATE", update_booking, BLUE, 2)
create_button("CANCEL", cancel_booking, RED, 3)
create_button("CLEAR", clear_form, GREY, 4)

# ---------------- BOOKING RECORDS ----------------

records_frame = tk.Frame(
    root,
    bg=WHITE,
    padx=20,
    pady=15
)

records_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=10
)

tk.Label(
    records_frame,
    text="BOOKING RECORDS",
    font=("Arial", 14, "bold"),
    bg=WHITE,
    fg=BLUE
).pack(anchor="w", pady=5)

total_label = tk.Label(
    records_frame,
    text="Total Bookings: 0",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=GREEN
)

total_label.pack(anchor="e")

# Table Fonts
table_font = font.Font(
    family="Courier New",
    size=13
)

heading_font = font.Font(
    family="Courier New",
    size=11,
    weight="bold"
)

# Column Headings
heading = tk.Label(
    records_frame,
    text="",
    font=heading_font,
    bg=BLUE,
    fg=WHITE,
    anchor="w",
    padx=8,
    pady=10
)

heading.pack(fill="x", pady=(8, 0))

# Listbox and Scrollbar
list_frame = tk.Frame(records_frame, bg=LIGHT_BLUE)
list_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

booking_list = tk.Listbox(
    list_frame,
    font=table_font,
    bg=LIGHT_BLUE,
    fg=TEXT,
    selectbackground=BLUE,
    selectforeground=WHITE,
    height=6,
    relief="flat",
    yscrollcommand=scrollbar.set
)

booking_list.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.config(command=booking_list.yview)

booking_list.bind(
    "<<ListboxSelect>>",
    select_booking
)

# Adjust Table When Window Is Resized
booking_list.bind(
    "<Configure>",
    lambda event: display_bookings()
)

# ---------------- FOOTER ----------------

tk.Label(
    root,
    text="Select a booking to view or edit details.",
    font=("Arial", 9, "italic"),
    bg=BG,
    fg=GREY
).pack(pady=8)

# Load Existing Bookings
display_bookings()

# Run Application
root.mainloop()
