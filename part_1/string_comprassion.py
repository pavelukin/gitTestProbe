def string_comprassion (first_string, second_string):
	if first_string == second_string:
		return 1
	elif len(first_string) > len(second_string):
		return 2
	elif second_string == "learn":
		return 3
first_str = input ('введите первую строку: ')
second_str = input ('введите вторую строку: ')
print (string_comprassion (first_str, second_str))