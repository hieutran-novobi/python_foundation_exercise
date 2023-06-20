import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email) is not None


print(is_valid_email("jayson@gmail.com"))
print(is_valid_email("jayson_123@gmail.com"))
print(is_valid_email("jayson-54@gmail.com.vn"))
print(is_valid_email("jayson-54@gmail.com.vndasdas"))