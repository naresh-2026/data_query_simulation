Mini Data Query Simulation Engine

Overview
This project is a lightweight backend service that simulates a simplified version of a Gen AI-powered data query system. It provides an API to process natural language queries, convert them into pseudo-SQL, and return mock responses.

Features
- Natural Language Query Processing: Accepts queries like "What are the total sales?"
- Query Explanation: Provides a breakdown of how the system interprets the query.
- Validation: Checks if a query is feasible.
- Mock Database: Uses SQLite for storing example transactions and user data.
- Authentication: Requires an API key for secure access.

Tech Stack
- Backend: FastAPI (Python)
- Database: SQLite (In-Memory or File-Based)
- Authentication: Simple API Key Authentication
- Deployment: Render/Heroku/Railway (Optional)

Installation

Prerequisites
Ensure you have Python 3.8+ installed.

Clone the Repository
```sh
git clone https://github.com/naresh-2026/mini-query-engine.git
cd mini-query-engine
```

Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

Install Dependencies
```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Running the Application
Start the FastAPI server using Uvicorn:
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| POST | /query   | Converts a natural language query to pseudo-SQL and returns mock results. |
| POST | /explain | Explains how a query is interpreted. |
| POST | /validate | Checks if the query is valid. |

Example Request (Using cURL)
```sh
curl -X POST "http://127.0.0.1:8000/query" \
     -H "Content-Type: application/json" \
     -H "api-key: mysecurekey123" \
     -d '{"query": "What are the total sales?"}'
```

Example Response
```json
{
    "pseudo_sql": "SELECT SUM(sales) FROM transactions;",
    "result": 150000
}
```

Authentication
The API requires an API key for requests. Add `api-key` in the request header.
- Default API Key: `mysecurekey123`

Running Tests
To run tests (if applicable):
```sh
pytest tests/
```

Deployment (Optional)
To deploy on Render/Heroku/Railway, configure `Procfile` and use:
```sh
git push heroku main  # For Heroku deployment
```


