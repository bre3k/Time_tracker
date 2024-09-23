import sys 
import os

# Ensure the utils module can be found by adding the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import datetime
from utils import calculate_session_duration, format_duration
from models import setup_database, User, Activity, Session

@pytest.fixture
def db_session():
    # Create an in-memory SQLite database session for testing
    session = setup_database()
    return session

# Test for calculate_session_duration function
def test_calculate_session_duration():
    start_time = datetime(2024, 9, 1, 12, 0, 0)
    end_time = datetime(2024, 9, 1, 14, 0, 0)
    duration = calculate_session_duration(start_time, end_time)
    assert duration == 7200  # 2 hours in seconds

# Test for format_duration function
def test_format_duration():
    formatted_duration = format_duration(7200)
    assert formatted_duration == "2h 0m 0s"


