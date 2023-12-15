import string

# def word_frequency(sentence):
#     # Remove punctuation and convert to lowercase
#     translator = str.maketrans("", "", string.punctuation)
#     cleaned_sentence = sentence.translate(translator).lower()

#     # Split the sentence into words
#     words = cleaned_sentence.split()

#     # Count the frequency of each word
#     frequency_dict = {}
#     for word in words:
#         frequency_dict[word] = frequency_dict.get(word, 0) + 1

#     return frequency_dict

# # Test case
# sentence = "This is a test sentence. This sentence is a test."
# result = word_frequency(sentence)
# print(result)

def word_frequency(sentence):
    split_words = sentence.split(" ")
    frequency_tracker = {}
    for word in split_words:
        # in membership operator to check if word is in the tracker
        if word not in frequency_tracker:      
            frequency_tracker.update({word: 1})
        else:
            frequency_tracker[word] +=1            
    return frequency_tracker
    pass

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)