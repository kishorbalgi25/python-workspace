from data_analysis import calculate_mean,calculate_median,calculate_standard_deviation,calculate_variance,calculate_range

# test_data = []
# test_data = [2, 4, 6, 8, 10, 12]
test_data = [3, 7, 11, 15, 19]


def main():
    print(f"The dataset is: {test_data}")
    print(f"Mean: {calculate_mean(test_data)}")
    print(f"Median: {calculate_median(test_data)}")
    print(f"SD: {calculate_standard_deviation(test_data)}")
    print(f"Variance: {calculate_variance(test_data)}")
    print(f"Variance: {calculate_range(test_data)}")
    
if __name__=="__main__":
    main()