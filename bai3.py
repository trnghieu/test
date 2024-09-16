def nhap():
    dict = {}
    n = int(input("Nhập số lượng cặp : "))
    
    for i in range(n):
        key = input(f"Nhập key {i + 1}: ")
        value = input(f"Nhập value {i + 1}: ")
        dict[key] = value
    
    return dict

def taoDictC(dict_a, dict_b):
    dict_c = {}

    for key, value in dict_a.items():
        if key not in dict_b:
            dict_c[key] = value
        else:
            if dict_b[key] > value:
                dict_c[key] = dict_b[key]
            else:
                dict_c[key] = value
    
    for key, value in dict_b.items():
        if key not in dict_a:
            dict_c[key] = value
    
    return dict_c

dict_a = nhap()
dict_b = nhap()

dict_c = taoDictC(dict_a, dict_b)
print(dict_c)