"""
Find the total sales for each product across all stores.
Identify the store with the highest total sales (sum of all products).
Find the best-selling product (i.e., the product with the highest total sales).
Sort the stores based on their total sales in descending order and print the sorted result.
"""
sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5
    }
}

st = {}
prod = {}

def total_sales(sales_data):
    """
        Here we will pass the sales data dictonary then we will access the detials of stores and its details 
        then we will count for occurence of each product in each store and do total and return a dictonary 
        for total no of sales of each product
    """
    for stores, values in sales_data.items():
        for product, sales in values.items():
            if prod.get(product):
                prod[product] += sales
            else:
                prod[product] = sales
    return prod

def highest_saleproduct(data):
    """
        From the above function we got a dictonary of sales of each product and then we would check the data with 
        max function to get the max value of highest sales product which will name of product with highest sales
        and no of sales 
    """
    highest_sale = max(data, key = lambda i : data[i])
    return highest_sale, data[highest_sale]


def highest_salestore(data):
    """
    Here we will pass the sales data dictonary then we will access the detials of stores and its details 
    then we will count for total no of sales of each store and then find the max out of it and return a 
    highest sale store, with no of products and dictonary for total no of sales
    """
    for stores, values in data.items():
        for product, sales in values.items():
            if st.get(stores):
                st[stores] += sales 
            else:
                st[stores] = sales
    highest = max(st, key=lambda i: st[i])
    return highest, st[highest],st

def sorting(data):
    """ 
    From the above method we got the total no of sales then using sorted method we will sort the data and 
    return it back as dictonary
    """
    sorted_stores = dict(sorted(data.items(), key = lambda i : i[1], reverse=True))
    return sorted_stores

totalsales = total_sales(sales_data)
highestsalestore, sale, storedetails= highest_salestore(sales_data)
highestsaleproduct, product_name = highest_saleproduct(totalsales)
sort = sorting(storedetails)

print(f"\n 1) Total no of Products sold {totalsales}")
print(f"\n 2) Store with highest no of sales is {highestsalestore} with no of sales {sale}")
print(f"\n 3) Product with highest no of sales is {highestsaleproduct} with no of sales {product_name}")
print(f"\n 4) Stores with highest sales in descending order : {sort}\n")
