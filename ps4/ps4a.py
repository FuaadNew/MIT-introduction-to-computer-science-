# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    res = []
    counts = {}
    for num in sequence:
        counts[num]= 1 + counts.get(num,0)
    def dfs(substr,count):
        if len(substr) == len(sequence):
            res.append("".join(substr[:]))
            return
        for num in count.keys():
            if count[num] > 0:
                substr.append(num)
                count[num]-=1
                dfs(substr,count)
                substr.pop()
                count[num]+=1
    dfs([],counts)
    return res


        

    

if __name__ == '__main__':
    # Test Case 1: Single character (base case)
    print('--- Test Case 1 ---')
    test1 = 'a'
    print('Input:', test1)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(test1))
    print()

    # Test Case 2: Two characters
    print('--- Test Case 2 ---')
    test2 = 'ab'
    print('Input:', test2)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(test2))
    print()

    # Test Case 3: Three characters (original example)
    print('--- Test Case 3 ---')
    test3 = 'abc'
    print('Input:', test3)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(test3))
    print()

    # Bonus Test Case 4: String with duplicate characters
    print('--- Test Case 4 (Bonus: duplicates) ---')
    test4 = 'aab'
    print('Input:', test4)
    print('Expected Output:', ['aab', 'aba', 'baa'])
    print('Actual Output:', get_permutations(test4))

