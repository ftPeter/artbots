#!/anaconda3/bin/python3
#
# for details see
# https://docs.google.com/spreadsheets/d/1bt1JF5_E65BAOLYqf0U_qrlKmlzXkmeIPwlu2J2Ue1o/edit?usp=sharing

import subprocess
from time import sleep

def set_motor_speeds( left, right, seconds ):
    for _ in range( int(seconds * 10) ):
        subprocess.run(args=['ticcmd', '-d', '00203410', '-y', str(left)])
        subprocess.run(args=['ticcmd', '-d', '00203494', '-y', str(-1*right)])
        sleep(0.1)

def set_motor_positions( left_cm, right_cm ):
    """ set the motor position in ticks """
    TICKS_PER_CM = 1000
    resume_motors()
    subprocess.run(args=['ticcmd', '-d', '00203410', '-p', str(left_cm * TICKS_PER_CM)])
    subprocess.run(args=['ticcmd', '-d', '00203494', '-p', str(-1 * right_cm * TICKS_PER_CM)])
    sleep(0.1)

def resume_motors():
    subprocess.run(args=['ticcmd', '-d', '00203494', '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', '00203494', '--resume'])
    subprocess.run(args=['ticcmd', '-d', '00203410', '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', '00203410', '--resume'])

def reset_positions():
    """ stop the motors and make encoder position zero) """
    subprocess.run(args=['ticcmd', '-d', '00203410', '--halt-and-set-position', '0'])
    subprocess.run(args=['ticcmd', '-d', '00203494', '--halt-and-set-position', '0'])

# should draw a vertical line downwards,
# if start position is centered between
# the motors

reset_positions()
resume_motors()
set_motor_positions(1.414213562, 1.414213562)
set_motor_positions(2.059126028, 2.059126028)
set_motor_positions(2.785677655, 2.785677655)
set_motor_positions(3.544009029, 3.544009029)
set_motor_positions(4.317406629, 4.317406629)
set_motor_positions(5.099019514, 5.099019514)

