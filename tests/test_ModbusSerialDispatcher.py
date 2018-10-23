from unittest import mock
from unittest.mock import MagicMock
import unittest
from modbus.modbusSerialDispatcher import *
from modbus.settingFileReader import *
from modbus.stationSetting import *


class TestModbusSerialDispatcher(unittest.TestCase):
    def Read(self, station_number):
        if station_number == 1:
            return StationSetting(interval=100, addr=200, len=10)
        elif station_number == 2:
            return StationSetting(interval=200, addr=300, len=20)
        return None

    def test_cycle_dispatch_by_files(self):
        # Arrange
        dispatcher = ModbusSerialDispatcher()
        reader = SettingFileReader()
        reader.Read = self.Read

        dispatcher.setting_file_reader = reader

        senderMock = MagicMock()
        dispatcher.sender = senderMock

        # Act
        dispatcher.cycle_send()

        # Assert
        calls = [mock.call(200, 10, unit=0x1), mock.call(300, 20, unit=0x1)]
        senderMock.read_holding_registers.assert_has_calls(
            calls, any_order=True)
