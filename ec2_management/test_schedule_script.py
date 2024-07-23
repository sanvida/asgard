import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import ec2_management.schedule_script as schedule_script
import os

INSTANCE_ID = os.getenv('INSTANCE_ID')

class TestEC2Management(unittest.TestCase):

    @patch('schedule_script.ec2.Instance')
    def test_start_instance(self, mock_instance):
        # Mock the instance state and start method
        instance = mock_instance.return_value
        instance.state = {'Name': 'stopped'}
        instance.start = MagicMock()
        instance.wait_until_running = MagicMock()

        schedule_script.start_instance(INSTANCE_ID)

        instance.start.assert_called_once()
        instance.wait_until_running.assert_called_once()

    @patch('schedule_script.ec2.Instance')
    def test_stop_instance(self, mock_instance):
        # Mock the instance state and stop method
        instance = mock_instance.return_value
        instance.state = {'Name': 'running'}
        instance.stop = MagicMock()
        instance.wait_until_stopped = MagicMock()

        schedule_script.stop_instance(INSTANCE_ID)

        instance.stop.assert_called_once()
        instance.wait_until_stopped.assert_called_once()

    @patch('schedule_script.datetime')
    @patch('schedule_script.ec2.Instance')
    def test_schedule_instance(self, mock_instance, mock_datetime):
        # Mock the datetime to simulate different times and days
        mock_now = datetime(2023, 7, 24, 9, 30, 0)  # Monday
        mock_datetime.utcnow.return_value = mock_now

        instance = mock_instance.return_value
        instance.state = {'Name': 'stopped'}
        instance.start = MagicMock()
        instance.stop = MagicMock()
        instance.wait_until_running = MagicMock()
        instance.wait_until_stopped = MagicMock()

        with patch('time.sleep', return_value=None):  # Skip sleeping
            schedule_script.schedule_instance()

        instance.start.assert_called()
        instance.stop.assert_not_called()

if __name__ == '__main__':
    unittest.main()
