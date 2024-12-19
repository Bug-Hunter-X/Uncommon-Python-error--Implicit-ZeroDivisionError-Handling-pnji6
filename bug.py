def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # This line handles division by zero
    else:
        return b / a

result = function_with_uncommon_error(0, 10) 
print(result) # Output: 10

result = function_with_uncommon_error(10, 0) 
print(result) # Output: 0.0