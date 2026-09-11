# Skills Test

from pyscript import document

# Menu and prices
menu = {
    "Original Chewy Cookie": 85.00,
    "Pistachio Knafeh Dubai Cookie": 150.00,
    "Dark Chocolate Dubai Cookie": 130.00,
    "White Chocolate Biscoff Dubai Cookie": 140.00,
    "Matcha Dubai Cookie": 135.00
}


# This runs when Create Order is clicked
def create_order(event):

    subtotal = 0
    selected_items = []

    # Check which cookies were selected
    if document.getElementById("original").checked:
        selected_items.append("Original Chewy Cookie")
        subtotal += menu["Original Chewy Cookie"]

    if document.getElementById("pistachio").checked:
        selected_items.append("Pistachio Knafeh Dubai Cookie")
        subtotal += menu["Pistachio Knafeh Dubai Cookie"]

    if document.getElementById("dark").checked:
        selected_items.append("Dark Chocolate Dubai Cookie")
        subtotal += menu["Dark Chocolate Dubai Cookie"]

    if document.getElementById("white").checked:
        selected_items.append("White Chocolate Biscoff Dubai Cookie")
        subtotal += menu["White Chocolate Biscoff Dubai Cookie"]

    if document.getElementById("matcha").checked:
        selected_items.append("Matcha Dubai Cookie")
        subtotal += menu["Matcha Dubai Cookie"]


    # Calculate VAT
    vat = subtotal * 0.12

    # Calculate total
    total = subtotal + vat


    # Create the receipt
    receipt = "<p>Selected Items:</p>"

    for item in selected_items:
        receipt += f"<p>{item} - ₱{menu[item]:.2f}</p>"

    receipt += f"<p>Subtotal: ₱{subtotal:.2f}</p>"
    receipt += f"<p>VAT (12%): ₱{vat:.2f}</p>"
    receipt += f"<p><b>Total: ₱{total:.2f}</b></p>"


    # Display the receipt
    document.getElementById("receipt").innerHTML = receipt


# Connect the button to the Python function
document.getElementById("order").onclick = create_order