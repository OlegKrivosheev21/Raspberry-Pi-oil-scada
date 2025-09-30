pump_state = {"status": "OFF"}

def turn_on():
    pump_state["status"] = "ON"
    return pump_state

def turn_off():
    pump_state["status"] = "OFF"
    return pump_state
