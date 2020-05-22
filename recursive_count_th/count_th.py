'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # return word.count("th")
    count = 0
    string = word
    
    if word == "":
        return 0
    if not word[0].isalpha():
        return count_th(word[1:])
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

    
none = ""
no = "adas123dasd"
one = "thasdasd"
two = "thethe"

print("None:", count_th(none))
print("No:", count_th(no))
print("One:", count_th(one))
print("Two:", count_th(two))



##### UNDERSTANDING

# takes in a single string (can it be comprised of multiple words, full grammer?)
# counts the instances of "th" (lower case only) that occur within the string
# only use recursion
# STRETCH = Iterate backwards as well?

##### PLanning
# what happens if string is empty?
# what happens if word is not string?
# what happens if string is populated?
    # search the string
        # find a "t" sith next char == "h"
        # check every charac pair, check the pairs
    # what happens if string has no "th"?