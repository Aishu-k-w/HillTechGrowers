# Smart Agriculture Web Interface for Hilly Areas

A comprehensive web application for monitoring and controlling smart agriculture systems in hilly regions like Sikkim and Jorethang.

## Features

### 🌱 Dashboard
- **Soil Data Monitoring**: Real-time pH, moisture, temperature, and nutrient levels
- **Weather Tracking**: Temperature, humidity, rainfall, and wind speed data
- **Crop Irrigation**: Schedule management and system status
- **Water Tank Level**: Visual tank level indicator with capacity information
- **Water Flow Control**: Start/stop irrigation system controls
- **Quick Navigation**: Easy access to graphs and alerts

### 📊 Analytics & Graphs
- **Soil Moisture vs Time**: Track moisture levels throughout the day with optimal range indicators
- **Rainfall vs Irrigation Demand**: Compare natural rainfall with irrigation requirements
- **Crop Water Requirements**: Monitor water needs for hill crops (cardamom, ginger, turmeric, maize, potato, cabbage)
- **Summary Statistics**: Key performance indicators and efficiency metrics
- **Agricultural Insights**: Actionable recommendations for hilly cultivation

### 🚨 Alerts & Updates
- **Real-time Notifications**: System alerts categorized by priority and type
- **Filter System**: Filter alerts by category (irrigation, weather, temperature, water, system)
- **Priority Management**: High, medium, and low priority alert classification
- **Search Functionality**: Search through alerts by title, message, or category
- **Status Tracking**: Monitor system health and operational status

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js for data visualization
- **Icons**: Font Awesome
- **Styling**: Custom CSS with responsive design

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd smart-agriculture-app
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

## Default Login Credentials

- **Username**: `admin`
- **Password**: `agriculture2025`

## Project Structure

```
smart-agriculture-app/
├── app.py                 # Flask application main file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── dashboard.html    # Main dashboard
│   ├── graphs.html       # Analytics page
│   └── alerts.html       # Alerts page
└── static/               # Static assets
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        ├── main.js       # Main JavaScript functionality
        ├── charts.js     # Chart configurations
        └── alerts.js     # Alerts page functionality
```

## API Endpoints

- `GET /` - Login page
- `POST /login` - Authentication
- `GET /dashboard` - Main dashboard
- `GET /graphs` - Analytics and trends
- `GET /alerts` - Alerts and notifications
- `GET /logout` - User logout
- `POST /api/water_control` - Water flow control API

## Features for Hilly Agriculture

### Specialized Crop Monitoring
- **Hill Crops**: Cardamom, ginger, turmeric optimized for mountain cultivation
- **Terraced Farming**: Water management for sloped terrain
- **Weather Adaptation**: Monitoring systems adapted for hill climate patterns

### Water Management
- **Efficient Irrigation**: Optimized for water conservation in hilly terrain
- **Rainfall Integration**: Smart irrigation based on natural precipitation
- **Tank Management**: Water storage monitoring for remote locations

### Environmental Monitoring
- **Soil Conditions**: pH and nutrient monitoring for hill soil types
- **Temperature Tracking**: Both soil and air temperature for altitude considerations
- **Humidity Control**: Important for preventing fungal diseases in hill crops

## Customization

### Adding New Crops
Edit the `get_crop_water_data()` function in `app.py` to add new crop types and their water requirements.

### Modifying Alert Categories
Update the alert categories in the `get_alerts_data()` function and corresponding filter tabs in `alerts.html`.

### Changing Chart Types
Modify the Chart.js configurations in `static/js/charts.js` to customize chart appearances and data presentation.

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Mobile Responsive

The application is fully responsive and optimized for:
- Desktop computers
- Tablets
- Mobile phones

## Security Features

- Session-based authentication
- CSRF protection ready
- Input validation
- Secure password handling

## Future Enhancements

- Real-time sensor data integration
- SMS/Email alert notifications
- Weather API integration
- Mobile app companion
- Multi-language support (Hindi, Nepali, etc.)
- Offline mode for remote areas

## Support

For technical support or feature requests, please contact the development team or create an issue in the project repository.

## License

This project is designed for educational and agricultural development purposes in hilly regions.