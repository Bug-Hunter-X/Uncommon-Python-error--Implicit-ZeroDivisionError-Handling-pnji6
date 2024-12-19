def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b
        else:
            return b / a
    except ZeroDivisionError:
        return "Division by zero"

result = function_with_uncommon_error(0, 10) 
print(result) # Output: 10

result = function_with_uncommon_error(10, 0) 
print(result) # Output: 0.0

result = function_with_uncommon_error(0, 0)
print(result) # Output: Division by zero