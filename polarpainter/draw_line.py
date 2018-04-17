# for details see
# https://docs.google.com/spreadsheets/d/1bt1JF5_E65BAOLYqf0U_qrlKmlzXkmeIPwlu2J2Ue1o/edit?usp=sharing
# Katie Was Here
import subprocess
from time import sleep
from cart_to_bot import cartbot

right_motor_address = '00203410'
left_motor_address = '00203494'

def set_motor_positions( left_in, right_in ):
    """ set the motor position in ticks """
    TICKS_PER_IN = 125

    left_tics = 1 * left_in * TICKS_PER_IN
    right_tics =  right_in * TICKS_PER_IN
    print (left_tics, right_tics)


    resume_motors()
    subprocess.run(args=['ticcmd', '-d', right_motor_address, '-p', str(int(right_tics))])
    subprocess.run(args=['ticcmd', '-d', left_motor_address, '-p', str(int(left_tics))])
    sleep(2)
    reset_positions(left_in, right_in)

def resume_motors():
    #subprocess.run(args=['ticcmd', '-d', left_motor_address, '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', left_motor_address, '--resume'])
    #subprocess.run(args=['ticcmd', '-d', right_motor_address, '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', right_motor_address, '--resume'])

def reset_positions(left_in,right_in):
    """ stop the motors and make encoder position zero) """
    left_tics = left_in*125
    right_tics = right_in*125
    print (left_tics, right_tics)

    subprocess.run(args=['ticcmd', '-d', right_motor_address, '--halt-and-set-position', str(int(right_tics))])
    subprocess.run(args=['ticcmd', '-d', left_motor_address, '--halt-and-set-position', str(int(left_tics))])


def print_status():
    subprocess.run(args=['ticcmd', '-d', left_motor_address, '--status', '--full'])
    subprocess.run(args=['ticcmd', '-d', right_motor_address, '--status', '--full'])



# should draw a vertical line downwards,
# if start position is centered between
# the motors
resume_motors()
reset_positions(22, 22)
set_motor_positions(30, 22 )
set_motor_positions(30, 30 )
set_motor_positions(22, 30)
set_motor_positions(22, 22 )
#print_status()

#left,right = cartbot (16,16)

#print (left, right)




