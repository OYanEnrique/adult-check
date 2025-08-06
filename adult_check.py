#Adult Check
current_year = int(input('Enter the current year:\n'))
adult_check=0
minor_check=0

for number in range (0,7):
	birth_year = int(input('Enter your birth year:\n'))
	if current_year - birth_year >= 18:
		adult_check += 1
	else:
		minor_check += 1
		
print(f'{adult_check} People are an adult!')
print(f'{minor_check} People are not an adult yet!')