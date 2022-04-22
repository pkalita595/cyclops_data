def specs():

	reject_strings = ["a c","a b d","a a c c c b"]
	accept_strings = ["c b e", "a c b e b e", 'd b b e']
	config = {
		'num_rules': 6, #Number of rules
		'size_rules' : 3, #Number of symbols in RHS
		'num_nonterms' : 3, #Number of nonterms
		'expansion_constant' : 10, #Determines the max. number of parse actions to take while parsing
		'optimize' : False, # enable optimized mode
		'neg_egs' : True, # consider negative examples 
		'threshold' : 0.2  # number of unsat cores to break
	}

	return accept_strings,reject_strings,config

def find_original_grammar():
	original_grammar = [['S', 'A','B','e'],['A','eps','d','B'],['A','eps','a','S'],['A','eps','eps','c'],['B','eps','A','S'],['B','eps','eps','b']]
	# return get_original_grammar()
	return original_grammar

def getError():
    #return "2nd rule, first of A is first B (term: c)"
    return "a should  be in first set of S"

def get_parse_table():
	parse_table = [{'non_term':'S' ,'e':0 ,'d':1,'a':0,'c':1,'b':0,'$':0},{'non_term':'A' ,'e':0 ,'d':2,'a':3,'c':4,'b':0,'$':0},{'non_term':'B' ,'e':0 ,'d':5,'a':5,'c':5,'b':6,'$':0}]
	#parse_table = [{'non_term':'S' ,'e':0 ,'d':1,'a':1,'c':1,'b':0,'$':0},{'non_term':'A' ,'e':0 ,'d':2,'a':3,'c':4,'b':0,'$':0},{'non_term':'B' ,'e':0 ,'d':5,'a':5,'c':5,'b':6,'$':0}]
	return parse_table

def nums():
	original_grammar = find_original_grammar()
	num_vars = {'num_rules':len(original_grammar), 'size_rules':len(original_grammar[0])-1}
	return num_vars

def get_first_set():
	first_set = [{'non_term':'S' ,'e':0 ,'d':1 ,'a':1 ,'c':1 ,'b':0 ,'eps':0 },{'non_term':'A' ,'e':0 ,'d':1 ,'a':1 ,'c':1 ,'b':0 ,'eps':0 },{'non_term':'B' ,'e':0 ,'d':1 ,'a':1 ,'c':1 ,'b':1 ,'eps':0 }]
	return first_set

def get_follow_set():
	follow_set = [{'non_term':'S' ,'e':1 ,'d':1,'a':1,'c':1,'b':1,'$':1},{'non_term':'A' ,'e':0 ,'d':1,'a':1,'c':1,'b':1,'$':0},{'non_term':'B' ,'e':1 ,'d':1,'a':1,'c':1,'b':1,'$':0}]
	return follow_set

reject_strings = ["a c","a b","a a c c c b"]
accept_strings = ["c b e", "a c b e b e", 'd b b e']
#S -> A B e
#A -> d B
#A -> a S
#A -> c
#B -> A S
#B -> b

