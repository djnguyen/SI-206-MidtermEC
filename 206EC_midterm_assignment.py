## Winter 2017
## SI 206 - Programming I
## Name: David Nguyen (djnguyen)
## Section: Thursday (3-4 PM)

## Extra Credit Assignment

####### INSTRUCTIONS #######

## This assignment is extra credit, and it is especially encouraged for those who found the midterm or concepts before the midterm challenging or who would like to revisit them.

## In this assignment you will revisit eight exercises from the midterm. We have chosen these questions based on class-wide midterm statistics AND which specific concepts these questions address. For extra credit, you may complete any of the ones that you did not receive full points for on the midterm!

## For each of these problems, you are required to correctly solve each exercise, in either a comment or writing code, as appropriate, in this file, and add a reflection underneath your solution in comments that briefly describes:

## - What your confusion or misunderstanding was on the midterm OR what was incorrect about the answer that you put on the exam if you answered the question.

## - Why the correct answer is correct. If the answer involves writing code, write 1-3 sentences explaining what the code does, or comment each line. If the answer involves determining code output, write 1-3 sentences explaining why it outputs that code. If the answer is a multiple choice question, write 1-2 sentences about why that option (or those options) are the correct ones.

# Brevity is encouraged! correctness is also important.

## You could potentially get UP TO 400 extra credit points in the course with this assignment. Each question revisit is worth 50 points. You may complete as many or as few of these six as you want, as long as you did not get full credit on them on the midterm.

## You may use any resources, help, etc. to complete this. You must write the comments explaining incorrect/correct answers by yourself, in your own words. When we release a solution set for the midterm, you may use that, you may use the rubric that shows correct answers, and you may certainly run the code to test it out! We encourage you to come up with the answer on your own and test it by running the code so you really test your understanding.

## This file must run without syntax errors when you turn it in. Everything that needs commenting-out should be commented out, and it should not include any characters that cannot be in a Python file, etc. (Copying and pasting from e.g. Word can cause that, so be careful.) Test it before you turn it in!

## Deadline to submit on Canvas: Tuesday, March 14th at 11:59 PM

############ END INSTRUCTIONS ############
print("\n*******\n")

print ('Midterm Question #3')

## (Midterm 3). What is the output after the following code runs?

def func(x):
    for item in x:
        return x

print(func([1,2]))

## Put your answer to the question here:

## The Answer I put for Question 1 was: 1


## Put your comment explanations/reflections here:

## After looking at this problem again, I realized that x is equal to the list [1,2] and since that list is being
## passed through the function, it would return that same list again. During the exam, I was thinking becuase there 
## is a return statement, the for loop would exit and only the first element of the list will be printed, instead of both.

## LOOK AT THIS AGAIN???


print("\n*******\n")
print ('Midterm Question #6')
print ('Check out my Comments!')

## (Midterm 6) Which of the following statements (in comments) are valid to create an instance of class Card and save it to the variable x, with no errors? (Reference cards.py / the code on the exam)

# a. x = Card.create()
# b. x = Card(2.3)
# c. x = Card(5,3)
# d. x = Card(2)
# e. x = Card.__init__
# f. x = Card(1, "Queen")

## Put your answer to the question here:

## C and D

## Put your comment explanations/reflections here:

## The answer for this problem was only supposed to be D. I had the right idea going because for answer choice B, I wrote
## down that x = Card(2.3) would create the instance but would fail. I had forgotten to realize that there is no suit in
## the suit_name list with the list element of 5. That would also cause nothing to be saved into the variable x becuase
## it would fail to properly create an instance.



print("\n*******\n")
print ('Midterm Question #7')

## (Midterm 7). Write an additional method for the Card class called compare_rank. You can assume the method is correctly placed inside the class, but you can write it by copying the Card class definition into this file, OR you can write it and test it in the cards.py file and copy it into this file commented out. (Otherwise, it won't run!)

## This method should return a boolean value True if the input rank number is larger than the Card's rank, and False if it is smaller or equal to the Card's rank.

class Card(object):
    suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
    rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

    def __init__(self, suit=0,rank=2):
        self.suit = self.suit_names[suit]
        if rank in self.faces: # self.rank handles printed representation
            self.rank = self.faces[rank]
        else:
            self.rank = rank
        self.rank_num = rank # To handle winning comparison 

    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

    def compare_rank(self, rank_imp):
        
        if self.rank_num < rank_imp:
            return True
        
        else:
            return False

## For example, the following code should work correctly when placed inside the Card class definition, if the compare_rank method is defined correctly:

c = Card(2,11)

print(c.compare_rank(4)) # should print False
print(c.compare_rank(13)) # should print True
print(c.compare_rank(11)) # should print False

## Remember this code WILL NOT RUN here without the Card class definition here and the method defined properly.


## Put your answer to the question here:

## My answer to this question was:
# def compare_rank(self, rank_imp):
#     if self.rank > rank_imp:
#         return False
#     else:
#         return True


## Put your comment explanations/reflections here:

## I got marked down due to a logic error and I definitely see why I got it wrong.
## Because within the if statement, I had it return False while I should have had it return true. I also should have 
## used self.rank_num so that the method can compare integers and not strings for the face cards.


