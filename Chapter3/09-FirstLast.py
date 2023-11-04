# First-Last
#  - Create a function first_last()
#  - Takes in a sequence (string, list, tuple)
#  - Returns the first and last elements of the sequence

def first_last(sequence):
    return sequence[:1] + sequence[-1:]

def even_odd_sums(sequence):
    # Get the sum of all even indexed numbers and all odd indexed numbers
    return [sum(sequence[0::2]), sum(sequence[1::2])]

def plus_minus(sequence):
    # Alternate adding and subtracting sequence numbers [0 + 1 - 2 + 3]
    return sum(sequence[:2]) + sum(sequence[3::2]) - sum(sequence[2::2])

if __name__ == '__main__':
    print(first_last("abc"))
    print(first_last([1,2,3,4]))
    print(first_last((1,2,3,4)))
    print(even_odd_sums([10,20,30,40,50,60]))
    print(plus_minus([10,20,30,40,50,60]))