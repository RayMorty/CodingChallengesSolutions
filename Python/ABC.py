def main():
    let = ['A', 'B', 'C']
    N = input()
    L = input()
    nums = [int(x) for x in N.split(" ")]
    sorted_nums = sorted(nums)
    letters = [x for x in L]
    for i in letters:
        index = let.index(i)
        print(sorted_nums[index], end=' ')

if __name__ == "__main__":
    main()