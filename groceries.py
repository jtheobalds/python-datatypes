from IPython import embed

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)

# TODO: write some Python code here to produce the desired output
#print(type(products))
#print(products[0]) #prints the first product in the list
#print(products[0]["name"]) #prints the name of the first products

first_product = products[0]
#print(type(first_product))
#this is a dictionary; the entire products list is a list of dictionaries
#print(first_product["name"])
#print(len(products)) #prints the number of products in the list
#to print the name of each product, want to loop throught the lise
#for prod in products:
#    print(prod["name"])

product_count_message = "THERE ARE " + str(len(products)) + " PRODUCTS:"
print("--------------")
print(product_count_message)
print("--------------")

def sort_by_name(prod):
    return prod["name"]

products = sorted(products, key=sort_by_name)

for prod in products:
    rprice = "(${0:.2f})".format(prod["price"])
    print(" + " + prod["name"] + rprice)

#PRINT DEPARTMENTS
departments = []

for prod in products:
    departments.append(prod["department"])
#print(departments)
#REMOVE DUPLICATES
departments = set(departments)
departments = list(departments)

#SORT DEPARTMENTS
departments.sort()

#dept_count_message = "THERE ARE " + str(len(department)) + " DEPARTMENTS"
print("--------------")
print("THERE ARE " + str(len(departments)) + " DEPARTMENTS")
print("--------------")

def products_belonging_to(dept_name):
    return[p for p in products if p["department"] == dept_name] #TODO look up all products belonging to dept

for d in departments:
    associated_products = products_belonging_to(d)
    label = "products"
    if len(associated_products) == 1:
        label = "product"
    print (" + " + d.title() + " (" + str(len(associated_products)) + " " + label + ")")
