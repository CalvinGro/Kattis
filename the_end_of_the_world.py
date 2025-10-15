while True:
    s = input()
    if s == 'X':
        break

    # CREATE NUMS LIST
    nums = [0] * len(s)
    for i, c in enumerate(s):
        if c == 'A':
            nums[i] = 1
        elif c == 'B':
            nums[i] = 2
        else:
            nums[i] = 3
    # print(f"nums: {nums}")

    # DEFINE SHIFT
    shift = {0:0}
    i = 0
    while i < len(nums):
        i += 1 
        shift[i] = (shift[i-1] * 2) + 1
    # print(f"shift: {shift}")

    # MAIN LOOP
    total = 0
    len_remaining = len(nums)
    target = 2

    for num in nums[::-1]:
        len_remaining -= 1
        # print(f"len_remaining: {len_remaining}")
        if num == target:
            continue
        target = 6 - target - num
        total += 1
        total += shift[len_remaining]
    print(total)
