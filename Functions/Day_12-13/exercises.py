#Level 1
import string
import random


#1. Write a function which generates a six digit/character random_user_id

# def random_user_id():
#     characters = string.ascii_letters + string.digits
#     user_id = ''.join(random.choice(characters) for _ in range(6))
#     return user_id
#
# print(random_user_id())

# def random_user_id():
#     characters = string.ascii_letters + string.digits
#
#     user_id = ''
#     for _ in range(6):
#         random_char = random.choice(characters)
#         user_id += random_char
#
#     return user_id
#
# print(random_user_id())

#2. #The most difficult!!!
# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters, but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# def user_id_gen_by_user():
#     char_number = int(input("Enter number of characters: "))
#     id_number = int(input("Enter id number: "))
#     characters = string.ascii_letters + string.digits
#
#     for i in range(id_number):
#         user_id = ''
#
#         for j in range(char_number):
#             random.charm = random.choice(characters)
#             user_id += random.charm
#         print(user_id)
#
# user_id_gen_by_user()


#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)

# def rgb_color_gen():
#     rgb_color = random.randint(0, 255)
#     gb_color = random.randint(0, 255)
#     bg_color = random.randint(0, 255)
#     return (rgb_color, gb_color, bg_color)
#
# print('rgb', rgb_color_gen())

#Level 2
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples)

# def list_of_hexa_colors():
#     hex_symbols = '0123456789abcdef'
#     count = int(input('How many hexa colors do you want? '))
#
#     for i in range(count):
#         hex_color = '#'
#
#         for j in range(6):
#             random_hex = random.choice(hex_symbols)
#             hex_color += random_hex
#         print(hex_color)
#
# list_of_hexa_colors()

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array

# def list_of_rgb_colors(count):
#     rgb_colors = []
#     for _ in range(count):
#         rgb = random.randint(0, 255)
#         gb = random.randint(0, 255)
#         bg = random.randint(0, 255)
#         rgb_colors.append((rgb, gb, bg))
#     return rgb_colors
#
# print(list_of_rgb_colors(10))

#3. Write a function generate_colors which can generate any number of hexa or rgb colors

def generate_colors(format_type, count):
    colors = []
    for _ in range(count):
        if format_type == 'hex':
            hex_symbols = '0123456789abcdef'
            color  = '#'
            for _ in range(6):
                random_hex = random.choice(hex_symbols)
                color += random_hex

        elif format_type == 'rgb':
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = f"rgb({r}, {g}, {b})"

        else:
            print("Invalid format")

        colors.append(color)

    return colors

print(generate_colors('rgb', 5))


#3. Level 3

#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list (lst):
    random.shuffle(lst)
    return lst

desserts = ['мороженое', 'блинчики', 'пирог', 'печенье','конфеты']

print(shuffle_list(desserts))

#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique

def unique_list ():
    return random.sample(range(10),7)

print(unique_list())








































