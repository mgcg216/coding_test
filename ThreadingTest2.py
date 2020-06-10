from threading import Timer
import sys
def wait_for(answer, error_message):
    answer_timer = Timer(10, answer_not_found, args=error_message)
    robot_answer = ""

    # loop to find answer, if answer is not found after 10 seconds print error message
    while robot_answer != answer:

        if answer == -1 & answer_timer.is_alive() is False:
            answer_timer.start()
            answer_timer.join()

        elif answer != -1:
            robot_answer = answer

    answer_timer.cancel()
    print('Received: %s' % robot_answer)
    sys.stdout.flush()


