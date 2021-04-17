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