print("\n*******\n")
print ('Midterm Question #9')


## (Midterm 9). Given the following code, there is 1 possible value of var such that every print statement will print out. What is the only possible type that value could be? (In your reflection/explanation, explain briefly why.)

var = 'mpyx'

print (var[1:3])
if var[1:3] == "py":
    print("Yup!")
if var[-1] == 'x':
    print("Nice")
if len(var) == 4:
    print(False)
if 'm' in var:
    print("Done")

## Put your answer to the question here:

## I put that there was a possibility that the type of var could also be a string OR a list.


## Put your reflections/explanations here:

## The reason why 'var' can only be a string and not a list is because of the first if statement.
## If one was to print var[1:3] if var was a list, a list would be returned and it would not be the string "py"
## causing that to fail. However, with var as a string, splitting that string would return the string "py", meeting
## the requirements for everything to print. So, the type of var is only a STRING.


print("\n*******\n")
print ('Midterm Question #10')

## (Midterm 10). What will print when the following code runs? If there will be an error, say so.

stuff = {"purple": [9,106,506,'SI','Yu-Jen','Mauli'],"blue": "Cornflower", 42: "Green"}
print(stuff['purple'][3] + stuff["blue"][0]) 


## Put your answer to the question here:

## I said that an error would occur becuase strings are immutable.


## Put your comment explanations/reflections here:

## It was clear that the answer to this was "SIC". I was thinking that strings are immutable and you cannot add to a string.
## However, becuase both 'SI' and 'C' are from their own entities, we can add them together. The idea that strings
## are immutable is that if I had x = 'hello', I cannot just add on to variable x, I would have to create a new variable
## y = x + "lol" if I wanted to add "lol" to the string 'hello'. But saying print(stuff['purple'][3] + stuff["blue"][0]) 
## is acceptable. I also thought stuff['blue'][0] was "Cornflower" but since stuff['blue'] only has one value, the [0]
## would refer to the first letter which is 'C'.


print("\n*******\n")
print ('Midterm Question #15')

print ('some code here')


## (Midterm 15). (Also refer to the code and instructions on pages 7 and 8 of the midterm PDF.) Write 2 more tests for class Student to check that it does precisely what the description on page 7 says it ought to do. You should create a new test class in which to do put these tests. 

## Note that if you write them here, either they will not run without invoking unittest.main() -- which is OK, you need not do so -- OR they will all fail because the class Student is not defined. Still, we are looking for accurate, syntactically correct tests that will test the methods of class Student as specified in the question.

## Put your answer to the question here:

## That is what I put:
# import unittest

# class test_Student_class(unittest.TestCase):
#     def test_string_method(self):
#         s = Student("David")
#         self.assertEqual(print(s.__str__())), "David has written 0 papers."

#     def test_write_paper(self):
#         s2 = Student("Danielle")
#         s2.write_paper()
#         self.assertEqual(s2.number_papers,1)

#     def test_name_type(self):
#         s3 = Student("Ankita")
#         self.assertEqual(type(s3.name),type(str))

# unittest.main(verbosity=2)

## **These are my corrections**

import unittest

class test_Student_class(unittest.TestCase):

## Put your reflections/explanations here. (Remember, brief.)



print("\n*******\n")
print ('Midterm Question #15 Number 2')
print ('Check Out My Comments')

## Put your answer to the question here:

## The answer that I put was B,D,E where the correct answer was just D and E.


## Put your reflections/explanations here. (Remember, brief.)

## The reason why B is incorrect is becuase when defining functions, all required parameters must be placed 
## before any optional parameters. It would be hard if optional parameters came first because the interpreter
## would not be able to decide which values were to go with what. With D and E, the optional parameters come
## after the required ones.



print("\n*******\n")
print ('THE END')


# Obtained Full Points for Midterm Question 18
# ## (Midterm 18). Given the following code, you want to sort the list saved in lst1 to end up in the following order: ["happy","absence","something","synergy"]. Which of the 3 following named functiosn should be the KEY PARAMETER of the sorted function (replacing the question marks in the commented line below)?

# lst1 = ["happy","absence","synergy","something"]

# # (a)
# def second_elem(x):
#     return x[1]

# # (b)
# def sec_elements(lst):
#     for x in lst:
#         return x

# # (c)
# def sort_by(lst):
#     return len(lst)

# # this is the sorted line that needs one of those names as addition...
# # sorted_lst1 = sorted(lst1, key = ???)


# ## Put your answer to the question here:

# ## Put your reflections/explanations here:

# print("\n*******\n")

# Obtained Full Points for Midterm Question 20
# ## (Midterm 20). Given the following code:

# import requests
# import json
# baseurl = "http://itunes.apple.com/search"
# params = {}
# params["term"] = "Franz Ferdinand"
# params["entity"] = "musicVideo"
# r = requests.get(baseurl, params=params)

# ## What is the type of the variable r?

# # a. A File object
# # b. A BeautifulSoup object
# # c. A Response object
# # d. A string
# # e. A dictionary

# ## Put your answer to the question here:


# ## Put your reflections/explanations here:


