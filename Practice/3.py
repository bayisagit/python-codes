def read_list(n):
    lists = []
    for i in range(n):
        mark = int(input("Mark of list {}: ".format(i+1)))
        lists.append(mark)
    return lists

def find_max(lists):
    maxs = max(lists)
    return maxs

def find_min(lists):
    mins = min(lists)
    return mins

def find_range(maxs, mins):
    range = maxs - mins
    return range

def find_mean(lists):
    mean = sum(lists) / len(lists)
    return mean

def main():
    n = int(input("How many marks do you want to record: "))
    lists = read_list(n)
    maxs = find_max(lists)
    mins = find_min(lists)
    range = find_range(maxs, mins)
    mean = find_mean(lists)

    print("******************************************")
    print("Display list:")
    print(lists)
    print("******************************************")
    print("Max\tMin\tRange\tMean")
    print("******************************************")
    print("{}\t{}\t{}\t{}".format(maxs, mins, range, mean))

if __name__ == "__main__":
    main()