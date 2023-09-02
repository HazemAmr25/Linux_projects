#Lec_2   task2
#Write python code to generate Init function of GPIO for AVR



import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:\n")
for i in range(1, n):
    print(sys.argv[i])

