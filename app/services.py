import re

def process_query(query: str):
    """Convert natural language query to pseudo-SQL and return a mock response."""
    
    query = query.lower()

    if "total sales" in query:
        return {
            "pseudo_sql": "SELECT SUM(sales) FROM transactions;",
            "result": 150000
        }
    elif "users signed up" in query:
        return {
            "pseudo_sql": "SELECT COUNT(*) FROM users WHERE signup_date >= DATE('now', '-7 days');",
            "result": 245
        }
    else:
        return {"error": "Query not supported. Try a different question."}

def explain_query(query: str):
    """Explain how the query is interpreted."""
    
    if "total sales" in query:
        return {
            "explanation": "Summing up sales transactions.",
            "pseudo_sql": "SELECT SUM(sales) FROM transactions;"
        }
    elif "users signed up" in query:
        return {
            "explanation": "Counting new users in the last 7 days.",
            "pseudo_sql": "SELECT COUNT(*) FROM users WHERE signup_date >= DATE('now', '-7 days');"
        }
    else:
        return {"error": "Cannot explain query."}

def validate_query(query: str):
    """Validate query structure."""
    
    if len(query) < 5:
        return {"valid": False, "error": "Query is too short."}
    if not re.search(r"\b(sales|users|revenue|transactions)\b", query.lower()):
        return {"valid": False, "error": "Query lacks a valid keyword."}
    
    return {"valid": True}
