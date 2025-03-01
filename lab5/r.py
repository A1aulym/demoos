import re

#1
def match_a_b_zero_or_more(string):
    result = re.fullmatch(r'ab*', string) is not None
    print(f"'{string}' -> {result}")
    return result

#2
def match_a_two_to_three_b(string):
    result = re.fullmatch(r'ab{2,3}', string) is not None
    print(f"'{string}' -> {result}")
    return result

#3
def find_lowercase_with_underscore(string):
    result = re.findall(r'[a-z]+_[a-z]+', string)
    print(f"'{string}' -> {result}")
    return result

#4
def find_upper_followed_by_lower(string):
    result = re.findall(r'[A-Z][a-z]+', string)
    print(f"'{string}' -> {result}")
    return result

#5
def match_a_anything_b(string):
    result = re.fullmatch(r'a.*b', string) 
    print(f"'{string}' -> {result}")
    return result

#6
def replace_space_comma_dot(string):
    result = re.sub(r'[ ,.]', ':', string)
    print(f"'{string}' -> '{result}'")
    return result

#7
def snake_to_camel(string):
    words = string.split('_')
    result = words[0] + ''.join(word.capitalize() for word in words[1:])
    print(f"'{string}' -> '{result}'")
    return result

#8
def split_at_uppercase(string):
    result = re.findall(r'[A-Z][^A-Z]*', string)
    print(f"'{string}' -> {result}")
    return result

#9
def insert_spaces_capital_words(string):
    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
    print(f"'{string}' -> '{result}'")
    return result

#10
def camel_to_snake(string):
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
    print(f"'{string}' -> '{result}'")
    return result





match_a_b_zero_or_more("abbb") 
match_a_two_to_three_b("abb")  
find_lowercase_with_underscore("hello_world and example_test")
find_upper_followed_by_lower("Hello World TestCase")
match_a_anything_b("a123b")  
replace_space_comma_dot("Hello, world. This is a test")
snake_to_camel("this_is_a_test")
split_at_uppercase("HelloWorldExample")
insert_spaces_capital_words("HelloWorldExample")
camel_to_snake("HelloWorldExample")