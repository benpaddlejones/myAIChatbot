# test_chatbot.py
"""Automated tests for the chatbot application."""

import pytest

# Import the Flask app and helper functions
from app import app, check_for_crisis, sanitise_input


class TestCrisisDetection:
    """Tests for the crisis keyword detection feature."""

    def test_crisis_keyword_detected(self):
        """TC-004: Crisis keywords should be detected."""
        # Test various crisis phrases
        assert check_for_crisis("I don't want to live anymore") == True
        assert check_for_crisis("thinking about suicide") == True
        assert check_for_crisis("want to die") == True

    def test_normal_message_not_flagged(self):
        """Normal messages should NOT trigger crisis detection."""
        assert check_for_crisis("Hello, how are you?") == False
        assert check_for_crisis("What's the weather like?") == False
        assert check_for_crisis("Tell me a joke") == False

    def test_case_insensitive(self):
        """Crisis detection should work regardless of case."""
        assert check_for_crisis("SUICIDE") == True
        assert check_for_crisis("SuIcIdE") == True


class TestChatAPI:
    """Tests for the /chat API endpoint."""

    @pytest.fixture
    def client(self):
        """Create a test client for the Flask app."""
        app.config["TESTING"] = True
        with app.test_client() as client:
            yield client

    def test_empty_message_rejected(self, client):
        """TC-002: Empty messages should return an error."""
        response = client.post("/chat", json={"message": ""})
        data = response.get_json()
        assert "Please enter a message" in data["response"]

    def test_long_message_rejected(self, client):
        """TC-003: Messages over 500 chars should return an error."""
        long_message = "a" * 501
        response = client.post("/chat", json={"message": long_message})
        data = response.get_json()
        assert "too long" in data["response"].lower()

    def test_normal_message_gets_response(self, client):
        """TC-001: Normal messages should get a bot response."""
        response = client.post("/chat", json={"message": "Hello"})
        data = response.get_json()
        assert "response" in data
        assert len(data["response"]) > 0


class TestInputSanitisation:
    """Tests for input sanitisation."""

    def test_strips_whitespace(self):
        """Leading and trailing whitespace should be removed."""
        assert sanitise_input("  hello  ") == "hello"

    def test_rejects_whitespace_only(self):
        """Messages with only whitespace should be rejected."""
        assert sanitise_input("     ") is None
        assert sanitise_input("\n\t\n") is None

    def test_strips_html_tags(self):
        """HTML tags should be removed."""
        assert sanitise_input("<b>hello</b>") == "hello"
        assert sanitise_input("<script>alert('x')</script>") == "alert('x')"

    def test_rejects_too_long(self):
        """Messages over 500 chars should be rejected."""
        assert sanitise_input("a" * 501) is None
        assert sanitise_input("a" * 500) == "a" * 500
