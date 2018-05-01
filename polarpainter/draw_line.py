# for details see
# https://docs.google.com/spreadsheets/d/1bt1JF5_E65BAOLYqf0U_qrlKmlzXkmeIPwlu2J2Ue1o/edit?usp=sharing
# Katie Was Here
import subprocess
from time import sleep
import math
from cart_to_bot import cartbot

TICKS_PER_IN = 125
right_motor_address = '00203410'
left_motor_address = '00203494'


class Artbot:
    def __init__(self, x_in, y_in):
        # input is cartesian x y starting at the top left of the board
        # return value is length of left and right strings
        distance_between_robots = 37  # values in inches
        left_length = math.sqrt(x_in * x_in + y_in * y_in)
        right_length = math.sqrt((distance_between_robots - x_in) * (distance_between_robots - x_in) + y_in * y_in)
        print("{},{} <= cartbot({},{})".format(left_length, right_length, x_in, y_in))
        self.current_left_tics = left_length * TICKS_PER_IN
        self.current_right_tics = right_length * TICKS_PER_IN
        self.reset_positions(self.getLeftIn(),self.getRightIn())

    def getLeftIn(self):
        return self.current_left_tics / TICKS_PER_IN

    def getRightIn(self):
        return self.current_right_tics / TICKS_PER_IN

    def set_cartesian_position(self,x_in,y_in):
        # input is cartesian x y starting at the top left of the board
        # return value is length of left and right strings
        distance_between_robots = 37  # values in inches
        left_length = math.sqrt(x_in * x_in + y_in * y_in)
        right_length = math.sqrt((distance_between_robots - x_in) * (distance_between_robots - x_in) + y_in * y_in)
        print("{},{} <= cartbot({},{})".format(left_length, right_length, x_in, y_in))
        self.set_motor_positions(left_length, right_length)

    def set_relative_positions(self, left_in, right_in):
        self.set_motor_positions((self.current_left_tics / TICKS_PER_IN + left_in),
                                 (self.current_right_tics / TICKS_PER_IN + right_in))

    def set_motor_positions(self, left_in, right_in):
        # set the motor position in ticks
        left_tics = 1 * left_in * TICKS_PER_IN
        right_tics = right_in * TICKS_PER_IN
        print(left_tics, right_tics)
        start_left_tics = subprocess.run(args=['ticcmd', '-d', right_motor_address, '-p', str(int(right_tics))])
        start_right_tics = subprocess.run(args=['ticcmd', '-d', left_motor_address, '-p', str(int(left_tics))])

        self.resume_motors()
        left_distance_in = abs(left_in - self.current_left_tics / TICKS_PER_IN)
        right_distance_in = abs(right_in - self.current_right_tics / TICKS_PER_IN)
        if left_distance_in > right_distance_in:
            max_distance_in = left_distance_in
        else:
            max_distance_in = right_distance_in

        if max_distance_in < 1:
            max_distance_in = 1
        max_distance_in = int(max_distance_in)

        delta_left_tics = (left_tics - self.current_left_tics) /(max_distance_in *2 )
        delta_right_tics = (right_tics - self.current_right_tics) / (max_distance_in*2 )

        for i in range(1, (max_distance_in*2) + 1):

            left_target = self.current_left_tics + i * (delta_left_tics)
            right_target = self.current_right_tics + i * (delta_right_tics)
            print("for i = {}, l {}, r {}".format(i, left_target, right_target))
            subprocess.run(args=['ticcmd', '-d', right_motor_address, '-p', str(int(right_target))])
            subprocess.run(args=['ticcmd', '-d', left_motor_address, '-p', str(int(left_target))])
            sleep(0.8)

        self.current_left_tics = left_tics
        self.current_right_tics = right_tics
        #self.reset_positions(left_in, right_in)

    def resume_motors(self):
        # subprocess.run(args=['ticcmd', '-d', left_motor_address, '--halt-and-hold'])
        subprocess.run(args=['ticcmd', '-d', left_motor_address, '--resume'])
        # subprocess.run(args=['ticcmd', '-d', right_motor_address, '--halt-and-hold'])
        subprocess.run(args=['ticcmd', '-d', right_motor_address, '--resume'])

    def reset_positions(self, left_in, right_in):
        """ stop the motors and make encoder position zero) """
        self.current_left_tics = left_in * TICKS_PER_IN
        self.current_right_tics = right_in * TICKS_PER_IN
        print("resetting positions", self.current_left_tics, self.current_right_tics)

        subprocess.run(
            args=['ticcmd', '-d', right_motor_address, '--halt-and-set-position', str(int(self.current_right_tics))])
        subprocess.run(
            args=['ticcmd', '-d', left_motor_address, '--halt-and-set-position', str(int(self.current_left_tics))])

    def print_status(self):
        subprocess.run(args=['ticcmd', '-d', left_motor_address, '--status', '--full'])
        subprocess.run(args=['ticcmd', '-d', right_motor_address, '--status', '--full'])


if __name__ == "__main__":
    print("hello")

    artbot = Artbot(18.6,14.8)
    # artbot.set_cartesian_position(18.5,20)
    # artbot.set_cartesian_position(18.5, 16)
    # artbot.set_cartesian_position(18.5, 20)
    # artbot.set_cartesian_position(18.5, 28)
    # artbot.set_cartesian_position(18.5, 20)
    # artbot.set_cartesian_position(20.5, 20)
    # artbot.set_cartesian_position(18.5, 20)
    # artbot.set_cartesian_position(16.5, 20)
    artbot.set_cartesian_position(18.6,14.8)
    artbot.set_cartesian_position(21.5, 24.3)
    artbot.set_cartesian_position(13.5, 18.4)
    artbot.set_cartesian_position(23.5, 18.4)
    artbot.set_cartesian_position(15.4, 24.3)
    artbot.set_cartesian_position(18.6,14.8)
    # print_status()

    # print (left, right)
