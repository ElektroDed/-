def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [1, True, 'Car']
values_dict = {'a':12, 'b':False, 'c':'Friend'}
values_list_2 = [56, 'Bus']
print_params(b=25)
print_params(*values_dict)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 45)
