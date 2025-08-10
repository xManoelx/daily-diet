# Daily Diet API

A comprehensive RESTful API built with Flask for tracking daily meals and diet management. This application allows users to register meals, monitor their diet compliance, and get detailed statistics about their eating habits.

## 🚀 Features

- **Meal Management**: Complete CRUD operations for meal tracking
- **Diet Monitoring**: Track whether meals are within diet guidelines
- **Statistics Dashboard**: Comprehensive diet statistics including streaks and percentages
- **User Management**: Multi-user support with individual meal tracking
- **Health Check**: API status monitoring endpoint
- **Database Reset**: Administrative functionality for data cleanup
- **Data Validation**: Robust input validation for all endpoints
- **Error Handling**: Comprehensive error responses with detailed messages

## 🛠️ Tech Stack

- **Framework**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Architecture**: Service-oriented architecture with separation of concerns
- **Data Models**: User and Meal entities with proper relationships
- **Validation**: Custom validation utilities
- **Language**: Python 3.x

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher installed
- pip (Python package installer)
- Basic understanding of REST APIs
- SQLite (included with Python)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd daily-diet-api
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Set environment variables** (optional)
   ```bash
   export DATABASE_URL=sqlite:///daily_diet.db
   export SECRET_KEY=your-secret-key
   ```

## 🚦 Running the Application

1. **Start the development server**
   ```bash
   python app.py
   ```

2. **Access the API**
   - The API will be available at `http://localhost:5000`
   - Health check: `http://localhost:5000/health`

## 📚 API Documentation

### Health & Utility Endpoints

#### GET /health
Check if the API is running and operational.

**Response:**
```json
{
  "status": "OK",
  "message": "Daily Diet API is running!",
  "version": "1.0.0"
}
```

#### POST /api/reset
Reset all meals in the database (administrative function).

**Response:**
- **200 OK**: Database reset successfully
- **500 Internal Server Error**: Reset failed

### Meal Management Endpoints

#### POST /api/meals
Register a new meal.

**Request Body:**
```json
{
  "name": "Breakfast",
  "description": "Healthy breakfast with fruits",
  "date_time": "2025-08-10T08:00:00Z",
  "is_on_diet": true
}
```

**Response:**
- **201 Created**: Meal created successfully
- **400 Bad Request**: Validation errors
- **500 Internal Server Error**: Server error

#### GET /api/meals
List all meals for the user, ordered by date (newest first).

**Response:**
```json
{
  "meals": [
    {
      "id": "meal-uuid",
      "name": "Breakfast",
      "description": "Healthy breakfast",
      "date_time": "2025-08-10T08:00:00Z",
      "is_on_diet": true,
      "created_at": "2025-08-10T08:00:00Z",
      "updated_at": "2025-08-10T08:00:00Z"
    }
  ],
  "total": 1
}
```

#### GET /api/meals/{meal_id}
Get details of a specific meal.

**Parameters:**
- `meal_id`: Unique meal identifier

**Response:**
- **200 OK**: Meal details returned
- **404 Not Found**: Meal not found

#### PUT /api/meals/{meal_id}
Update an existing meal.

**Parameters:**
- `meal_id`: Unique meal identifier

**Request Body:** (partial updates supported)
```json
{
  "name": "Updated meal name",
  "is_on_diet": false
}
```

**Response:**
- **200 OK**: Meal updated successfully
- **404 Not Found**: Meal not found
- **400 Bad Request**: Invalid data

#### DELETE /api/meals/{meal_id}
Delete a meal.

**Parameters:**
- `meal_id`: Unique meal identifier

**Response:**
- **200 OK**: Meal deleted successfully
- **404 Not Found**: Meal not found

#### GET /api/meals/stats
Get comprehensive diet statistics for the user.

**Response:**
```json
{
  "stats": {
    "total_meals": 10,
    "meals_on_diet": 7,
    "meals_off_diet": 3,
    "diet_percentage": 70.0,
    "best_diet_streak": 5,
    "current_streak": 2
  }
}
```

