# WeatherDashboard

WeatherDashboard is a Python-based application that fetches real-time weather data for multiple cities using the OpenWeatherMap API and stores the data as JSON files in an Amazon S3 bucket and also visualize this data on Grafana. 
This project demonstrates how to integrate external APIs, process data, and interact with AWS services.

## Features

- Fetches weather data, including temperature, humidity, and conditions, for multiple cities.
- Automatically creates an S3 bucket if it does not already exist.
- Saves weather data in JSON format with timestamped filenames for historical tracking.
- Displays temperature (°F), humidity, and weather conditions

## Prerequisites

1. **Python 3.8 or higher**:  [Download Python](https://www.python.org/downloads/)
2. **AWS Account**: Required to use Amazon S3.
3. **OpenWeather API Key**: Sign up and get your API key from the [OpenWeather website](https://openweathermap.org/api).
4. **AWS CLI configured**: Ensure AWS CLI is installed and configured with credentials. [Set up AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
5. **Dependencies**: boto3 (AWS SDK), python-dotenv and requests.

## ProjectStructure

weather-dashboard-demo/
  src/
    __init__.py
    weather_dashboard.py
  tests/
    weather_dashboard.test.py
  data/
  .env
  .gitignore
  requirements.txt

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CyGold/weather-dashboard-demo.git
   
2. Create a python virtual environment and activate it:
 ```bash
  python3 -m venv myenv
   source myenv/bin/activate 

3. Install dependencies:
```bash
pip install -r requirements.txt

4. Configure environment variables (.env):
```bash
echo OPENWEATHER_API_KEY=your_api_key >> .env
echo AWS_BUCKET_NAME=your_bucket_name{RANDOM} >> .env

4.Configure AWS credentials:
```bash
aws configure

5. Run the application:
```python3 src/weather_dashboard.py

after Installation, if you dont want to incur costs, you empty then delte the S3 bucket on the aws console
## Highlights
 What I Learned
AWS S3 bucket creation and management
Environment variable management for secure API keys
Python best practices for API integration
Git workflow for project development
Error handling in distributed syste
Cloud resource management#
Dynamic Weather Retrieval: Fetches weather data for Houston, Austin, and Dallas in real-time. • Error Handling: Improved resilience for API failures and bucket operations. • Resource Cleanup: Ensures AWS resources are cleaned up properly using the delete action.