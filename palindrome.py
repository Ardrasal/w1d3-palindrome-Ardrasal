def palindrome(text): 
    """Takes a string, converts it into all lower case letters and ignores spaces and punctuation, and determines if it's a palindrome."""

    if len(text) <= 1:
        return True
    # if len(text) > 1:
    #     return Falsey
      
def clean_text(words):
    """"This function will clean up the text by removing white space, converting to lowercase, and only selecting alphabetic characters."""
    words = words.lower()
    new_words = ""
    for char in words:
        if char.isalpha():
            new_words = new_words + char
    # print(new_words)
    return new_words

def inner(alpha):
    """start with full phrase and then reduce each side by 1 letter"""
    # clean_text = clean_text (trying to figure out how to store but this didn't work)
    # print(alpha)
    if len(alpha) > 1:
        inner(alpha [1:-1])
        # need to compare first and last letters
    # print(alpha[0])
    # print(alpha[-1])
    if alpha[0] == alpha[-1]:
        return True
    else:
        return False

test_case = input("Test your word or phrase here to find out if it's a palindrome: ")

palindrome(test_case)
# # is palindrome function needed?
test_case = clean_text(test_case)
new_words = inner(new_words)
# # print(clean_test_case(test_case))
# # Compare first and last letters and work in.
# # make sure that it's called in the proper order

if True:
    print("is a palindrome")
if False:
    print("is not a palindrome")
    