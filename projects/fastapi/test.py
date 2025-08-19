import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

from main import app, send_email

client = TestClient(app)

@pytest.mark.asyncio
async def test_send_notification():
    with patch("main.send_mail", new=AsyncMock()) as mocked_email:
        response = client.post(
            "/send-notification",
            json={"email": "test@example.com", "message": "Test notification"}
        )

        assert response.status_code == 200
