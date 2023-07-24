# For Exercise 1.3

# Data/portfolio.dat
# https://www.tutorialspoint.com/python/python_files_io.htm

# The first column is the stock name, the second column is the number of shares,
# and the third column is the purchase price of a single share.
# Write a program called pcost.py that opens this file, reads all lines,
# and calculates how much it cost to purchase all of the shares in the portfolio.
# To do this, compute the sum of the second column multiplied by the third column.

def func1_3():
    with open("/Users/ettvo/Documents/Internship/Training Courses/Python Training Course/python-mastery/Data/portfolio.dat", "r") as f:
        fread = f.read().split()
        print(fread)
        total = 0
        num_stocks = 0
        stock_price = 0
        counter = 0
        for token in fread:
            # all are str, need to convert
            counter += 1
            if (counter == 2):
                num_stocks = float(token)
            elif (counter == 3):
                stock_price = float(token)
                counter = 0
                total += num_stocks * stock_price

    with open("/Users/ettvo/Documents/Internship/Training Courses/Python Training Course/python-mastery/Data/portfolio.dat", "r") as f:
        total_cost = 0
        for line in f: # separated until newline
            fields = line.split()
            nshares = int(fields[1])
            price = float(fields[2])
            total_cost = total_cost + nshares * price
        print(total_cost)

def func1_4(filename):
    try:
        with open(filename, "r") as f:
            total_cost = 0
            for line in f: # separated until newline
                fields = line.split()
                try:
                    nshares = int(fields[1])
                    price = float(fields[2])
                    total_cost = total_cost + nshares * price
                except ValueError as e:
                    print("Couldn't parse:", repr(line))
                    print("Reason:", e)
                else:
                    total_cost = total_cost + nshares * price
            return round(total_cost, 2)
    except FileNotFoundError:
        print(filename + " was not found.")

print(func1_4("/Users/ettvo/Documents/Internship/Training Courses/Python Training Course/python-mastery/Data/portfolio.dat"))
print(func1_4("/Users/ettvo/Documents/Internship/Training Courses/Python Training Course/python-mastery/Data/portfolio3.dat"))

