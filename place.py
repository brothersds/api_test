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
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
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
        get_url = f'{base_url}{get_resourse}{key}&place_id={place_id}'
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код :" + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!! Проверка создания новой локации прошла успешно")
        else:
            print("Провал!!! Запрос ошибочный")

        """Изменение новой локации"""
        put_resourse = "/maps/api/place/update/json"  # ресурс метода PUT
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": f'{place_id}',
            "address": "100 Lenina street, RU",
            "key": key.partition("=")[2]
        }


new_place = TestNewLocation()
new_place.test_create_new_location()
