import simpleparser

while True:
		text = input('simple parser > ')
		result, error = simpleparser.run('<stdin>', text)


		if error: print(error.as_string())
		else: print(result)