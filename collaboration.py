# This file is autogenerated. Only students should edit.
# Add your full name from Moodle to your function.

def greet_radu_minea():
	return 'missing'

def greet_diana_dutica():
	return 'missing'

def greet_horia_ignat():
	return 'missing'

def greet_mara_nicolae():
	return 'Mara Nicolae'

def greet_pavel_mateescu():
	return 'missing'

def greet_radu_chivereanu():
	return 'missing'

def greet_razvan_matisan():
	return 'missing'

def greet_laurentiu_olteanu():
	return 'missing'

if __name__ == '__main__':
	students = []
	students += [greet_radu_minea()]
	students += [greet_diana_dutica()]
	students += [greet_horia_ignat()]
	students += [greet_mara_nicolae()]
	students += [greet_pavel_mateescu()]
	students += [greet_radu_chivereanu()]
	students += [greet_razvan_matisan()]
	students += [greet_laurentiu_olteanu()]
	not_missing = lambda i: i != 'missing'
	print('\n'.join(filter(not_missing, students)))
