case_num = int(input())


for case in range(case_num):
    people_num = int(input())
    people = []
    nums = []
    longest = 0
    
    for person_num in range(people_num):
        person, _class = input().split(": ")
        people.append([0, person])
        
        num = []
        ranks = _class.split("-")
        if len(ranks) > longest:
            longest = len(ranks)

        for rank in ranks:
            if rank[0] == "u":
                num.append('1')
            elif rank[0] == 'm':
                num.append('2')
            elif rank[0] == 'l':
                num.append('3')
            else:
                num.append('2')
        num.reverse()
        nums.append(num)

    

    for i, num in enumerate(nums):
        while len(num) < longest:
            num.append('2')
        
        
        num = int("".join(num))
        people[i][0] = num

    people.sort()
    for person in people:
        print(person[1])
    
    print("==============================")

        

        



