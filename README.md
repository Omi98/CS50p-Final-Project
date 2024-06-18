# Calculator

#### Video Demo: https://youtu.be/iitcGGFoMqg

#### Description: A simple Python project using Tkinter library

This program is a simple calculator that takes only 2 numbers and performs one of the 4 operations. Addition, subtraction, multiplication and division.
It has GUI. The user is required to interact with the GUI and not the terminal of text editor.

This is just a fine adaption of the solution. A good would be a simple calculator interface just like the one we have on our phones. From a user’s point of view, I think a user would rather choose the good outcome.
But in terms of my own solution, as compared to the very first problem set of this course, this is something that I really worked hard on. OOP was the hardest concept for me in the course, I still fear it, but I used the basics to keep the GUI methods in one place.
A lot can be said on outcomes, this is time consuming, and not the better outcome, but it is a breakthrough for me.

To start off, you need to install tkinter library.
Run the following command in your terminal:
`pip install tk`

### Welcome Frame
The program uses a single window and two frames to display the information.
It starts off with the Welcome Frame. That has two buttons on it. The **Proceed** Button allows the user to move to the next frame, while the **Exit** Button simply quits the window.

### Proceed Frame
The Proceed frame is where everything comes together. The user is asked to enter 2 numbers, in separate Input Fields, and then choose one of the 4 opterations (in the form of Radio Buttons).

### When errors are raised?
1. When any of the Input Fields is left empty
2. When the entry is not an integer
3. When a number is divided by 0

### Submit
After entering the numbers and choosing one of the operations (Addition, Subtraction, Multiplication, Division), the user can click the **Submit** Button.
After clicking the Submit Button, the program then processes the information and displays the result in a **Message Box**.

### Tests
In terms of testing, I am still a beginner. It is always challenging to try to map the test function with the original function, specially when it involves inputs, I still wrote 4 simple tests that can be run with pytest.
To run the test file, install the pytest library using the command
`pip install pytest`

## This was CS50P!


