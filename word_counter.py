print("------------WELCOME TO WORD COUNTING---------")
#function to count the number of words in the given input sentence or paragraph
def count_words(text):
    words = text.split()
    return len(words)
#function to display the text entered as input
def display_data(text):
    print("Entered data: ", text)
#function to display the individual words in the given input text
def display_words(text):
    print("Words in the entered data is : ", text.split())
#user input 
data = input("Enter a sentence or paragraph: ")
# Basic control flow to check if the input is not empty
if data.strip():
    #to display the entered input text
    display_data(data)
    word_count = count_words(data)
    #to display the individual words of the given input text
    display_words(data)
    #to display the number of words in the given input text
    print("Number of words in the given input text is: ", word_count)
else:
    print("No text entered. Please enter some text.")
