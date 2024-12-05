def control_pump(water_level, threshold_low=10, threshold_high=40):
    """
    Control pump state based on water level.
    Turn ON if water level is below the low threshold.
    Turn OFF if water level exceeds the high threshold.
    """
    if water_level < threshold_low:
        return "Pump ON"
    elif water_level > threshold_high:
        return "Pump OFF"
    return "Pump IDLE"
