def fibonacci_by_number(to_number):
    """1.- Write a fibonacci function"""
    try:
        i = 0
        fibonnaci_result = [1, 1]
        fibonacci_number = 1
        while fibonacci_number < to_number:
            fibonacci_number = fibonnaci_result[i] + fibonnaci_result[-1]
            if fibonacci_number < to_number:
                fibonnaci_result.append(fibonacci_number)
            i = i + 1
        return fibonnaci_result
    except:
        raise

def reverse_list(original_list):
    """2.-Write a function reverse to reverse a list. Can you do this without using list slicing?"""
    try:
        reversed_list = original_list.copy()
        j = 0
        while j < len(reversed_list) - 1: 
            i = 0
            while i < len(reversed_list) - 1:
                if reversed_list[i] > reversed_list[i+1]:
                    tmp = reversed_list[i]
                    reversed_list[i] = reversed_list[i+1]
                    reversed_list[i+1] = tmp
                i = i + 1
            j = j + 1
        return reversed_list
    except:
        raise

def cumulative_sum_list(original_list):
    """3.-Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. 
    Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?"""
    try:
        list_result = []
        j = 0
        while j < len(original_list) - 1:
            i = 0
            cumulative_result = original_list[j]
            while i < j:
                cumulative_result = cumulative_result + original_list[i]
                i = i + 1
            list_result.append(cumulative_result)
            j = j + 1
        return list_result
    except:
            raise
def cumulative_product_list(original_list):
    """4.-Write a function cumulative_product to compute cumulative product of a list of numbers."""
    try:
        list_result = []
        j = 0
        while j < len(original_list) - 1:
            i = 0
            cumulative_result = original_list[j]
            while i < j:
                cumulative_result = cumulative_result * original_list[i]
                i = i + 1
            list_result.append(cumulative_result)
            j = j + 1
        return list_result
    except:
            raise

def distinct_list(original_list):
    """5.-Write a function unique to find all the unique elements of a list. (int & strings)"""
    return set(original_list)

def duplicates_list(original_list):
    """6.-Write a function dups to find all duplicates in the list. (int & strings)"""
    duplicate_list = [x for i,x in enumerate(original_list) if original_list.count(x) > 1]
    return set(duplicate_list)

def group_list(original_list,size):
    """7.-Write a function group(list, size) that take a list and splits into smaller lists of given size."""
    groups = len(original_list) / size
    grouped_list = []
    if len(original_list) % size > 0:
        groups = groups + 1
    i = 0
    while i < groups:
        start = i * size 
        end = start + size
        grouped_list.append(original_list[start:end])
        i = i + 1
    return grouped_list
# """1.- Call the fibonacci function"""
print("1.- Call fibonacci_by_number(100)")
print(fibonacci_by_number(100))
# """2.- Call reverse_list([9,6,3,2,4,8])"""
print("2.- Call reverse_list([9,6,3,2,4,8])")
print(reverse_list([9,6,3,2,4,8]))
# """3.- Call cumulative_sum_list([9,6,3,2,4,8])"""
print("3.- Call cumulative_sum_list([9,6,3,2,4,8])")
print(cumulative_sum_list([9,6,3,2,4,8]))
# """4.- Call cumulative_product_list([9,6,3,2,4,8])"""
print("4.- Call cumulative_product_list([9,6,3,2,4,8])")
print(cumulative_product_list([9,6,3,2,4,8]))
# """5.-Call distinct_list([0,0,2,2,1,3,4,5])"""
print("5.-Call distinct_list([0,0,2,2,1,3,4,5])")
print(distinct_list([0,0,2,2,1,3,4,5]))
# """6.-Call duplicates_list([0,0,2,2,1,3,4,5])"""
print(".-Call duplicates_list([0,0,2,2,1,3,4,5])")
print(duplicates_list([0,0,2,2,1,3,4,5]))
# """7.-Call group_list([0,1,2,3,4,5,6,7,8,9])""
print("7.-Call group_list([0,1,2,3,4,5,6,7,8,9])")
print(group_list([0,1,2,3,4,5,6,7,8,9],2))