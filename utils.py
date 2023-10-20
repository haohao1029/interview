# utils.py
from database import get_items, update_item, create_transaction
import datetime
def calculate_change(amount_paid, price):
    notes = [100, 20, 10, 5, 1]
    change = amount_paid - price
    change_notes = {}
    for note in notes:
        if change >= note:
            qty = change // note
            change_notes[note] = qty
            change -= note * qty
    return change_notes

def vending_machine_transaction(item_id, amount_paid):
    items = get_items()
    print(items)
    item = next((item for item in items if item[0] == item_id), None)
    if not item:
        return "Item not found"
    if item[3] <= 0:
        return "Item out of stock"
    if amount_paid < item[2]:
        return "Insufficient amount paid"
    change = calculate_change(amount_paid, item[2])
    update_item(item_id, quantity=item[3]-1)
    date = datetime.datetime.now().isoformat()

    create_transaction(item_id, amount_paid,date)
    return f"Transaction successful. Change to be returned: {change}"
