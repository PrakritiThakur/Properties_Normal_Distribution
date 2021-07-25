import pandas as pd
import csv
import statistics
import random

df = pd.read_csv('StudentsPerformance.csv')
data = df["reading score"].tolist()

mean = statistics.mean(data)
print("Mean is :- "+str(mean))
median = statistics.median(data)
print("Median is :- "+str(median))
std = statistics.stdev(data)
print("Standard deviation is :- "+str(std))

first_std_start,first_std_end = mean - std,mean + std
second_std_start,second_std_end = mean - (2*std), mean + (2*std)
third_std_start,third_std_end = mean - (3*std), mean + (3*std)

std_1 = [result for result in data if result > first_std_start and result <first_std_end]
std_2 = [result for result in data if result >second_std_start and result <second_std_end]
std_3 = [result for result in data if result > third_std_start and result < third_std_end]

print("{}% of data lies within first standard deviation".format(len(std_1)*100/len(data)))
print("{}% of data lies within second standard deviation".format(len(std_2)*100/len(data)))
print("{}% of data lies within third standard deviation".format(len(std_3)*100/len(data)))