#Exercises in 10.15

#Exercise 8 - The birthday paradox
from __future__ import division
import random

#Part 1

print "Homework Part 1 - has_duplicates"

def has_duplicates(t):
    has_duplicates_flag = False
    t_copy = t[:]
    t_copy.sort()
    for i in range(len(t)-1):
        if t_copy[i]==t_copy[i+1]:
            has_duplicates_flag = True
    return has_duplicates_flag
    
print "Result for has_duplicates for list containing duplicates"
print has_duplicates([1, 3, 5, 2, 1])
print "Result for has_duplicates for list not containing duplicates"
print has_duplicates([1, 2, 3, 4])

#Part 2
print "Homework Part 2 - duplicate_birthdays"

def find_birthday_duplicates():
    duplicate_birthdays = 0
    simulations = 50000
    for i in range(simulations):
        student_bday = []
        for i in range(23):
            student_bday.append(random.randint(1, 365))
        if has_duplicates(student_bday):
            duplicate_birthdays += 1
    return duplicate_birthdays/simulations
            
print "Probability of 23 students having a duplicate birthday = ", find_birthday_duplicates()

#Employee Class

class Employee:
    
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def __repr__(self):
        return 'Employee name: %s Employee age: %s' % (self.name, str(self.age))
          
    def __lt__(self, t):
        return self.age < t.age
 
print "Homework Part 3 - Employee class"       

Madhura = Employee("Madhura", 24)
Nithanth = Employee("Nithant", 25)
Deepak = Employee("Deepak", 25)

employee_list = [Nithanth, Madhura, Deepak]
print "Before Sorting"
print employee_list
employee_list.sort()
print "After Sorting"
print employee_list    
    

