#!/anaconda3/bin/python3

import subprocess
from time import sleep

def set_motor_speeds( left, right, seconds ):
    for _ in range( int(seconds * 10) ):
        subprocess.run(args=['ticcmd', '-d', '00203410', '-y', str(left)])
        subprocess.run(args=['ticcmd', '-d', '00203494', '-y', str(-1*right)])
        sleep(0.1)

def resume_motors():
    subprocess.run(args=['ticcmd', '-d', '00203494', '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', '00203494', '--resume'])
    subprocess.run(args=['ticcmd', '-d', '00203410', '--halt-and-hold'])
    subprocess.run(args=['ticcmd', '-d', '00203410', '--resume'])

resume_motors()
set_motor_speeds( -1000000, -1000000, 5.0 ) # up
set_motor_speeds( 1000000, -1000000, 5.0 ) # right
set_motor_speeds( 1000000, 1000000, 5.0 ) # down
set_motor_speeds( -1000000, 1000000, 5.0 ) # left
set_motor_speeds( 0, 0, 0.5 )

