"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction - Object orientation allows us to hide the details of how the 
function is working exactly, which allows for the code to be cleaner. When using 
a function, a user only needs to know what kind of input to add and what kind
of output the function will give. The user of the function doesn't need to see
every step the function takes to make this happen every time they use the 
function. 

Encapsulation - By using object orientation, you can keep the information about 
the data and how the data can behaves together. The attributes of the data as
well the methods that can be used with the data will live in one location.  

Polymorphism - Object orientation allows for the interchangeability of 
components, which cuts down on repetitive code and allows for more fluidity
between data. 

2. What is a class?

A class is a type of object, like a string or a file.

3. What is an instance attribute?

An instance attribute is information regarding an object that is an 
instance of a class. 

4. What is a method?

A method is a function that relates directly to a specific class. Methods are 
defined within a class, and they usually have at least one parameter (self).

5. What is an instance in object orientation?

An instance of object orientation is an object that is defined as part of a 
class. That object not only takes on the attributes and methods of that 
particular class, but the object can have attributes that are attributed to just
itself.

For example, this would be an instance of object orientation:

fido = Animal()

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is data that can be applied to a group of objects that share
similarities, while an instance attribute is specific to the object itself.
A class attribute would be if all cats of the class Cats have paws and claws. 
However, an instance attribute would be if spaghetti was the favorite food of 
"Whiskers", a specific cat (whiskers.favoritefood = "spaghetti"). 

"""
################################################################################

"""Part 2 - 5

"""

class Student(object):
    """Student class, which requires the parameters of first name, last name,
    and address.

    Saves the parameters as instance attributes to the instantiated object."""


    def __init__(self,first_name,last_name,address):
        """instantiating and object that requires first name, last name and 
        address as arguments
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Question class, which requires a question and answer as parameters.
    """

    def __init__(self, question, answer):
    """instantiating an object in the Question class and requires a question and
    #answer as arguments
    """
        self.question = question
        self.answer = answer


    def ask_and_evaluate(self):
        """Question class method that asks the user for an answer to the 
        question and responds with True or False if the user inputted the 
        correct answer or not
        """
        #ask user question and saves answer as variable
        user_answer = raw_input(self.question)
        #if user_answer is equal to the answer in the tuple
        if user_answer == self.answer:
            #return True
            return True
        #else return False
        else:
            return False

class Exam(object):
    """Exam class, which requires the name of the student taking the exam.
    """


    def __init__(self, name):
        """instantiating an object in the Exam class and requiring a name of the
        student and saves an empty list as the questions instance attribute
        """
        self.name = name
        self.questions = []

    def add_question(self,question,answer):
        """Exam method, requires question and answer as parameters, adds the 
        question and answer as a tuple to the instance attribute list
        """
        self.questions.append((question,answer))


    def administer(self):
        """Exam method, asks the user the questions attributes and if the user 
        answers correctly, it increases the count; returns count once there's 
        no more questions
        """
        #set count to 0
        count = 0

        #iterate through the questions using index
        for i in range(len(self.questions)):
            #ask user the question
            user_answer = raw_input(self.questions[i][0]+" ")
            #if user answer == answer in tuple
            if user_answer == self.questions[i][1]:
                #increase count
                count += 1
        return count


    def take_test(self,student):
        """Exam method that calls the administer() method and adds the score as 
        an instance attribute for the Student object
        """

        #call administer method and save as variable
        score = self.administer()
        #save score as student score attribute
        student.score = score
        return score

class Quiz(Exam):
    """Quiz class which inherits from Exam class
    """


    def take_test(self,student):
        """Quiz method that takes the take_test method and evaluates whether 
        the user received a 50 percent or more on the quiz
        """
        
        #saves the parent class take_test output as a variable
        score = super(Quiz, self).take_test(student)
        #finds the number of questions
        count_questions = len(self.questions)

        #if the percent of questions answered correctly is less than 50 percent
        if float(score)/float(count_questions) < .5:
            #return fail
            print "Fail"
        #otherwise print pass
        else:
            print "Pass" 

def example():
    """example that instantiates an object for Quiz/Exam, adds questions to 
    a list, instantiates an object for Student and call take_test method
    """
     
    example = Quiz("example")
    example.add_question("What is 5 * 5?","25")
    example.add_question("What color is the sky?","Blue")
    example.add_question("What is the capital of CA?","Sacramento")
    bob = Student("Bob","Smith","123 Sutter St.")
    example.take_test(bob)

example()






###############################################################################

# Parts 2 through 5:
# Create your classes and class methods
