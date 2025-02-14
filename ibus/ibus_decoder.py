from ibus_reader import ibus_reader

def map_to_linear_command(value, in_min=1000, in_max=2000, out_min=-1.0, out_max=1.0):
    return -1*(round((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min,2))

def map_to_sw_command(value):
    if value == 1000:
        return 0
    elif value == 1500:
        return 3
    else:
        return 1


controller = ibus_reader()
while True:
    
    controller.read_serial_data()
    
    controller.linear_y = map_to_linear_command(controller.linear_y)
    controller.linear_x = map_to_linear_command(controller.linear_x)
    controller.yellow_sw = map_to_sw_command(controller.yellow_sw)
    controller.red_sw = map_to_sw_command(controller.red_sw)
    controller.long_sw = map_to_sw_command(controller.long_sw)
    controller.system_troubleshoot()

