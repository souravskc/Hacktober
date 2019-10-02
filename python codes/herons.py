def semi_perimeter(side1,side2,side3):
    '''it provides the semi perimeter by providing sides
    '''
    return perimeter(side1,side2,side3)/2
def area_h(side1,side2,side3):
    semi=semi_perimeter(side1,side2,side3)
    area= math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
    return area
