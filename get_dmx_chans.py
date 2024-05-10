dmx_chans_table = op('dmx_chans_table')
fixture_offsets_table = op('lamp_fixture_offsets')
content_null = op('lamp_out_null')

fixture_chans = op('fixture_chans')
fixture_chans.clear()

dmx_chans_table.clear()
fixture_offsets_table.clear()

current_channel = 0
channel_offest = 8
total_fixtures = 3
current_fixture = 0
channels = ['dimmer', 'r', 'g', 'b', 'amber', 'white', 'ultraviolet', 'strobe']

while current_fixture < total_fixtures:
    start_channel = current_channel
    # for channel in channels:
    for index, channel in enumerate(channels):
        print(index)
        print(current_channel)
        value = 0
        if index == 0:
            value = 255
        if index == current_fixture + 1:
            value = 255
        dmx_chans_table.appendRow([current_fixture, channel, current_channel, value])
        fixture_chans.appendRow([f"chan{current_channel}", value])
        current_channel += 1
    fixture_offsets_table.appendRow([current_fixture + 1, start_channel+1, current_channel])
    current_fixture += 1
