# write a list  of 10 random numbers to a file  called "numbers.txt"
# read the numbers from the file and print them

import random

def main():
    # open the file
    outfile = open("numbers.txt", "w")

    # write 10 random numbers to the file
    for count in range(10):
        number = random.randint(1, 100)
        outfile.write(str(number) + "\n")

    # close the file
    outfile.close()

    # open the file again
    infile = open("numbers.txt", "r")
    
    # read the numbers from the file and print them
    for line in infile:
        number = int(line)
        print(number)

    # close the file
    infile.close()


# call the main function
main()
