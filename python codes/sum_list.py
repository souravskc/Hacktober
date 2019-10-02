def count_matches(s1,s2):
    num_matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1


    return num_matches       




def sum_items(list1,list2):
    sum_list =[]
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])


    return sum_list    
def calculate_average(asn_grade):
    for item in asn_grade:
        total = total + item[1]

    return total  /len(asn_grade)
