# Ask the user to enter three different integers.
#int1 = 10       # Test data
#int2 = 13       # Test data
#int3 = 6        # Test data
int1 = int(input("Please enter 1st Integer : "))
int2 = int(input("Please enter 2nd Integer : "))
int3 = int(input("Please enter 3rd Integer : "))

# The sum of all the numbers
int_sum = int1 + int2 + int3
print(int_sum)

# The first number minus the second number
int_1st_sub_2nd = int1 - int2
print(int_1st_sub_2nd)

# The third number multiplied by the first number
int_3rd_x_1st = int3 * int1
print(int_3rd_x_1st)

# The sum of all three numbers divided by the third number
int_sum_div_3rd = int_sum / int3
print(int_sum_div_3rd)