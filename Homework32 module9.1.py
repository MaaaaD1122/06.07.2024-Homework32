def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        func_name = function.__name__
        results[func_name] = function(int_list)
    return results


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def min_value(num):
    return min(num)


def max_value(num):
    return max(num)


def length(num):
    return len(num)


def total(num):
    return sum(num)


def sorted_list(num):
    return sorted(num)


result = apply_all_func(numbers, min_value, max_value, length, total, sorted_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
