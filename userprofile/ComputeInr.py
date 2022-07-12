
def ComputeA(inr_range):

    if inr_range  <= 1.5:
        value = inr_range
    elif inr_range > 1.5 and inr_range <= 3.3:
        value = inr_range
   
    elif inr_range > 3.4 and inr_range <= 4.0:
        value = inr_range

    elif inr_range > 4.1 and inr_range <= 5.0:
        value = inr_range 
    elif inr_range > 5.1 and inr_range <= 9.0:
        value = inr_range
    elif inr_range >9.1:
        value = inr_range
    else:
        value = None
    
    return value


print(ComputeA(6))


def ComputeB(inr_range_input):

    if inr_range_input  <= 2.0:
        # value = inr_range
    elif inr_range_input > 2.0 and inr_range_input <= 2.4:
        # value = inr_range
   
    elif inr_range_input > 2.5 and inr_range_input <= 3.7:
        # value = inr_range

    elif inr_range_input > 3.8 and inr_range_input <= 4.0:
        # value = inr_range _input
    elif inr_range_input > 4.1 and inr_range_input <= 5.9:
        # value = inr_range
    elif inr_range_input > 6.0 and inr_range_input <= 9.0:
        # value = inr_range
    elif inr_range_input >9.1:
        # value = inr_range
    else:
        value = None
    
    return value


print(ComputeB(6))



# 

