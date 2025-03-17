products = [
    ["audi", 90],
    ["bmw", 30],
    ["tričko", 1],
]

products2 = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    }
]

def print_products():
    for product in products:
        print(f"Název produktu: {product[0]}, cena: {product[1]}$d")
    for product in products2:
        print(f"Název produktu: {product['name']}, cena: {product['price']}$")

def add_product():
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product = [product_name, product_price]
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product)

def menu():
    print("Vítej ve skladu")
    print("#################\n")
    print("1. výpis položek")
    print("2. Přidání položky\n")

    choice = int(input("Volba: "))
    if choice == 1:
        print("Výpis položek")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky")
        add_product()
        print("")
        menu()

    else:
        print("něco jiného")
        menu()


menu()