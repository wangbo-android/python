def print_matches(match_text):
	
	print('Looking for', match_text)
	while True:
		line = (yield)
		if match_text in line:
			print(line)


def count_down(n):
	print('Counting Down')
	while n > 0:
		yield n
		n = n - 1


def match_input():
	"""This is generator"""
	matches = ['python', 'quido', 'jython']
	while True:
		line = (yield)
		if line in matches:
			print('Got it')


for c in count_down(5):
	print(c)
p = print_matches('python')
next(p)
# p.__next__()
p.send('Hello World')
p.send('python is cool')
p.send('yow!')
p.close()
m = match_input()
m.__next__()
m.send('python')
print(dir(count_down))
print(match_input.__doc__)



