def palindrome(text):
    """Takes a string, converts it into all lower case letters and ignores spaces and punctuation, and determines if it's a palindrome."""

    # if len(text) <= 1:
    #     return True
      
def clean_text(words):
    """"This function will clean up the text, remove white space, lowercase, and only select alphabetic characters."""
    words = words.lower()
    new_words = ""
    for char in words:
        if char.isalpha():
            new_words = new_words + char
    return new_words

def inner(clean_text):
    """start with full phrase and then reduce each side by 1 letter"""
    # clean_text = clean_text (trying to figure out how to store but this didn't work)
    print(clean_text)
    if len(clean_text) > 1:
        inner(clean_text [1:-1])
        # need to compare first and last letters
    # print(clean_text[0])
    # print(clean_text[-1])
    if clean_text[0] == clean_text[-1]:
        return True
    else:
        return False

# def letter_check(letters): didn't need this one
    """Compare the first and last letters of each iteration of the shrinking phrase, to see if they are equal"""
    
# # ignore punctuation 

test_case = input("Test your word or phrase here to find out if it's a palindrome: ")

test_case = clean_text(test_case)
inner(test_case)
# # print(clean_test_case(test_case))
# Compare first and last letters and work in.
# make sure that it's called in the proper order

if True:
    print("is a palindrome")
if False:
    print("is not a palindrome")
    