
class ModbusSerialDispatcher:
    def __init__(self):
        self.sender = None

    def cycle_send(self):
        self.sender.read_holding_registers(200, 10, unit=0x1)
        self.sender.read_holding_registers(300, 20, unit=0x1)
