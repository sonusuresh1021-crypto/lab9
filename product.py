def product_details(product_id, name, quantity, price):
     return (
        f"Product ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: Rs.{price}"
        )
        print(product_details(101, "Laptop", 2, 45000))