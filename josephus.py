import sys
import argparse


def josephus(n, k):
    """ Function that calculates the last person location
        of the josephus problem

    Args:
        n(int): number of people in circle
        k(int): step rate

    Returns:
        int: index value of the winner

    """
    # special case, k = 1
    if k == 1:
        return n - 1
    # base case, if only one person left, they win
    elif n <= 1:
        return 0
    if k <= n:
        num_dead = n / k
    else:
        num_dead = 1

    # first and last people to die in current round
    # the mod n is applied in case k > n
    first_index = (k - 1) % n
    last_index = first_index + k * (num_dead - 1)

    # which person the next round starts counting from
    next_round_start = last_index + 1

    # recursion to find out who winner is in next round
    winner_next_round = josephus(n - num_dead, k)

    # translate that over to the current round's numbering
    # the people in [next_round_start, n) are all alive
    if next_round_start + winner_next_round < n:
        return next_round_start + winner_next_round
    # look at [0, next_round_start). Some may be dead, adjust.

    else:
        winner_next_round -= (n - next_round_start)
        # every k-th person is dead

        block_num = winner_next_round / (k - 1)
        index_in_block = winner_next_round % (k - 1)
        return block_num * k + index_in_block


def main():
    parser = argparse.ArgumentParser(
        description='Finds location of survivor in josephus problem')
    parser.add_argument(
        'n', type=int, help='No of people in circle'
    )
    parser.add_argument('k', type=int, help='step rate', )
    args = parser.parse_args()
    print "The index position of the survivor is {0}".format(
        josephus(args.n, args.k))


if __name__ == '__main__':
    sys.exit(main())
