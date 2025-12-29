from ps4b import Message 
from ps4b import PlaintextMessage

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
