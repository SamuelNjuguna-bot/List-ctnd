#  Python Program to count unique values in a List
from enum import unique
from itertools import count


def uniquevalues(listelements):
    newList = []
    for item in listelements:
        if item not in newList:
            newList.append(item)
    cont = len(newList)

    return cont


def removeduplicates(unique):
    uniqueval = []
    for item in unique:
        if item not in uniqueval:
            uniqueval.append(item)
    return uniqueval
example_list = [21, 34, 21, 98, 100, 76, 34, 45, 100, 21, 54]
contitems = uniquevalues(listelements=example_list)
uniqueval = removeduplicates(unique=example_list)
print(contitems)
print(uniqueval)


# The program Tests for Elements in the List with a Frequency greater than K
test_List = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 2
cont = []
for num in test_List:
    frequency = test_List.count(num)
    if frequency >= 2 and num not in cont:
        cont.append(num)

print(cont)


# The Following Program checks if there are three consecutive numbers in list
anotherList = [2, 2, 3, 2, 1, 1, 1, 6]
size = len(anotherList)
for numbers in range(size -2):
    if anotherList[numbers]== anotherList[numbers+1] and anotherList[numbers+1]==anotherList[numbers+ 2] : print(anotherList[numbers])

# The program removes empty lists from a list
list_items = [[], [23, 56], [], [12, 64]]
for item in list_items:
    if item == []:
        list_items.remove(item)
print(list_items)
#Convert List to List of dictionaries
input_list  = ["Gathaiya", 23]
keylist = ["Name", "Age"]
list2 = [{keylist[0]: input_list[0], keylist[1]: input_list[1]}]
print(list2)

#Uncommon Elements in a two lists and common
def commonAndUncommonNumbers(list1, list2):
    l1 = set(list1)
    l2 = set(list2)
    common = list(l1.union(l2))

    uncommon =list(l1.intersection(l2))
    return common,uncommon

list1 = [90, 67, 80, 45, 37, 52, 78]
list2 = [16, 45, 67, 54, 33, 52, 17]
res = commonAndUncommonNumbers(list1=list1, list2=list2)
print(list(res))

#Selects random Elements from a list
from itertools import chain
import random

listl = [[12,34], [18,87], [90,84]]
ran = random.choice(list(chain.from_iterable(listl)))
print(ran)

#Below Program Sorts Elemnts and reverses their order
tester_list  = [[12, 76] ,[45, 32], [89,87, 65,], [23,43]]
reversed_sort = []
for item in tester_list:
    srt = sorted(item)
    reversed_list = reversed(srt)
print(tester_list)

# The below program pair elements in list
unpaired_list = [[12, 26,89],[23,54,76], [51,58]]
res = []
for sub in unpaired_list:
    res.append([[ele, sub[-1]] for ele in sub[:-1]])
print(res)
# Below Program appends a String to a List
string = "Python Lists"
list_elements = [21, 34, 87, 63]
list_elements.append(string)
print(list_elements)
#Below Program checks if an element is a list or not
list_type = []
print(type(list_type))
#Below program changes string representation into a list
string_list = "[21, 34, 87, 63]"
new = list(string_list.strip('[]').split(','))
print(type(new))
#Below program checks the most frequent element in a list
def mostFrequent(another):
    counter = 0
    num = another[0]

    for i in another:
        curr_frequency = another.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

another = [2, 2, 3, 1, 1, 1, 6]
mx = mostFrequent(another)
print(mx)
#or
from statistics import mode
print(mode(another))

#Converting a number to a list of numbers
def convertNum(num):
  new = []
  Strin = str(num)
  ln = len(Strin)

  for item in Strin:
        new.append(item)
  neew = str(new)
  neew.strip('][').split(',')
  print(neew)
  ls = list(neew)
  print(neew)
num = 2024
convertNum(num)
#Below program removes None values from a list
lit_with_none_values = [24, None, 63, None, 47]
for element in lit_with_none_values:
    if element == None:
       lit_with_none_values.remove(element)
print(lit_with_none_values)
#Below Program accesses the index and value
def indexValue(List):
    ln = len(List)
    for value in range(ln):
        print(List[value], value)
List = [46, 71, 83, 76]
indexValue(List)
#Below Program selects a random no from a List
def RandomNum(list_random):
    ran = random.choice(list_random)
    return ran
list_random = [21, 34, 87, 63]
print(RandomNum(list_random))
#Below Program checks if two lists are indentical
list3 = ['Banice','God Own', 'Bet', 'Orods']
list4 =['Ndichu', 'Mum Sharon', 'Peace', 'Jamo','Manu']
l3 = set(list3)
l4 = set(list4)
if (l4.intersection(l3) == l4):
    print('elements are identical')
else:
    print('Elements are not identical')

#Below program gets the last element from a list
lastItemList = [401, 202, 201, 404]
print(lastItemList.pop())
