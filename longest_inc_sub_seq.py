
while True:
    try:
        n = int(input())
        nums = [int(x) for x in input().split()]
        pred = [-1] * n
        

        # best is the starting index of the best sequence of each length
        best = [0]
        i = 0

        
        for num in nums[1:]:
            i += 1

            # find the highest index of best where num is greater than the last number in the list
            j = len(best)-1
            while j > -1:
                if nums[best[j]] < num:
                    break
                j -= 1


            # print(f"num: {num}")
            # print(f"j: {j}")
            
            if j == len(best)-1:
                pred[i] = best[j]
                #print(f"best: {best}")
                #print(f"create new best: {i} and set it to j: {j} in pred")
                best.append(i)
                # print(f"best: {best}")
                # print(f"pred: {pred}\n")


            else:
                if j == -1:
                    if nums[best[0]] > num:
                        #print(f"hit 0")
                        # print(f"from 0 set: {best[0][0]} = {num}")
                        pred[i] = -1
                        best[0] = i
                        # print(f"best: {best}")
                        # print(f"pred: {pred}\n")


                elif nums[best[j+1]] > num:  
                    # print(f"set: {best[j+1][-1]} = {num}")
                    #print(f"in pred set i: {i} = {pred[best[j+1]]}")
                    pred[i] = best[j]
                    best[j+1] = i

        index = best[-1]
        indexs = []
        while index != -1:
            indexs.append(index)
            index = pred[index]
        print(len(best))
        for i in indexs[::-1]:
            print(f"{i} ", end="")
        print()


    except EOFError:
        break
