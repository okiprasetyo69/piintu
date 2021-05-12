def palindrome(val) :
    reverse_sentece = str(val)[::-1]
    if val.lower() == reverse_sentece.lower():
        print('Sentence : "{}" is palindrome'.format(val))
    else:
        print('Sentence : "{}" is not palindrome'.format(val))

    if reverse_sentece.lower() == val.lower():
        return True
    return False

input_sentences = input('Please input sentence palinrdrome ! : ')
print('The sentence : ' + str(input_sentences))
print(palindrome(input_sentences))