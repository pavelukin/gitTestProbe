def get_summ(one,two):
	return str(one)+ str(two)
def get_summ_new(one, two, three = '!'):
		summ = str(one)+str(two)+str(three)
		return summ.upper()
print (get_summ_new('a', 'b', '!'))