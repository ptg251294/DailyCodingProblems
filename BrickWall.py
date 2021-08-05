# This problem was asked by LinkedIn.

# A wall consists of several rows of bricks of various integer lengths and uniform height. Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number of bricks. If the line goes through the edge between two bricks, this does not count as a cut.

# For example, suppose the input is as follows, where values in each row represent the lengths of bricks in that row:

# [[3, 5, 1, 1],
#  [2, 3, 3, 2],
#  [5, 5],
#  [4, 4, 2],
#  [1, 3, 3, 3],
#  [1, 1, 6, 1, 1]]
# The best we can we do here is to draw a line after the eighth brick, which will only require cutting through the bricks in the third and fifth row.

# Given an input consisting of brick lengths for each row such as the one above, return the fewest number of bricks that must be cut to create a vertical line.



wall = [
    [3, 5, 1, 1],
    [2, 3, 3, 2],
    [5, 5],
    [4, 4, 2],
    [1, 3, 3, 3],
    [1, 1, 6, 1, 1]
]


def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num


bricksLengthSumList = []
mergedList = []


def get_brick_length_summation_lists():
    global mergedList
    get_brick_sum_list()
    mergedList = mergedList + temp
    bricksLengthSumList.append(temp)


def get_brick_sum_list():
    for i in range(0, len(wall[wallRow]) - 2):
        if i == 0:
            value = wall[wallRow][i] + wall[wallRow][i + 1]
            temp.append(value)
        else:
            value = temp[i - 1]
            temp.append(wall[wallRow][i + 1] + value)


for wallRow in range(len(wall)):
    temp = []
    get_brick_length_summation_lists()

print('Cut at position: ' + str(most_frequent(mergedList)))


def calculate_cuts():
    cuts_count = 0
    for i in range(len(bricksLengthSumList)):
        if bricksLengthSumList[i].count(8) <= 0:
            cuts_count += 1
    return cuts_count


cuts = calculate_cuts()
print('No of bricks getting cut: ' + str(cuts))
