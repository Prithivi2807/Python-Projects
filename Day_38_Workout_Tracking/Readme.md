# Workout Tracker 🏃‍♂️

A Python-based workout tracking application that automatically logs your exercises to Google Sheets using the Nutritionix API and Sheety API.

## Features

- **Natural Language Input**: Simply describe your workout in plain English
- **Automatic Data Logging**: Logs exercise name, duration, calories burned, date, and time
- **Google Sheets Integration**: Stores all workout data in a structured Google Sheet
- **Personalized Calculations**: Uses your personal stats for accurate calorie calculations

## Setup Guide

### Prerequisites

- Python 3.7+
- Google Sheet with Sheety API configured
- Nutritionix API account

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/workout-tracker.git
   cd workout-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install requests
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   GENDER=your_gender
   WEIGHT_KG=your_weight
   HEIGHT_CM=your_height
   AGE=your_age
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key
   AUTH_TOKEN=your_sheety_auth_token
   ```

### API Setup

1. **Nutritionix API**
   - Sign up at [Nutritionix](https://developer.nutritionix.com/)
   - Get your APP_ID and API_KEY from the dashboard

2. **Sheety API**
   - Create a Google Sheet with columns: date, time, exercise, duration, calories
   - Go to [Sheety](https://sheety.co/) and connect your Google Sheet
   - Copy the endpoint URL and get your AUTH_TOKEN

## Usage

1. **Run the tracker**
   ```bash
   python Working_Tracking_Modified.py
   ```

2. **Enter your workout**
   ```
   Tell me which exercises you did: ? Ran 5km and did 20 pushups
   ```

3. **Check your Google Sheet** - Your workout will be automatically logged!

## Example Output

```json
{
  "exercises": [
    {
      "name": "running",
      "duration_min": 30,
      "nf_calories": 300
    },
    {
      "name": "push-ups",
      "duration_min": 5,
      "nf_calories": 50
    }
  ]
}
```

## File Structure

```
workout-tracker/
├── working_Tracking.py           # Main file without environment variable
├── Working_Tracking_Modified.py  # Main workout tracker with environment variable file 
├── README.md                     # This file
├── .env                          # Environment variables (create this)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

If you have any questions or issues, please open an issue on GitHub or contact the maintainer.
