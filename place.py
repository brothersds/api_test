import requests


class TestNewLocation():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"    # базовая URL
        key = "?key=qaclick123"                        # параметр для всех запросов

        """Создание новой локации"""
        post_resourse = "/maps/api/place/add/json"      # ресурс метода POST

        post_url = base_url + post_resourse + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone number": "(+91) 983 893 3937",
            "adress": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)

        print("Статус код :" + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!!! Создана новая локация")
        else:
            print("Провал!!! Запрос ошибочный")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f'Статус код ответа: {check_info_post}')
        assert check_info_post == "OK"
        print("Статус ответа верен")
        place_id = check_post.get("place_id")
        print(f'place_id: {place_id}')

        """Проверка создания новой локации"""
        get_resourse = "/maps/api/place/get/json"      # ресурс метода GET



new_place = TestNewLocation()
new_place.test_create_new_location()
