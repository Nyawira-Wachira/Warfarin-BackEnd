

# define a filter method

# send  algorithm
# send inr range






def Compute(inr_range):

    if inr_range  <= 1.5:

        remedy ="A"

        return remedy
    elif inr_range > 1.5 and inr_range <= 3.3:

        remedy ="B"

        return remedy
    elif inr_range > 3.4 and inr_range <= 4.0:

        remedy = "Continue current Warfarin dose "

        return remedy

    elif inr_range > 4.1 and inr_range <= 5.0:

        remedy = ""

        return remedy
    elif inr_range > 5.1 and inr_range <= 9.0:
        remedy = ""

        return remedy
    elif inr_range >9.1:

        remedy = "weeeh"

        return remedy

    else:

        remedy = "invalid Option"






print(Compute(3+8))



# 

