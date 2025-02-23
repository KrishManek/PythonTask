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


def calculate_totalsales(sales_data, product_prices):
    for store, product_details in sales_data.items():
        total_price[store] = 0
        for product_name, quantity in product_details.items():
            total_price[store] += product_prices[product_name] * quantity    
    highessale =  max(total_price, key = lambda i : total_price[i])
    return total_price, highessale

def findtopemployee(employee_sales):
    return gettopthree(employee_sales)

def complainpercentage(complaints):
    topcomplain = ""
    totalcomplains = 0
    highestcomplain = 0
    for name, no in complaints.items():
        if highestcomplain < no:
            highestcomplain = no 
            topcomplain = name 
        totalcomplains = no if totalcomplains == 0 else totalcomplains + no   
    percentcompain = calcper(complaints,totalcomplains)
    return totalcomplains, topcomplain, highestcomplain, percentcompain

def calcper(complaints,totalcomplains):
    for name, no in complaints.items():
        complainperc[name] = (no/totalcomplains)*100
    return complainperc

def getbestmarketer(marketing_performance):
    topperformerval = total =  count = 0
    for name,value in marketing_performance.items():
        if topperformerval < value:
            topperformer = name 
            topperformerval = value
        total = value if total == 0 else total + value
        count+=1
    average = getaverage(total,count)
    return topperformer, topperformerval, average    

def gettopthree(data):
    topthreedata={}
    sorteddata = dict(sorted(data.items(), key=lambda i : i[1], reverse = True))
    count = 0
    for name,sale in sorteddata.items(): 
        if count > 2:
            return topthreedata,top
        else:
            topthreedata[name] = sale
            count += 1
        if count == 1:
            top = name

def getcount(data):
    count = 0
    for name,value in data.items():
        count+=1
    return count

def getaverage(total,noofcount):
    return total/noofcount

def getmovierating(movie_ratings):
    topthreemovies, topmovie = gettopthree(movie_ratings)
    return getaverage(gettotal(movie_ratings), getcount(movie_ratings)), topthreemovies,topmovie

def gettotal(data):
    total = 0
    for key,value in data.items():
        total = value if total == 0 else total + value
    return round(total,3)



total_sales, highestsalestore = calculate_totalsales(sales_data, product_prices)
topthreeemployes, topemployee = findtopemployee(employee_sales)
totalcomplains, topcomplain, highestcomplain, percentcompain = complainpercentage(complaints)
topperformer, topperformerval, averagemarketing =  getbestmarketer(marketing_performance)
averagemovierating, topthreemovies, topmovie = getmovierating(movie_ratings)


print(f"Total sales of each store: {total_sales}")
print(f"Highest sale store: {highestsalestore} with no of sales as {total_sales[highestsalestore]}")
print(f"Top 3 employees are : {topthreeemployes}")
print(f"Highest sale employee: {topemployee} with no of sales as {topthreeemployes[topemployee]}")
print(f"Total no of Complains is {totalcomplains}")
print(f"Highest complain {topcomplain} with no of complains {highestcomplain}")
print(f"Complain percentage : {percentcompain}")
print(f"Top performer is {topperformer} with percentage {topperformerval}%")
print(f"Average marketing rate : {averagemarketing}%")
print(f"Average movie rating is : {averagemovierating}")
print(f"Top 3 movies {topthreemovies}, Top Movie {topmovie} with rating {topthreemovies[topmovie]}")
