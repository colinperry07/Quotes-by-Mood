import json, random

with open('quotes.json', 'r') as file:
    quotes_json = json.load(file)

choosing = True

chosen_category = None

synonyms = {
    "happy" : ['content', 'cheerful', 'proud', 'confident', 'silly', 'energetic'],
    "surprise" : ['startled', 'confused', 'shocked', 'overwhelmed', 'speechless', 'curious'],
    "peaceful" : ['calm', 'loving', 'affectionate', 'trusting', 'relaxed', 'thoughtful'],
    "sad" : ['bored', 'tired', 'lonely', 'guilty', 'disappointed', 'hurt'],
    "anger" : ['mad', 'offended', 'jealous', 'irritated', 'frustrated', 'annoyed'],
    "fear" : ['excluded', 'regret', 'anxious', 'worried','nervous', 'scared',' shy']
}

# a function that checks to see if the users choice word is a synonym for one of the six main emotions
def check_for_synonyms(word):
    for emotion in synonyms:
        if word == emotion:
            return emotion
    for emotion, synonym_list in synonyms.items():
        if word in synonym_list:
            return emotion


# runs all the checks for the user choice process
while choosing:
    
    choice = input("What kind of mood are you in? : ")
    
    # checks to see if the choice is a synonym for one of the quote categories
    choice = check_for_synonyms(choice.lower())

    # checks choice validity
    for category in quotes_json:
        if choice == category:
            chosen_category = category
            
            #loop breaks if user choice is valid
            choosing = False
    
    # otherwise is terminates the program
    if not chosen_category:
        print("Sorry, thats not a mood we have in our system.")
        quit()


# runs through the quotes in the user chosen category and adds them to a list
quote_list = []
for quote in quotes_json[str(chosen_category)]:
    quote_list.append(quote)


# dissects the list and chooses a random quote to print
rand_quote = random.choice(quote_list)
print(rand_quote)