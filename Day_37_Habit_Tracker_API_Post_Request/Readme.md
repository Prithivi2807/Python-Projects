# Habit Tracker API Project

## Overview
This project is a Python-based habit tracking application that uses the Pixela API to create, update, and manage habit tracking graphs. It allows users to track their daily habits (specifically cycling distance in this implementation) and visualize their progress over time.

## Features
- **User Registration**: Create new users on the Pixela platform
- **Graph Creation**: Create custom graphs for tracking specific habits
- **Data Logging**: Record daily habit data with timestamps
- **Data Updates**: Modify existing habit entries
- **Data Deletion**: Remove specific habit entries
- **API Integration**: Seamless integration with Pixela's REST API

## Technology Stack
- **Language**: Python 3.x
- **API**: Pixela API v1
- **HTTP Library**: Requests
- **Date/Time Handling**: datetime module

## Prerequisites
Before running this project, ensure you have:
- Python 3.x installed
- `requests` library installed (`pip install requests`)
- Internet connection for API calls
- A Pixela account (can be created through the API)

## Installation

1. Clone or download the project files
2. Install required dependencies:
   ```bash
   pip install requests
   ```

## Configuration

The project uses the following configuration variables that can be modified in `Habit_tracker.py`:

```python
USERNAME = ""  # Your Pixela username
TOKEN = ""  # Your Pixela API token
GRAPH_ID = "graph1"  # Unique identifier for your graph
```

### Getting Started with Pixela

1. **Create a User Account** (Uncomment the relevant code):
   ```python
   response = requests.post(url=pixela_endpoint, json=user_params)
   ```

2. **Create a Graph** (Uncomment the relevant code):
   ```python
   response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
   ```

## Usage

### 1. Logging Daily Activity
The main functionality logs cycling distance for the current day:

```python
python Habit_tracker.py
```

When prompted, enter the distance cycled:
```
How many kilometers did you cycle today ? 10.5
```

### 2. API Endpoints Used

#### Base URL
```
https://pixe.la/v1/users
```

#### Endpoints:
- **POST** `/v1/users` - Create new user
- **POST** `/v1/users/{username}/graphs` - Create new graph
- **POST** `/v1/users/{username}/graphs/{graph_id}` - Create pixel (log data)
- **PUT** `/v1/users/{username}/graphs/{graph_id}/{date}` - Update existing pixel
- **DELETE** `/v1/users/{username}/graphs/{graph_id}/{date}` - Delete pixel

### 3. Data Format

**Graph Configuration:**
```json
{
  "id": "graph1",
  "name": "Cycling Graph",
  "unit": "km",
  "type": "float",
  "color": "ajisai"
}
```

**Pixel Data:**
```json
{
  "date": "20250815",
  "quantity": "10.5"
}
```

## Code Structure

### Main Components

1. **Configuration Section**
   - User credentials and API tokens
   - Graph ID and endpoint URLs

2. **User Creation** (Commented out by default)
   - Creates a new user on Pixela platform

3. **Graph Creation** (Commented out by default)
   - Sets up a new graph for tracking cycling distance

4. **Pixel Creation**
   - Logs daily cycling distance with current date

5. **Update Functionality** (Commented out)
   - Allows modification of existing entries

6. **Delete Functionality** (Commented out)
   - Enables removal of specific entries

## Customization

### Changing the Tracked Habit
To track a different habit, modify the graph configuration:

```python
graph_config = {
  "id": "graph1",
  "name": "Reading Graph",  # Change name
  "unit": "pages",         # Change unit
  "type": "int",           # Change type
  "color": "shibafu"       # Change color
}
```

### Adding New Features
You can extend the project by:
- Adding multiple habit graphs
- Implementing batch data entry
- Creating visualization dashboards
- Adding data validation
- Implementing error handling for network issues

## Error Handling

The current implementation includes basic error handling through API responses. Common issues and solutions:

- **401 Unauthorized**: Check your token and username
- **409 Conflict**: Graph or user already exists
- **503 Service Unavailable**: Pixela service temporarily down

## Viewing Your Data

After logging data, view your graph at:
```
https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html
```

## Example Workflow

1. **First Time Setup**:
   ```bash
   # Uncomment user creation code and run once
   python Habit_tracker.py
   
   # Uncomment graph creation code and run once
   python Habit_tracker.py
   ```

2. **Daily Usage**:
   ```bash
   # Keep only pixel creation code uncommented
   python Habit_tracker.py
   # Enter distance when prompted
   ```

## Security Notes

- Never commit your actual API token to version control
- Use environment variables for sensitive data in production
- The token provided in the code is for demonstration purposes

## Troubleshooting

### Common Issues

1. **Import Error**: Install requests library
   ```bash
   pip install requests
   ```

2. **Connection Error**: Check internet connection

3. **API Errors**: Verify your username and token are correct

4. **Date Format**: Ensure date is in YYYYMMDD format

## Future Enhancements

- Web interface for easier data entry
- Mobile app integration
- Multiple habit tracking
- Data export functionality
- Statistical analysis and trends
- Reminder notifications
- Integration with fitness trackers

## Support

For Pixela API support, visit: https://docs.pixe.la/
