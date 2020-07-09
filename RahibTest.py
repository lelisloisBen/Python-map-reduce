# 1 ##################################

import random
randomlist = []
for i in range(0,30):
    n = random.randint(1,100)
    randomlist.append(n)

print("Question 1: \n", randomlist, "\n")

# 2 ####################################

class User:
  def __init__(self, name, id):
    self.name = name
    self.id = id

userInfo = User("samir", 1)

print("Question 2: \n", "name: ",userInfo.name, " - id: ", userInfo.id, "\n")

# 3 & 4 ####################################

arr = [ 0, 10, 2, -10, -20 ]
arr_size = len(arr)  

def segregate(arr, size): 
	j = 0
	for i in range(size): 
		if (arr[i] <= 0): 
			arr[i], arr[j] = arr[j], arr[i] 
			j += 1 
	return j 

def findMissingPositive(arr, size): 
	
	for i in range(size): 
		if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0): 
			arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1] 
			 
	for i in range(size): 
		if (arr[i] > 0): 
			return i + 1
	return size + 1

def findMissing(arr, size): 

	shift = segregate(arr, size) 
	return findMissingPositive(arr[shift:], size - shift) 

missing = findMissing(arr, arr_size) 
print("Question 3: \n", "The smallest positive missing number is: ", missing , "\n") 


# 5 ########################################

# return sends a specified value back to its caller,
# whereas yield can produce a sequence of values.
# We should use yield when we want to iterate over a sequence 
# but don't want to store the entire sequence in memory.
# yield is used in Python generators.

print("Question 5: \n", "return sends a specified value back to its caller, whereas yield can produce a sequence of values. We should use yield when we want to iterate over a sequence but don't want to store the entire sequence in memory. yield is used in Python generators.", "\n")

# 6 ###########################################

weekdays = ['sun','mon','tue', 'sun','mon','tue','wed','thu','fri','wed','thu','fri','sat']

weekNew = []
for days in weekdays:
    if days not in weekNew:
        weekNew.append(days)

weekdays = weekNew
print("Question 6: \n", "list with removed duplicate: ", weekdays, "\n")

# 7 ###############################################
 
    # a // CREATE TABLE quiz1 (name varchar(255), id int );
    # b // INSERT INTO quiz1 ( name, id ) VALUES ( 'samir', 1 );
    # c // SELECT * FROM quiz1;
    # d // DROP TABLE quiz1;

