

# defines the main function
def main():
    banner()
    new_sentence = input('Please enter a sentence: ')
    converted = camelCase_conversion(new_sentence)
    print(converted)

# converts the sentence passed to it - changes everything to lower case, splits it on space, iterates over the length of the list
# adds the first one to the list with no changes after being made lower case, it will then capitalize each subsequent item while appending it to the list.
# Finally it joins them all together into one string and returns it.
def camelCase_conversion(sentence):
    i = 0
    converted_sentence = []
    lowercase_sentence = sentence.lower()
    seperated_sentence = lowercase_sentence.split()
    space = ''
    while i < len(seperated_sentence):
        if i >=1:
           capital_word = seperated_sentence[i].capitalize()
           converted_sentence.append(capital_word)
        elif i == 0:
            converted_sentence.append(seperated_sentence[0])   
        i += 1
    combined = space.join(converted_sentence)
    return combined

def banner():
    """Display program name"""
    message = "Awesome camelcase program!!"
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')


main()        