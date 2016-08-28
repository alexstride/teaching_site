#This isn't very readable code (deliberately), so wait until the lesson to find out of best to write up this program.

#FYI this is how you can program when you've got a bit of practice

#check for the version of python being run and throw and adjust the functions accordingly
import sys
if sys.version_info[0]==2:
    f = lambda x: raw_input(x)
elif sys.version_info[0]==3:
    f = lambda x: input(x)
else:
    raise VersionError("You are using an unsupported version of python!")

#Ask for input, convert and print out
print(''.join([bin(ord(i))[2:] for i in f("Please enter you name:\n")]))

