from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_endpoint_returns_status_payload() -> None:
    response = client.get("/")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "running"
    assert payload["app"] == "instagram-assistant"


def test_v1_health_endpoint_returns_expected_payload() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["database"] in {"connected", "unavailable"}
    assert payload["version"]


def test_placeholder_resource_endpoints_exist() -> None:
    for path in ["/api/v1/users", "/api/v1/automations", "/api/v1/messages", "/api/v1/analytics"]:
        response = client.get(path)
        assert response.status_code == 200
