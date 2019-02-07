# Run the code. Read the error message.
# Fix it

# Error 1:
# Use * syntax to take variable arguments

def mean(*numbers):
    print(type(numbers))
    total = sum(numbers)
    return total / len(numbers)

mean(5, 3, 6, 10)


# Error 2:
# Define a method called student_details that takes in two arguments

def user_details(name, occupation):
    print(f"Hi! My name is {name} and I am a {occupation}.")

# Call the method
user_name = "Glo"
user_occupation = "Lecturer"
# occupation was mis-spelled
print(user_details(user_name, user_occupation))


# Error 3:
# Define a method called apple_price which takes in one argument
def apple_price(num_of_apples):
    return num_of_apples * 1.00

# Call the method
# What's wrong with the following code?
print(apple_price(10))
# apple price had an extra s (mis-spelled)


# Error 4:
# Define a method called "run" that does not take in any arguments
# but prints out "This is the method 'run' and it did not take in any arguments!"
def run():
    return "This is the method \'run\' and it did not take in any arguments!"
# need to add keyword return + escape single quotes and return a string value
print(run())


# Error 5:
# Step 1: Determine the number of male adults to determine the number of couples
print("####################")
# Number of male adults equal to number of couples
def adult_males_population(n):
    adult_males = n * 0.6
    print(adult_males)

# Each couple will have 10 babies
def total_babies(n):
    adult_males_population(n) * 10


# # Step 2: Determine the number of adult females and baby females and add them up
def adult_female_population(n):
    return n * 0.4
#
#
def total_female(n, x):
    female_adults = adult_female_population(n)
    female_babies = total_babies(n) * 0.4
    return female_adults
    return female_babies
    total = female_adults + female_babies

print(total_female(1600, 100))
