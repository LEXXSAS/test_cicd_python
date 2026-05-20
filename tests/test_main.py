from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_fullname_success():
    """Тест успешного получения полного имени"""
    response = client.get("/fullname?firstname=Иван&lastname=Петров")

    assert response.status_code == 200
    assert response.json() == {
        "firstname": "Иван",
        "lastname": "Петров",
        "fullname": "Иван Петров"
    }


def test_fullname_empty_firstname():
    """Тест: пустое имя"""
    response = client.get("/fullname?firstname=&lastname=Петров")

    assert response.status_code == 400
    assert response.json()["detail"] == "Имя и фамилия не могут быть пустыми"


def test_fullname_empty_lastname():
    """Тест: пустая фамилия"""
    response = client.get("/fullname?firstname=Иван&lastname=")

    assert response.status_code == 400
    assert response.json()["detail"] == "Имя и фамилия не могут быть пустыми"


def test_fullname_missing_params():
    """Тест: отсутствуют параметры"""
    response = client.get("/fullname")

    assert response.status_code == 422