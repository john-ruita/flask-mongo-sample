from server import app

def test_get_questions():
    with app.test_client() as client:
        response = client.get("/api/questions")
        assert response.status_code == 200
        assert response.json["message"] == "Questions retrieved"
        assert "data" in response.json
        assert "page" in response.json
        assert "total" in response.json
