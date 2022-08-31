# the classes a student is registered for
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only the ITEC classes, can also .lower() and others like it
only_itec = [ c for c in classes_registered if c.startswith('ITEC')]
print(only_itec)


# Record temperature every day. Record -1 if not possible to take measurement.
high_temps =[-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

# Make a list of only numbers that represent a valid temperature measurement
only_real_measurements = [temp for temp in high_temps if temp != -1]
print(only_real_measurements)

temp_celsius = [(temp_f - 32) *5 /9 for temp_f in only_real_measurements]
print(temp_celsius)

average = sum(temp_celsius)/len(temp_celsius)
print(f'The average is {average:.2f}C')


#practice
even_numbers = [2, 4, 6]
odd_numbers = [even + 1 for even in even_numbers]
print(odd_numbers)

numbers = [0, 3, 4, 0, 22, 1]
no_zeros = [n for n in numbers if n != 0]
print(no_zeros)

classes = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
itec_classes = [itec for itec in classes if itec.startswith('ITEC')]
print(itec_classes)

numbers_with_zeros = [ 0, 10, 4, 0, 32]
numbers_doubled = [n * 2 for n in numbers_with_zeros if n != 0]
print(numbers_doubled)