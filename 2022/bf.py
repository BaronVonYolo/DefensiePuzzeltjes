nums = [1, 16, 25, 27, 32, 4, 15]

def forumula(order):

    return (nums[order[0]]-nums[order[1]]) + (nums[order[2]]+nums[order[3]]) + (nums[order[4]]*nums[order[5]]) - nums[order[6]]

def all_perms():
    opl_set = set()

    import itertools
    for it in itertools.permutations([0, 1, 2, 3, 4, 5, 6]):
        opl_set.add(forumula(it))

        print(f'{forumula(it)} {it}')

all_perms() 