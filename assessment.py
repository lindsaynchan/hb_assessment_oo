"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction - Object orientation allows us to hide the details of how the 
function is working exactly, which allows for cleaner code. When using a
function, a user only needs to know what input to use and that the function
will produce a particular output. 

Encapsulation - By using object orientation, you can keep the data with 
information regarding the data and how the data can behave. 

Polymorphism - Object orientation allows for the interchangeability of 
components, which cuts down on repetitive code and allows for more fluidity
between data.

2. What is a class?

A class is a type of thing, like a string or a file.

3. What is an instance attribute?

And instance attribute is information regarding an individual instance of a 
class. 

4. What is a method?

A method is a function that relates directly to a specific class. Methods are 
defined within a class, and they usually have at least one parameter.

5. What is an instance in object orientation?

An instance of object orientation is an object that is defined as part of a 
class. That object not only takes on the attributes and methods of that 
particular class, but the object can have attributes that are attributed just
to itself.

For example, this would be an instance of object orientation:

fido = Animal()

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is data that can be applied to a group of objects that share
similarities, while an instance attribute is specific to the object itself.
A class attribute would be if all cats of the class Cats have fur and claws. 
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
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Question class, which requires a question and answer as parameters.
    """

    #instantiating an object in the Question class and requiring a question and
    #answer as arguments
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    #Question class method that asks for an answer to the question and responds
    #with True or False if the user inputted the correct answer or not
    def ask_and_evaluate(self):
        user_answer = raw_input(self.question)
        if user_answer == self.answer:
            return True
        else:
            return False

class Exam(object):
    """Exam class, which requires the name of the student taking the exam.
    """

    #instantiating an object in the Exam class and requiring a name of the
    #student and saves an empty list as the instance attribute
    def __init__(self, name):
        self.name = name
        self.questions = []

    #Exam method, requires question and answer as parameters, adds the question
    #and answer as a tuple to the instance attribute list
    def add_question(self,question,answer):
        self.questions.append((question,answer))

    #Exam method, asks the user the questions attributes and if the user answers
    #correctly, it increases the count; returns count once there's no more 
    #questions
    def administer(self):
        count = 0
        for i in range(len(self.questions)):
            user_answer = raw_input(self.questions[i][0]+" ")
            if user_answer == self.questions[i][1]:
                count += 1
        return count

    #Exam method that calls the administer() method and adds the score as an
    #instance attribute for the Student object
    def take_test(self,student):
        score = self.administer()
        student.score = score
        return score

class Quiz(Exam):
    """Quiz class which inherits from Exam class
    """

    #Quiz method that takes the take_test method and evaluates whether the user
    #received a 50% or more on the quiz
    def take_test(self,student):
        score = super(Quiz, self).take_test(student)
        count_questions = len(self.questions)

        if float(score)/float(count_questions) < .5:
            print "Fail"
        else:
            print "True" 

def example():
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
