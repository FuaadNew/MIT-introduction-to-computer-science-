# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
         #delete this line and replace with your code here
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        
        
        shift_dict = {}
        wrap_around = len(lower_case)
        for i,x in enumerate(lower_case):
            shift_dict[x] = lower_case[(i + shift) % wrap_around]

        for i,x in enumerate(upper_case):
            shift_dict[x] = upper_case[(i + shift) % wrap_around]



        return shift_dict
        



    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        res = ""
        for c in self.message_text:
            if c in shift_dict:
                res+=shift_dict[c]
            else:
                res+=c
        return res

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''

        super().__init__(text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift) 
        
       
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift) 


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text) 

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_count = 0
        best_shift =0
        best_message = ""
        text = self.get_message_text()
        for shift in range(26):
            test_count = 0
            decrypted = self.apply_shift(shift)
            for word in self.decrypted.split():
                if is_word(word_list, word):
                    test_count+=1
            if test_count > best_count:
                best_count = test_count
                best_shift = shift
                best_message = decrypted
        
        return (best_shift, best_message)
        







     #delete this line and replace with your code here

if __name__ == '__main__':

    # ===== MESSAGE CLASS TESTS =====
    print('===== Message Class Tests =====')
    print()

    # Test 1: Message initialization and get_message_text
    print('--- Test 1: Message init and get_message_text ---')
    msg1 = Message('Hello, World!')
    print('Input: "Hello, World!"')
    print('Expected get_message_text(): "Hello, World!"')
    print('Actual get_message_text():', msg1.get_message_text())
    print()

    # Test 2: get_valid_words returns a copy (list)
    print('--- Test 2: get_valid_words ---')
    msg2 = Message('test')
    valid_words = msg2.get_valid_words()
    print('Input: "test"')
    print('Expected: a list of valid words (should not be empty)')
    print('Actual: got', len(valid_words), 'words')
    print('Is "hello" a valid word?', 'hello' in valid_words)
    print()

    # Test 3: build_shift_dict with shift=0 (no change)
    print('--- Test 3: build_shift_dict (shift=0) ---')
    msg3 = Message('abc')
    shift_dict_0 = msg3.build_shift_dict(0)
    print('Input shift: 0')
    print('Expected: a->a, b->b, z->z, A->A')
    print('Actual: a->', shift_dict_0.get('a'), ', b->', shift_dict_0.get('b'), 
          ', z->', shift_dict_0.get('z'), ', A->', shift_dict_0.get('A'))
    print()

    # Test 4: build_shift_dict with shift=2
    print('--- Test 4: build_shift_dict (shift=2) ---')
    msg4 = Message('abc')
    shift_dict_2 = msg4.build_shift_dict(2)
    print('Input shift: 2')
    print('Expected: a->c, b->d, y->a, z->b, A->C')
    print('Actual: a->', shift_dict_2.get('a'), ', b->', shift_dict_2.get('b'),
          ', y->', shift_dict_2.get('y'), ', z->', shift_dict_2.get('z'),
          ', A->', shift_dict_2.get('A'))

    # Test 5: apply_shift
    print('--- Test 5: apply_shift ---')
    msg5 = Message('Hello, World!')
    print('Input: "Hello, World!" with shift=2')
    print('Expected: "Jgnnq, Yqtnf!"')
    print('Actual:', msg5.apply_shift(2))
    print()

    # Test 6: apply_shift with shift=0 (no change)
    print('--- Test 6: apply_shift (shift=0) ---')
    msg6 = Message('abc XYZ!')
    print('Input: "abc XYZ!" with shift=0')
    print('Expected: "abc XYZ!"')
    print('Actual:', msg6.apply_shift(0))
    print()

    # ===== PLAINTEXTMESSAGE CLASS TESTS =====
    print('===== PlaintextMessage Class Tests =====')
    print()

    # Test 1: Basic encryption
    print('--- Test 1: PlaintextMessage basic encryption ---')
    plaintext1 = PlaintextMessage('hello', 2)
    print('Input: "hello" with shift=2')
    print('Expected get_message_text_encrypted(): "jgnnq"')
    print('Actual:', plaintext1.get_message_text_encrypted())
    print('Expected get_shift(): 2')
    print('Actual:', plaintext1.get_shift())
    print()

    # Test 2: Encryption with punctuation and mixed case
    print('--- Test 2: PlaintextMessage with punctuation ---')
    plaintext2 = PlaintextMessage('Hello, World!', 4)
    print('Input: "Hello, World!" with shift=4')
    print('Expected get_message_text_encrypted(): "Lipps, Asvph!"')
    print('Actual:', plaintext2.get_message_text_encrypted())
    print()

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story
