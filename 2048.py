class Block:
    def __init__(self, num):
        self.num = int(num)
        self.merged = False



def update_line(line:list):
    blocks = []
    for i, num in enumerate(line):
        blocks.append(Block(num))
    i = 1
    while i <= 3:
        if blocks[i].num == 0:
            i+=1
            continue

        # move past 0s
        elif blocks[i-1].num == 0:
            blocks[i-1].num = blocks[i].num
            blocks[i].num = 0
            i = i - 1
            continue

        elif blocks[i].num == blocks[i-1].num and not blocks[i-1].merged:
            blocks[i-1].num = blocks[i].num*2
            blocks[i].num = 0
            blocks[i-1].merged = True
            i+=1
        
        else:
            i+=1
    line=[]
    for block in blocks:
        line.append(block.num)
    return line

def print_lines(lines):
    
    for row in lines:
        for num in row:
            print(num, end=" ")
        print()

    
def move_left(lines):
    for i in range(3):
        lines[i] = update_line(lines[i])
    return lines

def move_right(lines):
    for i in range(3):
        lines[i] = update_line(lines[i])
    return lines

def move_up(lines):
    new_lines = [[],[],[],[]]
    for i in range(3):
        for line in new_lines:
            line.append(lines[i])
    for i, line in enumerate(new_lines):
        lines[i] = update_line(line)
    return lines

def move_down(lines):
    new_lines = [[],[],[],[]]
    for i in range(3):
        for line in new_lines:
            line.append(lines[i])
    for i, line in enumerate(new_lines):
        lines[i] = update_line(line)
    return lines



lines = []
lines.append([int(x) for x in input().split()])
lines.append([int(x) for x in input().split()])
lines.append([int(x) for x in input().split()])
lines.append([int(x) for x in input().split()])
move = int(input())

if move == 0:
    lines = move_left(lines)
elif move == 1:
    lines = move_up(lines)
elif move == 2:
    lines = move_right(lines)
else:
    lines = move_down(lines)
print_lines(lines)
