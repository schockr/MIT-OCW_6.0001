# Problem Set 4A
# Name: Robert Schock

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

    
    # define helper function for recursion
    def perm(sequence, n, permutations):
        '''
        Perform permutations of string and append to list using Heap's algorithm
        
        sequence (list): character array (list) of the target string on which permutations
        are being conducted

        n (integer): starts as length of string, gets decremented on each recursive call
        
        permutations (list): the final list of all permutations. 
        
        Returns a list of all permutations of a sequence
                
        '''

        # base case    
        if n==1:
            # only append if permutation doesn't already exist in list
            str_seq = ''.join(sequence)
            if permutations.count(str_seq) == 0:
                permutations.append(str_seq)
        else:
            for i in range(n):
                
                # recursively call function with one smaller substring
                perm(sequence,n-1, permutations)
                
                # if size is even, we want to swap 2 characters. Else swap first and last characters
                if n%2==0:
                    sequence[0],sequence[n-1] = sequence[n-1],sequence[0]
                else:
                    sequence[i],sequence[n-1] = sequence[n-1],sequence[i]
        return permutations
    
    
    # Cleanse input
    sequence = sequence.lower().strip()    

    # initialize list to store all permutations
    permutations = []

    return perm(list(sequence), len(sequence), permutations)
    


if __name__ == '__main__':
#    #EXAMPLE
    # listofwords=[]
    # print(heaps_func(list('abc'),len('abc'),listofwords))
    
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    tc1_input = 'test'
    print('Input:', tc1_input)
    print('Expected Output:', ['test','etst','stet','estt','sett','ttse','stte','tste','etts','tets','ttes'])
    print('Actual Output:', get_permutations(tc1_input))

    tc2_input = 'b1c'
    print('Input:', tc2_input)
    print('Expected Output:', ['b1c','1bc','cb1','bc1','1cb','c1b'])
    print('Actual Output:', get_permutations(tc2_input))

    tc3_input = 'ahh'
    print('Input:', tc3_input)
    print('Expected Output:', ['ahh','hah','hha'])
    print('Actual Output:', get_permutations(tc3_input))

