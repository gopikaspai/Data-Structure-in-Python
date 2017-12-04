'''A numeric sequence of ai is ordered if a1 < a2 < ... < aN. Let the subsequence
of the given numeric sequence (a1, a2, ..., aN) be any sequence
(ai1, ai2, ..., aiK), where 1 <= i1 < i2 < ... < iK <= N. For example, sequence (1,
7, 3, 5, 9, 4, 8) has ordered subsequences, e. g., (1, 7), (3, 4, 8) and many
others. All longest ordered subsequences are of length 4, e. g., (1, 3, 5, 8).
Your program, when given the numeric sequence, must find the length of its
longest ordered subsequence. The input list contains the elements of
sequence - N integers in the range from 0 to 10000 each. 1 <= N <= 1000.
Your output must contain a single integer that which is the length of the
longest ordered subsequence of the given sequence.

Sample Input
[1, 7, 3, 5, 9, 4, 8]

Sample Output
4 '''


def longest_ordered_subsequence(L):
    n = len(L)
    L_O_S = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if L[i] > L[j] and L_O_S[i] < L_O_S[j] + 1:
                L_O_S[i] = L_O_S[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, L_O_S[i])

    return maximum

def test_suite():
    if longest_ordered_subsequence([1, 7, 3, 5, 9, 4, 8]) == 4:
        print('passed')
    else:
        print('failed')


if __name__ == '__main__':
    test_suite()
