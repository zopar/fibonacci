#!/usr/bin/env python3
"""This script receives in input a positive integer and write a file with related fibonacci sequence
   It also check if the file to write already exists. In this case it will backup the file
   Eventual errors are written with logger.
   
"""

import os
import sys
import datetime
import logging

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')
# create logger
logger = logging.getLogger('fibonacci:')

# We use a generator
def fibonacci(number):
    """Generator of fibonacci 

    Args:
        number (integer): It must to be a positive integer

    Returns:
        generator: loop over generator to retrieve fibonacci values
    """
    
    # a is a small cache, we sum based on it
    a=[0,1]
    # In case of 0  len of range is 0 and do not do anything
    if number == 0:
        yield number
    for i in range(0, number):
        if i == 0:
            yield i
        if i == 1:
            yield i
        else:
            a[0] = a[0]+a[1]
            yield a[0]
            # We need inversion because we sum always on first element
            a[0], a[1] = a[1], a[0]

def check_and_rename(file_out):
    """Rename a file if already exists 
       It add date to the file with format %d-%m-%Y-%H-%M-%S
       for example fibonacci_1 will be renamed to fibonacci_1_22_08_2020_10_12_32

    Args:
        file_out (string): The path of the file
    """
    if os.path.isfile(file_out): 
        try:
            os.rename(file_out, file_out+"_"+datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
        except Exception as e:
            logger.error(e + file_out)
        logger.info("Renaming already existent file "+file_out)
                
def to_file(file_out, g):
    """This function permit to print value of the a generator to a file

    Args:
        file_out (string): Path of the file where we will store values 
    """
    check_and_rename(file_out)
        
    try:
        f=open(file_out, 'a')
        # looping over generator, this not increase time complexity  
        for result in g:
            f.write(str(result) + '\n')
        f.close()
    except Exception as e:
        logger.error(e + file_out)
        sys.exit(1)

def main():
    """This is the main function. Here we have also checks on value provided and related error messages
    """
    workdir=os.getcwd()+"/"
    basename="fibonacci"
    
    logger.info("This software prints fibonacci numbers in a file")

    # Manage exception value error if a non numeric value is passed
    try:
        number = int(input("Please, enter a positive number: "))
    except ValueError:
        logger.error("Non-numeric values are not allowed")
        sys.exit(1)

    # Be sure that the passed number is not negative
    if number < 0:
        logger.error("Negative values are not allowed")
        sys.exit(1)
        
    # file to write
    file_out=workdir+basename+"_"+str(number)
    
    logger.info("Calculating, it may take time, saving result on "+file_out)
    
    # call generator 
    g = fibonacci(number)
    # write generator to file
    to_file(file_out, g)
    
    logger.info("Done")

if __name__ == "__main__":
    main()
