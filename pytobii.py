'''
GazeTrack: Python Listener
-
In this example we illustrate how applications
other than Processing can listen to gaze events
generated by the TobiiStream application
-
Before you run this, make sure the
Tobii eye-tracker (EyeX, 4C) is connected
to the computer, and that the Tobii software 
is running and calibrated to your eyes.

Finally, make sure the 'TobiiStream.exe' is 
running and displaying gaze data. You can
download this application from:
http://hci.soc.napier.ac.uk/GazeTrack/TobiiStream.zip
-
You also need to install the zmq Pythong library
before you start: http://zeromq.org/bindings:python

by Augusto Esteves
http://hci.soc.napier.ac.uk
https://github.com/AugustoEst/gazetrack
'''

import zmq

ctx = zmq.Context()
s = ctx.socket(zmq.SUB)
s.connect("tcp://127.0.0.1:5556")

# Uncomment to subscribe to all data streams:
# TobiiStream, TobiiState, TobiiLeftEye, TobiiRightEye, TobiiHeadPose
# s.setsockopt_string(zmq.SUBSCRIBE,'')

# Uncomment to subscribe to the eye position data streams (TobiiLeftEye, TobiiRightEye)
# These are the positions of the user's eyeballs given in space coordinates (mm)
# relative to the center of the screen: # eye available (0, 1), x, y, z, 
# normalized_x, normalized_y, normalized_z
# s.setsockopt_string(zmq.SUBSCRIBE,'TobiiLeftEye')
# s.setsockopt_string(zmq.SUBSCRIBE,'TobiiRightEye')

# Basic example where we subscribe to solely TobiiStream and TobiiState
s.setsockopt_string(zmq.SUBSCRIBE,'TobiiStream')
s.setsockopt_string(zmq.SUBSCRIBE,'TobiiState')			# present, not present

try:
	while True:
		msg = s.recv()
		print(msg)

		# Splits the (byte) message into 
		split_msg = msg.decode("utf-8").split()
		
		if split_msg[0] == 'TobiiStream':
			eyeX = split_msg[2]
			eyeY = split_msg[3]

			# Do as you please...

except KeyboardInterrupt:								# Ctrl+C
	pass

print("Done.")
