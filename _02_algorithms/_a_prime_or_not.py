"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk

def is_prime(n):
    for i in range(n):
        if n == 1:
            return False
        if i > 1 and n%i == 0:
            return False
    return True

if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    window = Tk()
    window.withdraw()
    n = simpledialog.askinteger(None, "Enter a positive integer")
    if is_prime(n):
        messagebox.showinfo(None, str(n) + " is prime!")
    else:
        messagebox.showinfo(None, str(n) + " is not prime!")

