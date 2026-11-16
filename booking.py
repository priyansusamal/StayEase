
import json
import os


class BookingManager:

    def __init__(self):
        self.bookings = {}
        self.filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "bookings.json"
        )

        self.load_bookings()

    # LOAD BOOKINGS FROM JSON FILE
    def load_bookings(self):

        if os.path.exists(self.filename):

            try:
                with open(self.filename, "r") as file:
                    self.bookings = json.load(file)

                if not isinstance(self.bookings, dict):
                    self.bookings = {}

            except (json.JSONDecodeError, OSError):
                self.bookings = {}

        else:
            self.bookings = {}

    # SAVE BOOKINGS TO JSON FILE
    def save_bookings(self):

        with open(self.filename, "w") as file:
            json.dump(self.bookings, file, indent=4)

    # ADD BOOKING
    def add_booking(self, bid, name, guests, days, room, facility):

        if bid in self.bookings:
            return False

        self.bookings[bid] = {
            "name": name,
            "guests": guests,
            "days": days,
            "room": room,
            "facility": facility
        }

        self.save_bookings()
        return True

    # SEARCH BOOKING
    def search_booking(self, bid):

        return self.bookings.get(bid)

    # UPDATE BOOKING
    def update_booking(self, bid, name, guests, days, room, facility):

        if bid not in self.bookings:
            return False

        self.bookings[bid] = {
            "name": name,
            "guests": guests,
            "days": days,
            "room": room,
            "facility": facility
        }

        self.save_bookings()
        return True

    # CANCEL BOOKING
    def cancel_booking(self, bid):

        if bid in self.bookings:

            del self.bookings[bid]
            self.save_bookings()

            return True

        return False

    # DISPLAY ALL BOOKINGS
    def get_all_bookings(self):

        return self.bookings
