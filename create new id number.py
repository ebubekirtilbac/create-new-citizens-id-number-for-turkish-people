import random

generated_tcs = set()  # Set to keep track of generated TC Identification Numbers

def generate_tc():
    while True:
        tc = [random.randint(1, 9) for _ in range(9)]  # First 9 digits are randomly selected

        # Calculation of the sum of the first 9 digits
        sum1 = sum(tc[:9])

        # Calculation of the single-digit of the sum of the first 10 digits
        checksum1 = sum1 % 10

        # Calculation of the sum of the first 11 digits
        sum2 = sum(tc[:10])

        # Calculation of the single-digit of the sum of the first 11 digits
        checksum2 = sum2 % 10

        tc.append(checksum1)  # First checksum digit is added
        tc.append(checksum2)  # Second checksum digit is added

        tc_number = ''.join(str(digit) for digit in tc)
        
        if tc_number not in generated_tcs:  # Check if the generated TC Identification Number is not already generated
            generated_tcs.add(tc_number)  # Add the generated TC Identification Number to the set
            return tc_number

# Prompt the user for the number of TC Identification Numbers to generate
num_of_tcs = int(input("How many TC Identification Numbers would you like to generate? "))

# Generate the specified number of TC Identification Numbers and print them to the screen
for _ in range(num_of_tcs):
    tc_number = generate_tc()
    print(tc_number)