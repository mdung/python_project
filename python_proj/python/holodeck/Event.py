# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data for events and bookings
events = [
    {"id": 1, "name": "Birthday Party"},
    {"id": 2, "name": "Wedding"},
    {"id": 3, "name": "Corporate Gathering"},
    # Add more events as needed
]

bookings = []

# Home route
@app.route('/')
def home():
    return render_template('index.html', events=events)

# Event details route
@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = next((e for e in events if e["id"] == event_id), None)
    return render_template('event_details.html', event=event)

# Booking route
@app.route('/book/<int:event_id>', methods=['POST'])
def book(event_id):
    event = next((e for e in events if e["id"] == event_id), None)
    participant_name = request.form.get('participant_name')

    # In a real app, you would perform the booking process here
    # This could involve handling payments, confirming availability, etc.

    booking = {"event": event["name"], "participant": participant_name}
    bookings.append(booking)

    return redirect(url_for('booking_success', booking_id=len(bookings)))

# Booking success route
@app.route('/booking-success/<int:booking_id>')
def booking_success(booking_id):
    booking = bookings[booking_id - 1]
    return render_template('booking_success.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True)