### User Management Endpoints

#### GET /api/users
List all registered users.

**Response:**
```json
{
  "users": [
    {
      "id": "user-1",
      "name": "Test User",
      "email": "test@dailydiet.com",
      "created_at": "2025-08-10T08:00:00Z",
      "total_meals": 5
    }
  ]
}
```

#### GET /api/users/{user_id}
Get details of a specific user.

**Parameters:**
- `user_id`: Unique user identifier

**Response:**
- **200 OK**: User details returned
- **404 Not Found**: User not found

#### POST /api/users
Create a new user account.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Response:**
- **201 Created**: User created successfully
- **400 Bad Request**: Validation errors

## 🏗️ Project Structure

```
daily-diet-api/
├── app.py              # Main application file with routes
├── database.py         # Database configuration and initialization
├── models.py           # Data models (User, Meal)
├── services.py         # Business logic services
├── utilities.py        # Validation utilities
└── daily_diet.db       # SQLite database file (auto-generated)
```

## 🎯 Key Features Explained

### Diet Tracking
- Track whether each meal follows diet guidelines
- Calculate diet compliance percentage
- Monitor current and best diet streaks

### Statistics Engine
- **Total Meals**: Count of all registered meals
- **Diet Compliance**: Percentage of meals that follow diet
- **Streak Tracking**: Current and best consecutive diet-compliant meals
- **Diet Distribution**: Breakdown of on-diet vs off-diet meals

### Data Models

#### User Model
- Unique ID (UUID)
- Name and email
- Creation timestamp
- One-to-many relationship with meals

#### Meal Model
- Unique ID (UUID)
- Name and optional description
- Date and time of meal
- Diet compliance flag
- User association
- Creation and update timestamps

## 🔒 Data Validation

The API includes comprehensive validation:

### Meal Validation
- Name is required
- Date/time must be in valid ISO format
- Diet compliance flag must be boolean
- Description is optional

### User Validation
- Name is required
- Email is required and must be unique
- Proper email format validation

## 🧪 Testing the API

### Using curl

```bash
# Health check
curl http://localhost:5000/health

# Create a user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Test User", "email": "test@example.com"}'

# Create a meal
curl -X POST http://localhost:5000/api/meals \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Breakfast",
    "description": "Healthy breakfast",
    "date_time": "2025-08-10T08:00:00Z",
    "is_on_diet": true
  }'

# Get statistics
curl http://localhost:5000/api/meals/stats

# List all meals
curl http://localhost:5000/api/meals
```

### Using Python requests

```python
import requests
import json

# Base URL
base_url = "http://localhost:5000"

# Create a meal
meal_data = {
    "name": "Lunch",
    "description": "Grilled chicken with vegetables",
    "date_time": "2025-08-10T12:00:00Z",
    "is_on_diet": True
}

response = requests.post(f"{base_url}/api/meals", json=meal_data)
print(response.json())

# Get statistics
stats = requests.get(f"{base_url}/api/meals/stats")
print(stats.json())
```

## 📊 Example Usage Scenarios

### Daily Meal Tracking
1. Register breakfast, lunch, dinner, and snacks
2. Mark each meal as on-diet or off-diet
3. View daily, weekly, or monthly statistics
4. Track progress over time

### Diet Analysis
1. Monitor diet compliance percentage
2. Identify patterns in eating habits
3. Track improvement in diet consistency
4. Set goals based on streak data

## ⚙️ Configuration

### Environment Variables
- `DATABASE_URL`: Database connection string (default: SQLite)
- `SECRET_KEY`: Flask secret key for security

### Database Configuration
- Automatic table creation on startup
- Default user creation for testing
- Support for multiple database backends via SQLAlchemy

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] Meal categories and tags
- [ ] Photo upload for meals
- [ ] Nutritional information tracking
- [ ] Goal setting and achievement system
- [ ] Data export functionality
- [ ] Mobile app integration
- [ ] Notification system for meal reminders
- [ ] Advanced analytics and reports
- [ ] Integration with fitness trackers
