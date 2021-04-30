from .quick_sort import *


def main():
    n = int(input("Enter Number of inputs: "))
    inputs = []
    for i in range(n):
        inputs.append(float(input()))

    print(inputs)
    pivot_inputs = partition(inputs, 0, len(inputs)-1)
    print(pivot_inputs)
    print(inputs)
    quick_sort(inputs, 0, len(inputs)-1)
    print(inputs)
    # print(sorted_inputs)