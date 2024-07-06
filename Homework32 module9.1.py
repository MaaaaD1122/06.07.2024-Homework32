def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        func_name = function.__name__
        results[func_name] = function(int_list)
    return results

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
