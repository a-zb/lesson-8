from art import *

# the above statement means:
# |- from the 'art' library , import or bring in '*'
# |-- '*' really means "bring in everything"
#
# So, we are bringing in all of the 'art' library into our program. Now we can use it.
# Libraries are collections of code, written by other developers.

# Check out this website. It shows more info about this library: https://www.ascii-art.site/

# let's print some ascii art. Run the program and see what shows up in the terminal
# Remember, this program is in your home directory, /code/lesson-8
print(text2art("This Is Fun"))

# Check which fonts are available: https://www.ascii-art.site/FontList.html

# The text2art() function accepts a message and a font you would like to use: https://www.ascii-art.site/#ascii-text
my_art = text2art("I'm a Ninja", font="aquaplan")

# Now , print it.
# Add a line of Python next. Pass my_art variable to the print function and run the program.

# Add 3 more calls to print and text2art() function. Feel free to mix and match messages and font name.

# This library has a collection of 1 line art. All of them are in a list.

# You can pass these names to the art() function. Here's the full list: https://www.ascii-art.site/ArtList.html
# Remove the # character on the next line, save the program and run it.
# print("This is a bear: ", art('bear'), "  This is a bear squinting: ", art('bear squiting'))

# Add 3 more calls to art() function, or as many as you like. Have fun.


# When you're done, watch this short video about Python libraries and modules: https://www.youtube.com/watch?v=dTYf3carzrc

# As practice, add a new file program-2.py.
# Import the art library in your new program and try using the library in any way you like.
# The lesson is complete, when you had enough fun with your own program.