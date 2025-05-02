def place_order(item, quantity):
    menu = {"burger": 10, "pizza": 5}
    try:
        if item not in menu:
            raise ValueError(f"{item} is not on the menu!")
        if menu[item] < quantity:
            raise Exception(f"Only {menu[item]} {item}(s) left!")
        menu[item] -= quantity
        print(f"Order placed: {quantity} {item}(s)!")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Order logged.")

place_order("pizza", 6)  # Oops, not enough stock!