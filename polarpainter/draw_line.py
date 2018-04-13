# for details see
# https://docs.google.com/spreadsheets/d/1bt1JF5_E65BAOLYqf0U_qrlKmlzXkmeIPwlu2J2Ue1o/edit?usp=sharing
# Katie Was Here
import subprocess
from time import sleep
from cart_to_bot import cartbot

def set_motor_positions( left_in, right_in ):
    """ set the motor position in ticks """
    TICKS_PER_CM = 1000
    INCHES_PER_CM = 2.54
    resume_motors()
    subprocess.run(args=['ticcmd', '-d', '00203410', '-p', str(int(-1 * left_in * TICKS_PER_CM * INCHES_PER_CM))])
    subprocess.run(args=['ticcmd', '-d', '00203494', '-p', str(int(1 * right_in * TICKS_PER_CM * INCHES_PER_CM))])
    sleep(1)

def resume_motors():
    subprocess.run(args=['ticcmd', '-d', '00203494', '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', '00203494', '--resume'])
    subprocess.run(args=['ticcmd', '-d', '00203410', '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', '00203410', '--resume'])

def reset_positions(left,right):
    """ stop the motors and make encoder position zero) """
    left_tics = left*1000*2.54
    right_tics = right*1000*2.54
    subprocess.run(args=['ticcmd', '-d', '00203410', '--halt-and-set-position', str(int(left_tics))])
    subprocess.run(args=['ticcmd', '-d', '00203494', '--halt-and-set-position', str(int(right_tics))])


# should draw a vertical line downwards,
# if start position is centered between
# the motors


resume_motors()
left,right = cartbot (16,16)
reset_positions(16,16)
print (left, right)


target_left, target_right = cartbot (9,24)
set_motor_positions(16, 16 )
