def rom2dec(rom_str):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    roman_back=list(rom_str)[::-1]
    value=0
    right_value=roman_dict[roman_back[0]]
    for elem in roman_back:
        left_value=roman_dict[elem]
        if left_value<right_value:
            value-=left_value
        else:
            value+=left_value
        right_value=left_value
    return value
rom_str=input("Enter roman number:")
print(rom2dec(rom_str))