# DataManagementSvc API Project

## Overview

The `DataManagementSvc` API is a Python-based service that calls the `DataSvc` API, performs data operations, and exposes another API to return the updated data model. The project is built using Flask and Flask-RESTX for creating RESTful endpoints and is hosted locally with Swagger for API documentation.

## Project Structure

```
DataManagementSvc/
│
├── datamanagementsvc/
│   ├── __init__.py           # Initializes the Flask application
│   ├── main.py               # Entry point of the application
│   ├── models.py             # Data model definitions
│   ├── service.py            # Logic for processing data and calling DataSvc API
│
├── env/                      # Python virtual environment directory
│
├── tests/
│   ├── __init__.py           # Initializes the test suite
│   ├── test_api.py           # Unit tests for API endpoints
│
├── .gitignore                # Git ignore file
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── setup.py                  # Project setup configuration
```

## Setup and Installation

### Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/DataManagementSvc.git
cd DataManagementSvc
```

### Step 2: Set Up Virtual Environment

Create and activate a virtual environment to manage project dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Start the Flask application:

```bash
python -m datamanagementsvc.main
```

The API will be available at `http://localhost:5001`, and the Swagger documentation can be accessed at `http://localhost:5001/swagger/`.

## API Endpoints

### GET /updated-data/process

Calls the `DataSvc` API, processes the data, and returns the updated data model as JSON.

- **URL:** `http://localhost:5001/updated-data/process`
- **Method:** `GET`
- **Response:** JSON array containing the processed data.

### Example Response

```json
[
  {
    "H1": "1",
    "H2": "1.1",
    "H3": "2.1",
    "H4": "3.1",
    "H5": "4.1",
    "H6": "Test1",
    "processed_flag": true
  },
  {
    "H1": "2",
    "H2": "1.2",
    "H3": "2.2",
    "H4": "3.2",
    "H5": "4.2",
    "H6": "Test2",
    "processed_flag": true
  }
]
```

## Testing

### Running Tests

Unit tests are located in the `tests` folder. To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Customization

- **Data Processing Logic:** You can modify the data processing logic by updating the code in the `service.py` file.
- **API Routes:** Additional API routes can be added by creating new classes in the `datamanagementsvc.main` file and defining new endpoints.