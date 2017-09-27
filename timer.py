import os
def start_timer():
    times = os.times()
    global start_timer
    start_timer = times[0] + times[1]
    return(start_timer)

def end_timer(message = "total time used:"):
    times = os.times()
    end_time = times[0] + times[1]
    total_time= end_time - start_timer
    print("{:<12s}{:.3f}".format(message,total_time))

if __name__ == "__main__":
    start_timer()

    lines=0
    sum_value=0
    for number in range(1,1000001):
        sum_value += number
    end_timer()
    print(sum_value)
