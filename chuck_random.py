import requests


class TestNewJoke():
    """Создание новой шутки"""

    def __int__(self):
        pass

    # def test_create_new_random_joke(self):
    #     """Создание случайной шутки"""
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print("Статус код :" + str(result.status_code))
    #     assert 200 == result.status_code
    #     if result.status_code == 200:
    #         print("Успешно!!! Мы получили новую шутку!")
    #     else:
    #         print("Провал!!! Запрос ошибочный")
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #     check = result.json()
    #     # check_info = check.get("categories")
    #     # print(check_info)
    #     # print(result.json().get())
    #     # assert check_info == []
    #     # print("Категория верна")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("Chuck  присутствует")
    #     else:
    #         print("Chuck  отсутствует")

    def test_create_new_random_categories_joke(self):
        """Создание случайной шутки на определенную тему"""
        category = "sport"
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        print(url)
        result = requests.get(url)
        print("Статус код :" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы получили новую шутку!")
        else:
            print("Провал!!! Запрос ошибочный")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        print(result.json().get("categories"))
        assert check_info == ["sport"]
        print("Категория верна")
        assert check_info == [category]
        print("Категория верна")
        check_info_value = check.get("value")
        print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck  присутствует")
        # else:
        #     print("Chuck  отсутствует")


# random_joke = TestNewJoke()
# random_joke.test_create_new_random_joke()
sport_joke = TestNewJoke()
sport_joke.test_create_new_random_categories_joke()
