#!/usr/bin/python3 
if __name == "__main__":
     """ print all arguments """
     import sys

     count = 0
     for i in range(len(sys.argv) - 1):
         count += int(sys.argv[i + 1])
     print("{}".format(count))
