import requests

from lesson1.api_tests.services.case.pom import create_case
from lesson1.api_tests.services.case.data import create_case_dict
from lesson1.api_tests.services.case.models import Case
from lesson1.api_tests.services.case.data import create_case_dict
from lesson1.api_tests.utils.api_client import client

base_url: str = "http://localhost:8000"

def test_read_root1():
    response=requests.get(f"{base_url}/")
    assert response.status_code==200
    assert response.json() == {'Hello': 'World'}


def test_read_root():
    response = client.make_request(handle="/", method="GET")
    response.status_code_should_be_eq(200)
    response.json_should_be_eq({"Hello": "World"})


def test_create_case1():
    data = {
        "id": 3,
        "name": "test",
        "description": "Тестовое задание",
        "priority": "высокий",
        "steps": ["шаг 1", "шаг 2", "шаг 3"],
        "expected_result": "Задание выполнено",
    }
    response = requests.post(f"{base_url}/testcases/", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "name": "test",
        "description": "Тестовое задание",
        "priority": "высокий",
        "steps": ["шаг 1", "шаг 2", "шаг 3"],
        "expected_result": "Задание выполнено",
    }


def test_create_case():
    # or using model
    # response = create_case(Case(**create_case_dict).model_dump())
    response = create_case(json=create_case_dict)
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(create_case_dict)
    # Also we can check schema
    # response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())


def test_delete_case():
    data = {
        "id": 4,
        "name": "test",
        "description": "Тестовое задание",
        "priority": "высокий",
        "steps": ["шаг 1", "шаг 2", "шаг 3"],
        "expected_result": "Задание выполнено",
    }
    response = requests.post(f"{base_url}/testcases/", json=data)
    case_id = response.json()["id"]
    response1 = requests.delete(f"{base_url}/testcases/{case_id}")
    assert response1.status_code==200
    assert  response1.json()=={"detail":"Test case deleted."}


def test1_create_case():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 113,
            "name": "Tester",
            "description": "Description #1",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3", "Шаг 4"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        },
    )
    response.status_code_should_be_eq(200)
    response.json_should_contains({"id": 3})

