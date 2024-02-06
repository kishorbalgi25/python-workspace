# a.       calculate_mean(data): Accepts a list of numerical data and returns the mean (average) value.

# b.      calculate_median(data): Accepts a list of numerical data and returns the median value.

# c.       calculate_variance(data): Accepts a list of numerical data and returns the variance.

# d.      calculate_standard_deviation(data): Accepts a list of numerical data and returns the standard deviation.


from functools import reduce

# Mean:
def calculate_mean(data):
    n = len(data)
    sum =  reduce(lambda x,y: x+y,data)
    mean = sum/n
    return mean

# Median:
def calculate_median(data):
    n = len(data)
    d = list(data)
    d.sort()
    
    mid= n//2
    if n%2==0:
        median= (d[mid-1]+d[mid])/2
    else :
        median = d[mid]
    return median

# SD:
def calculate_standard_deviation(data):
    n=len(data)
    mean = calculate_mean(data)

    squared_deviation = reduce(lambda x,y: x + (y - mean)**2,data,0)
    
    standard_deviation = (squared_deviation/n)**0.5
    
    return standard_deviation

# Variance:
def calculate_variance(data):
    standard_deviation = calculate_standard_deviation(data)
    
    variance = standard_deviation ** 2
    
    return variance

# Range:
def calculate_range(data): 
    return max(data) - min(data)