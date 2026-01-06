def get_middle_three_chars(str1):
    print("original string is", str1)

    #first get middle index number
    mi = int(len(str1) /2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")
