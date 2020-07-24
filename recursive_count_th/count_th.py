'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Loop through the word array and return 0 if the words are less than two characters
    if (len(word) < 2):
        return 0

    # If first 2 chars are 'th', it runs again, starting from the next char and add 1 to count the occurance
    count = 0 
    if word[:2] == 'th': 
        count += 1

    # Use recurion for every two letters everytime it's called
    count += count_th(word[1:])

    return count