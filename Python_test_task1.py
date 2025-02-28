import pandas as pd
sale_data = [
 {'category': 'Toys', 'item': 'Doll', 'price': 185, 'quantity': 8},
 {'category': 'Clothing', 'item': 'Jeans', 'price': 386, 'quantity': 10},
 {'category': 'Books', 'item': 'Novel', 'price': 212, 'quantity': 4},
 {'category': 'Clothing', 'item': 'Hat', 'price': 951, 'quantity': 1},
 {'category': 'Books', 'item': 'Novel', 'price': 397, 'quantity': 9},
 {'category': 'Electronics', 'item': 'Smartwatch', 'price': 601, 'quantity': 9},
 {'category': 'Toys', 'item': 'Action Figure', 'price': 753, 'quantity': 5},
 {'category': 'Clothing', 'item': 'Jeans', 'price': 312, 'quantity': 9},
 {'category': 'Sports', 'item': 'Football', 'price': 382, 'quantity': 8},
 {'category': 'Books', 'item': 'Comic Book', 'price': 512, 'quantity': 1},
 {'category': 'Sports', 'item': 'Gym Bag', 'price': 17, 'quantity': 1},
 {'category': 'Electronics', 'item': 'Phone', 'price': 909, 'quantity': 4},
 {'category': 'Home & Kitchen', 'item': 'Toaster', 'price': 577, 'quantity': 10},
 {'category': 'Toys', 'item': 'Doll', 'price': 209, 'quantity': 6},
 {'category': 'Clothing', 'item': 'Hat', 'price': 812, 'quantity': 10},
 {'category': 'Electronics', 'item': 'Laptop', 'price': 161, 'quantity': 5},
 {'category': 'Toys', 'item': 'Puzzle', 'price': 627, 'quantity': 2},
 {'category': 'Sports', 'item': 'Basketball', 'price': 902, 'quantity': 9},
 {'category': 'Electronics', 'item': 'Phone', 'price': 919, 'quantity': 4},
 {'category': 'Home & Kitchen', 'item': 'Microwave', 'price': 404, 'quantity': 10},
 {'category': 'Electronics', 'item': 'Headphones', 'price': 165, 'quantity': 7},
 {'category': 'Clothing', 'item': 'T-Shirt', 'price': 782, 'quantity': 1},
 {'category': 'Home & Kitchen', 'item': 'Toaster', 'price': 898, 'quantity': 4},
 {'category': 'Toys', 'item': 'Doll', 'price': 932, 'quantity': 8},
 {'category': 'Clothing', 'item': 'Shoes', 'price': 213, 'quantity': 6},
 {'category': 'Books', 'item': 'Notebook', 'price': 868, 'quantity': 2},
 {'category': 'Toys', 'item': 'Doll', 'price': 464, 'quantity': 4},
 {'category': 'Home & Kitchen', 'item': 'Microwave', 'price': 764, 'quantity': 6},
 {'category': 'Toys', 'item': 'Remote Car', 'price': 531, 'quantity': 9},
 {'category': 'Clothing', 'item': 'Hat', 'price': 610, 'quantity': 5}
]
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

df  = pd.DataFrame(sale_data)
df.columns = df.columns.str.capitalize()
for items in df:
    df['Subtotal'] = df['Price'] * df['Quantity']
print (df)
#https://medium.com/codeptivesolutions/https-medium-com-nensi26-formatting-in-excel-sheet-using-xlsxwriter-part-1-2c2c547b2bea
""" writer = pd.ExcelWriter('salesdata.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="Sheet1", index=False)
workbook = writer.book
worksheet = writer.sheets['Sheet1']
cell_format = workbook.add_format()
cell_format.set_bold()
worksheet.set_column("A:A",None,cell_format) 
writer.close()"""
df.to_excel('salesdata.xlsx',engine='xlsxwriter', index=False)