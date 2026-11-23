def product_details(product_id, product_name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {product_name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )


if __name__ == "__main__":
    print(product_details(101, "Laptop", 2, 45000))
