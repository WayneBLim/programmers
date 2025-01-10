def solution(*temp):

    temp_set = set(temp)
    
    if len(temp_set) == 1:
        return (temp[0]+temp[1]+temp[2]) * (temp[0]**2+temp[1]**2+temp[2]**2) * (temp[0]**3+temp[1]**3+temp[2]**3)
    elif len(temp_set) == len(temp):
        return temp[0]+temp[1]+temp[2]
    else:
        return (temp[0]+temp[1]+temp[2]) * (temp[0]**2+temp[1]**2+temp[2]**2)