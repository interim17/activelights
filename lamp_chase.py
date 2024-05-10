# me - this DAT
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.
import random

def add_color(r, g, b):
    """Add a new color to the chase sequence."""
    # Assuming colors are provided as 0-1 floats, scale to 255 for 8-bit color values
    chase_colors.append((r, g, b))
    print(f"Added new color: {(r, g, b)}")

def set_transition_duration(seconds):
    """Set the duration of each color transition."""
    global transition_duration
    transition_duration = int(seconds * 60)  # Convert seconds to frames assuming 60 fps
    print(f"Transition duration set to {seconds} seconds")

def generate_random_color():
    """Generate a random RGB color."""
    return (random.random(), random.random(), random.random())

# Function to set the color of the Constant TOP
def set_constant_color(color):
    constant_top = op('lamp_color')  # Adjust 'constant_top' to match your Constant TOP's operator name
    constant_top.par.colorr = color[0]
    constant_top.par.colorg = color[1]
    constant_top.par.colorb = color[2]

# Define the chase pattern
chase_colors = [(0, 0, 1), (1, 0, 0)]  # Blue and Red (Add more colors as needed)

# Initialize frame counter and color index
frame_count = 0
color_index = 0
transition_duration = 32  # Transition over 4 seconds at 60 fps

def onStart():
    global frame_count, color_index
    frame_count = 0
    color_index = 0
    set_constant_color((0, 0, 1))  # Start with black
    print("Start of Chase")

def onCreate():
    print("DAT Created")

def onExit():
    print("Exiting")

def onFrameStart(frame):
    global frame_count, color_index
    frame_count += 1
    transition_progress = frame_count % transition_duration

    # Calculate the current interpolation factor
    t = transition_progress / float(transition_duration)

    # Determine current color and target black
    current_color = chase_colors[color_index]
    target_color = (0, 0, 0)  # Fade to black

    # Scale current color to full 8-bit if not already (assuming RGB values are defined from 0 to 1)
    current_color = tuple(int(c * 255) for c in current_color)

    # Calculate interpolated color fading to black
    interpolated_color = (
        int(current_color[0] * (1 - t)),
        int(current_color[1] * (1 - t)),
        int(current_color[2] * (1 - t))
    )

    print(f"Frame: {frame_count}, t: {t}, Interpolated Color: {interpolated_color}")

    # Update the color on the Constant TOP
    set_constant_color(interpolated_color)

    # Manage color transition end
    if transition_progress == transition_duration - 1:
        color_index = (color_index + 1) % len(chase_colors)
        frame_count = 0  # Reset frame count for the new color's full bright start
        print(f"Transition to next color: {chase_colors[color_index]} at full brightness")
              # Generate and add a random color
        new_color = generate_random_color()
        add_color(*new_color)

def onFrameEnd(frame):
    print("End of Frame")

def onPlayStateChange(state):
    print(f"Play State Changed: {'Paused' if state else 'Playing'}")

def onDeviceChange():
    print("Device Configuration Changed")

def onProjectPreSave():
    print("Project About to be Saved")

def onProjectPostSave():
    print("Project has been Saved")
