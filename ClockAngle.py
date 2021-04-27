# This problem was asked by Microsoft.
#
# Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.
#
# Bonus: When, during the course of a day, will the angle be zero?

def clock_angle(time):
    time_list = time.split(':')
    hour = int(time_list[0])
    minute = int(time_list[1])
    if hour == 12 and minute == 0:
        return 0.0
    answer = abs(hour * 30 - minute * 5.5)
    if answer > 180:
        return 360 - answer
    else:
        return answer


if __name__ == '__main__':
    input_time = input('Enter time: ')
    angle = clock_angle(input_time)
    print(angle)
