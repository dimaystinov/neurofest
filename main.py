import argparse
import requests


def synthesize(folder_id, iam_token, text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Bearer ' + iam_token,
    }

    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'alena',
        'folderId': folder_id
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument("--token", required=True, help="IAM token")
    #parser.add_argument("--folder_id", required=True, help="Folder id")
    #parser.add_argument("--text", required=True, help="Text for synthesize")
    #parser.add_argument("--output", required=True, help="Output file name")
    args = parser.parse_args()

    token = "t1.9euelZqOj5rLkZeLmYqMksjMj5Sblu3rnpWanMfHm5HIjpOZic6Zi8iTl47l9Pc5I2Nr-e9tdUX23fT3eVFga_nvbXVF9g.iIIIcjn0ZkHdUbkFosV7L5ocWQ4KNMQFJawnItXwn223CO1leEhTS2Ol3y4_-IwPj5mVYwcyjIOPtamUH_1rCg"
    text = """Внимание! Внимание! Паспорт без обложки, ручка, пакеты только прозрачные. Телефоны и вещи оставляем сопровождающим.  Район, а точнее школа номер 9, привествует новых гостей. 
    Для прохождения промежуточного пункта досмотра нужны паспорт без обложки, ручка и минимальный интеллект. 
    Со щитом или на щите. Пуля — дура, штык — молодец. Физфак МГУ топчик
    """

    text1 = "Внимание! Внимание! Паспорт без обложки, ручка, пакеты только прозрачные. Телефоны и вещи оставляем сопровождающим."

    text3 = "Район номер 9, а точнее школа номер 9 прощается с гостями. И И школы 9 интересуется Как прошёл экзамен? Приходите к нам ещё. МФТИ и физфак МГУ топчик. только физика соль, остальное всё ноль, а филолог и химик дубина. Дотвидания"
    text4 = "Каникулы! Каникулы! Я ничего не придумал. Пингвины на каникулы пошли и банан педро нашли. Чтобы все не забыли за лето. Я не знаю что говорить. Я люблю физику. Счатья и здоровья. Мы молоко попили манчестер сити победили. " \
            "Лето это прекрасное время чтобы выучить физику 7 го класса. Ссылка в описании. Вывод: ждите. Ждите новых переменных в уравнении. Чтоб оценки были хорошими надо хорошо хорошо заниматься. МФТИ и физфак МГУ топчик. Только физика соль, остальное всё ноль" \
            "а филолог и химик дубина. Азаза. ВСем хороших и каникул и помните, что каждую пятницу будет созвон в зуме на 1.5 часа. Дотвидания и хорошего дня лол "
    folder_id = "b1g3v4itpbs0sqqpqklv"
    # curl -d "{\"yandexPassportOauthToken\":\"AQAAAAAQKQPzAATuwVJpZHxwKE0TqjKNdgaFMRs\"}" "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    output = "test"
    with open(output, "wb") as f:
        for audio_content in synthesize(folder_id, token, text4):  # args.folder_id, args.token, args.text
            f.write(audio_content)