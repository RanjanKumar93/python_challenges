## Number Sum
def number_sum(n):
    return sum(range(1, n + 1))


# Example usage
print(number_sum(5))  # Output: 15
print(number_sum(3))  # Output: 6


## Find Minimum Number
def find_min(nums):
    min_val = float("inf")
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


# Example usage
print(find_min([1, 3, -1, 2]))  # Output: -1
print(find_min([18, 3, 7, 2]))  # Output: 2


## Remove Non-Integers
def remove_nonints(nums):
    return [num for num in nums if type(num) == int]


# Example usage
print(remove_nonints(["1", 1, "3", "400", 4, 500]))  # Output: [1, 4, 500]


## Factorial
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example usage
print(factorial(4))  # Output: 24
print(factorial(0))  # Output: 1


## Area Sum
def area_sum(rectangles):
    return sum(rect["height"] * rect["width"] for rect in rectangles)


# Example usage
rectangles = [
    {"height": 5, "width": 6},
    {"height": 3, "width": 4},
]
print(area_sum(rectangles))  # Output: 42


## FizzBuzz
def fizzbuzz(start, end):
    for num in range(start, end):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


# Example usage
fizzbuzz(1, 8)


# Output:
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7


## List Division
def divide_list(nums, divisor):
    return [num / divisor for num in nums]


# Example usage
print(divide_list([6, 8, 10], 2))  # Output: [3.0, 4.0, 5.0]


## Join Strings
def join_strings(string_list):
    result = ""
    for i, string in enumerate(string_list):
        result += string
        if i < len(string_list) - 1:
            result += ","
    return result


# Example usage
string_list = ["hello", "my", "friend"]
print(join_strings(string_list))  # Output: "hello,my,friend"
