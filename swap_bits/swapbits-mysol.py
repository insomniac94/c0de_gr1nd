"""Brute-Force Algorithm

Time Complexity = O(1), independent of the word size
"""

class Solution:
    def swap_bits(self, x, i, j):
        return x
    
def main():
    s = Solution()
    test_cases = [
        2198274943350798936,
        1934222162669788191,
        2270450305416888212,
        5820431162416610477,
        7060433214945544085
        ]
    for num in test_cases:
        i = 1
        j = 7
        swapped_number = s.swap_bits(num, i, j)
        print(f'{num} -> {swapped_number}')

if __name__ == '__main__':
    main()