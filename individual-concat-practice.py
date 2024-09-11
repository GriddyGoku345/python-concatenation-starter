# Isaac Bissonette
# 9/11/24
# String Concatenation

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in

first_name = 'Isaac'
city = 'Kalkaska'
state = 'Michigan'

print(first_name + ' lives in ' + city + ' ' + state + '.')


# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
# Create another variable that stores the welcome message
# Use concatenation to create the customized message

print('what is your name?')
user_name = input()
print('Welcome! ' + user_name + ' to the single most infuriating game on the planet!')




# Part 3
# Assign a number to your age variable
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
# Use concatenation to display a sentence that tells us your first name and age

age = 18
print('My name is ' + first_name + ' and i am ' + str(age) + ' years old' + '.')



# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches

last_name = 'Bissonette'
height = 70
print(f'My name is {first_name} {last_name} and I am {height} inches tall')