

def _sorted(nums):
    prev = -1
    for num in nums:
        if num <= prev:
            return False
        prev = num
    return True


while True:

    a, b = input().split()
    a = int(a)
    b = int(b)

    if a == 0:
        break
   
    players = [[] for _ in range(b)]

    for i in range(a): 
        players[i%b].append(i)
    j = 1



    new_list = []
    for player in players:
        for card in player[::-1]:
            new_list.append(card)

    while (not _sorted(new_list)):

        j += 1
        players = [[] for _ in range(b)]
        

        for i, card in enumerate(new_list):
            
            players[i % b].append(card)
        
        new_list = []
        for player in players:
            for card in player[::-1]:
                new_list.append(card)
    
    print(f"j: {j}")
    print(new_list)
    print()
















