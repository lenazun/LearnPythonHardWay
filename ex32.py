the_count = [1,2,3,4,5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#loop through a list
for number in the_count:
	print "This is count %d" % number
	
#same
for fruit in fruits:
	print "A fruit o type: %s" % fruit

#mixed lists
for i in change:
	print "I got %r" % i
	
#empty list
elements = []

for i in range(0, 6):
	print "Adding %d to the list." % i
	#append 
	elements.append(i)

#printing them out
for i in elements:
	print "Element was: %d" % i