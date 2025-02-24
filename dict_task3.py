#Dictonary datasets for performing various operations
sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

employee_sales = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}

marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}

movie_ratings = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}

total_price= {}
topthreedata = {}
totalcomplains = 0
complainperc={}

#Function to calculate total sales and highest sale store
def calculate_totalsales(sales_data, product_prices):
    """
    here the data is being passed and using for loop dictonary iteration processs is being performed
    where total sale per store is being caluclated and the stored in dictonary 
    Also max function is being used to find the highest selling store 
    """
    for store, product_details in sales_data.items():
        total_price[store] = 0
        for product_name, quantity in product_details.items():
            total_price[store] += product_prices[product_name] * quantity    
    highessale =  max(total_price, key = lambda i : total_price[i])
    return total_price, highessale

def findtopemployee(employee_sales):
    """
    Here employee data is being sent and using common fuction top employee data and top 3 employees are 
    being returened
    """
    topemployee, topemployeeval = gettopdata(employee_sales)
    return gettopthree(employee_sales), topemployee, topemployeeval

def complainpercentage(complaints):
    """
    Here complains data is being used and using common fuction top complain data, total no of complains
    and percentage calculation(using function) is being performed and answers are being returened
    """
    topcomplain, topcomplainval = gettopdata(complaints) 
    return gettotal(complaints), topcomplain,topcomplainval, calcper(complaints,gettotal(complaints))

def getbestmarketer(marketing_performance):
    """
    Here marketing data is being used and using common fuction top data, and get average 
    is being performed and answers are being returened
    """
    topperformer, topperformerval = gettopdata(marketing_performance)
    return topperformer, topperformerval, getaverage(gettotal(marketing_performance),len(marketing_performance))    

def getmovierating(movie_ratings):
    """
    Here movie rating data is being used and using common fuction top data, to three values and get average 
    is being performed and answers are being returened
    """
    topmovie,topmovieval = gettopdata(movie_ratings)
    return getaverage(gettotal(movie_ratings), len(movie_ratings)), gettopthree(movie_ratings),topmovie,topmovieval

# Common functions to reuse further 

# Function for percentage calculation 
def calcper(complaints,totalcomplains):
    for name, no in complaints.items():
        complainperc[name] = (no/totalcomplains)*100
    return complainperc

# Function to get top three data 
def gettopthree(data):
    topthreedata={}
    topthreedata = dict(sorted(data.items(), key=lambda i : i[1], reverse = True)[:3])
    return topthreedata

# Function to get average of data 
def getaverage(total,noofcount):
    return total/noofcount

# Function to get top data 
def gettopdata(data):
    return max(data,key = data.get), data[max(data,key = data.get)]

# Function to get total
def gettotal(data):
    total = 0
    for key,value in data.items():
        total = value if total == 0 else total + value
    return round(total,3)

#Function call and store in variables 
total_sales, highestsalestore = calculate_totalsales(sales_data, product_prices)
topthreeemployes, topemployee, topemployeesale = findtopemployee(employee_sales)
totalcomplains, topcomplain, highestcomplain, percentcompain = complainpercentage(complaints)
topperformer, topperformerval, averagemarketing =  getbestmarketer(marketing_performance)
averagemovierating, topthreemovies, topmovie, topmovieval = getmovierating(movie_ratings)

#Printing the whole Data
print(f"Total sales of each store: {total_sales}")
print(f"Highest sale store: {highestsalestore} with no of sales as {total_sales[highestsalestore]}")
print(f"Top 3 employees are : {topthreeemployes}")
print(f"Highest sale employee: {topemployee} with no of sales as {topemployeesale}")
print(f"Total no of Complains is {totalcomplains}")
print(f"Highest complain {topcomplain} with no of complains {highestcomplain}")
print(f"Complain percentage : {percentcompain}")
print(f"Top marketing performer is {topperformer} with percentage {topperformerval}%")
print(f"Average marketing rate : {averagemarketing}%")
print(f"Average movie rating is : {averagemovierating}")
print(f"Top 3 movies {topthreemovies}, Top Movie {topmovie} with rating {topmovieval}")
