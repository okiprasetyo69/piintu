def largest(total_element) :
    arr_string = ""
    for item in total_element :
        if item <= 0 or item >= 232 :
            arr_string = "Element  must be greater than 0 and less than 232 !"
            break 
        else :
            arr_string += str(item)

    return arr_string
    
    
total_element =[int (input()) for i in range(int(input("How many elements are in list : ")))] 
print('Your elements : ' + str(total_element))
print(largest(total_element))