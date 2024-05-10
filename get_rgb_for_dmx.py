# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	rgb_vals_chop = op('rgb_for_dmx')
	dmx_out_table = op('fixture_chans')

	num_fixtures = 3
	num_dmx_chans = 8
	base_index = 1
	for i in range(num_fixtures):
		base_index
		# Access each RGB value
		r = rgb_vals_chop[0][i]
		g = rgb_vals_chop[1][i]
		b = rgb_vals_chop[2][i]
		
		dmx_out_table[base_index, 1] = r  # DMX channel for Red
		dmx_out_table[base_index + 1, 1] = g  # DMX channel for Green
		dmx_out_table[base_index + 2, 1] = b  # DMX channel for Blue
		base_index += num_dmx_chans

	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return
