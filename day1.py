#importing library to clean up the message
import textwrap

#storing message into a variable naemed message
message = """ Hi! this is Eyasin Arafath from Dhaka. We are going to begin 
our jounry towards leaning python programming language. This is day 1 of our
journy. Here are the things you need to know befroe you also join us
in this journey. 
1. We will use multimple coding assistant such as Gemini, Clause
that will help us as our mentor.
2. We are using VS code as our IDE.
3. We are using github as our version control system.
4. We are using python as our primary language.
5. Our main objective is to be able to build AI agents that will 
solve real life problems 
6. Our learning goal is to become a AI agent developer. 
7. Our learing sylabus is designed in a way so that we only learn what
is necessary for our learning goal.
8. Our learning sylabus is designed in a way so that we only learn what
is necessary for our vission and goal.

__________Best of luck__________"""


#printing the message
print(textwrap.dedent(message).strip())