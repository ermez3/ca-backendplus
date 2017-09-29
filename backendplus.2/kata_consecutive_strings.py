#You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
#n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strarr, k):
    n = len(strarr)
    if (n == 0) or (k > n) or (k <= 0):
        return ""
    #print(strarr)
    array_lenght = len(strarr)
    len_values = []
    for i in range(0,array_lenght):
        positions = longest_consec_get_array_positions(i,k,array_lenght)
        str_values = [strarr[x] for i,x in enumerate(positions)]
        value = "".join(str_values)
        len_values.append([len(value),value])

    #print(len_values)
    len_values.sort(key=lambda row: row[:1], reverse=True)
    #print(len_values)
    result = len_values[0][1]
    #print(result)
    return result

def longest_consec_get_array_positions(start_position,number_of_blocks,array_lenght):
    result_positions = []
    for i in range(0,number_of_blocks):
        next_position = start_position + i
        if next_position < array_lenght:
            result_positions.append(next_position)
    return result_positions

# print(longest_consec_get_array_positions(0,2,3))
# print(longest_consec_get_array_positions(1,2,3))
# print(longest_consec_get_array_positions(2,2,3))
# longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)
