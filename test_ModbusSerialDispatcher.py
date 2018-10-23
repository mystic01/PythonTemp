import ModbusSerialDispatcher as MyModule
import unittest
from unittest.mock import MagicMock
from unittest import mock


class TestModbusSerialDispatcher(unittest.TestCase):
    def Read(self, station_number):
        if station_number == 1:
            return MyModule.StationSetting(interval=100, addr=200, len=10)
        elif station_number == 2:
            return MyModule.StationSetting(interval=200, addr=300, len=20)
        return None

    def test_cycle_dispatch_by_files(self):
        # Arrange
        dispatcher = MyModule.ModbusSerialDispatcher()
        reader = MyModule.SettingFileReader()
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


if __name__ == '__main__':
    unittest.main()
