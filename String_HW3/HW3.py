
# define sort of constants
JOIN_DELIMITER = ' '
SENTENCE_DELIMITER = '. '
DOT_DELIMITER = '.'

def last_words(str):
    # divide text by spaces and extract words with other symbols like '.', ',' etc
    list_of_words = str.split()
    last_word_list = []
    # if substring contains '.', add to the collection as last word in sentence
    for word in list_of_words:
        if word.endswith(DOT_DELIMITER):
            last_word_list.append(word.replace(DOT_DELIMITER, ""))

    return last_word_list

# divide text by '.'; for each sentence remove spaces before and after text and make first letter of the sentence big one;
# join all sentence with '. '
def capitalize(str):
    return SENTENCE_DELIMITER.join([sentence.strip().capitalize() for sentence in str.split('.')])

if __name__ == '__main__':
    # copy text in variable
    str = """ tHis iz your homeWork, copy these Text to variable.
    
    
     You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    
    
     it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
    
    
     last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
    """

    # make lowercase for further changes
    norm_str = str.lower()
    # replace iz to is
    norm_str = norm_str.replace(' iz ', ' is ')
    # clean spaces, capitalize first letter
    norm_str = capitalize(norm_str)
    # take this text as marker for finding needed index
    place_for_insert = 'paragraph.'
    # create new string with added last words in text
    str_with_last_words = (norm_str[:norm_str.index(place_for_insert) + len(place_for_insert) + 1]
                           + JOIN_DELIMITER.join(last_words(norm_str))
                           + norm_str[norm_str.index(place_for_insert)  + len(place_for_insert):])
    print(str_with_last_words)
    # symbol by symbol check if the char is related to whitespace, and sum the results if yes
    whitespaces = sum(1 for char in str if char.isspace())
    print(f'Whitespaces: {whitespaces}')