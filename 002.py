"""
Defining functions
Builtin functions are great, but we can only get so far with them before we need to start defining our own functions. Below is a simple example.
"""

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),                  # Python allows trailing commas in argument lists. How nice is that?
)

print(1, 2, 3, sep=' < ')

#But if we don't specify a value, sep is treated as having a default value of ' ' (a single space).

print("\n")
def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Olanle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("Gab")
print(greet())

#Functions Applied to Functions¶
"""
Here's something that's powerful, though it can feel very abstract at first.
You can supply functions as arguments to other functions.
Some example may make this clearer:
"""

print("\n")
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),    #This takes x as 1 since its the second value taken alongside of mult_by_five
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

print("\n")
"""
Functions that operate on other functions are called "higher-order functions." You probably won't write your own for a little while. But there are higher-order functions built into Python that you might find useful to call.
Here's an interesting example using the max function.
By default, max returns the largest of its arguments. But if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax').
"""

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5))


print("\n")
"""
Complete the body of the following function according to its docstring.
HINT: Python has a built-in function round.
"""

def round_to_two_places(num):
    
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
   return round(num, 2)
   pass

print(round_to_two_places(9.989))
print(round_to_two_places(9.999))


"""
In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
Below is a simple function that will calculate the number of candies to smash for any number of total candies.
Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
Update the docstring to reflect this new behaviour.
"""
alice_candies = 121
bob_candies = 77
carol_candies = 122

total_candies = alice_candies + bob_candies + carol_candies

def to_smash(total_candies, n_friends=3):
    return total_candies % n_friends

print(to_smash(total_candies))