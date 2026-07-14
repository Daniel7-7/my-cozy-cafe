from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    booking_message = ""
    
    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        guest_count = request.form.get("guest_count")
        booking_time = request.form.get("booking_time")
        # 🌟 Here is your new phone field caught by Python!
        customer_phone = request.form.get("customer_phone")
        
        if customer_name and guest_count and booking_time and customer_phone:
            # 🌟 Updated message to include your new feature
            booking_message = f"☕ Reservation Confirmed for {customer_name}! Table for {guest_count} at {booking_time}. We will text updates to {customer_phone}."
            
    return render_template("index.html", message=booking_message)

if __name__ == "__main__":
    app.run(debug=True)