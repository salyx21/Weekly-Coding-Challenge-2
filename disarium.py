def disarium(number):
    str_num = str(number)
    ls = [int(number)**(index+1) for index,number in enumerate(str_num)]
    return sum(ls) == number
