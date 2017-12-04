'''A supermarket has a set ‘Prod’ of products on sale. It earns a profit px for
each product x∈Prod sold by a deadline dx that is measured as an integral
number of time units starting from the moment the sale begins. Each
product takes precisely one unit of time for being sold. A selling schedule is
an ordered subset of products Sell ≤ Prod such that the selling of each
product x∈Sell, according to the ordering of Sell, completes before the
deadline dx or just when dx expires. The profit of the selling schedule is
Profit(Sell)=Σx∈Sellpx. An optimal selling schedule is a schedule with a
maximum profit.


For example, consider the products Prod={a,b,c,d} with (pa,da)=(50,2),
(pb,db)=(10,1), (pc,dc)=(20,2), and (pd,dd)=(30,1). The possible selling
schedules are listed in table 1. For instance, the schedule Sell={d,a} shows
that the selling of product d starts at time 0 and ends at time 1, while the
selling of product a starts at time 1 and ends at time 2. Each of these
products is sold by its deadline. Sell is the optimal schedule and its profit is
80.


Write a program that reads sets of products from the input and computes the
profit of an optimal selling schedule for each set of products. Your input
must be a list of n pairs (pi, di) of integers, that designate the profit and the
selling deadline of the i-th product. Note: 0 < n < 100, 1 <= pi <= 1000 and
1 <= di <= 1000. For output, the program returns the profit of an optimal
selling schedule for the set.


Sample Input 1
[(50, 2), (10, 1), (20, 2), (30, 1)]


Sample Output 1
80


Sample Input 2
[(20, 1), (2, 1), (10, 3), (100, 2), (8, 2), (5,
20), (50, 10)]


Sample Output 2
185'''

def supermarket(Items):
    s_items = sorted(Items, key=lambda x: x[0])
    s_items.reverse()
    l1 = []
    for i in range(0, len(s_items)):
        l1.append(s_items[i][1])
        deadline = max(l1)

        time_allotted = [0] * (deadline + 1)

    for i in range(0, len(s_items)):
        k = min(deadline, s_items[i][1])
        if k > 0:
            if time_allotted[k] == 0:
                time_allotted[k] = s_items[i][0]

            elif time_allotted[k] != 0:
                for j in range(k, 0, -1):
                    if time_allotted[j] == 0:
                        time_allotted[j] = s_items[i][0]
                        break
            else:
                pass

    optimal_solution = 0
    for i in time_allotted:
        optimal_solution += i

    return optimal_solution

def test_suite():
    if supermarket([(50, 2), (10, 1), (20, 2), (30, 1)]) == 80:
        print('passed')
    else:
        print('failed')

if __name__ == '__main__':
    test_suite()
