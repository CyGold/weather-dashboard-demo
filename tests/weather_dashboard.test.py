#!/usr/bin/env python3

import unittest
from src.weather_dashboard import WeatherDashboard

class TestWeatherDashboard(unittest.TestCase):

    def setUp(self):
        self.weather_dashboard = WeatherDashboard()

if __name__ == '__main__':
    unittest.main()
def test_create_bucket_location_constraint(self):
    self.weather_dashboard.s3_client.head_bucket = mock.Mock(side_effect=self.weather_dashboard.s3_client.exceptions.NoSuchBucket("Bucket does not exist"))
    self.weather_dashboard.s3_client.create_bucket = mock.Mock()

    self.weather_dashboard.create_bucket_if_not_exists()

    self.weather_dashboard.s3_client.create_bucket.assert_called_once_with(
        Bucket=self.weather_dashboard.bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'}
    )