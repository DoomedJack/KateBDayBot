import requests
import datetime
import time

KateID = 107061378
MineID = 99936297
class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset':offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_audio(self, chat_id, audio):
        params = {'chat_id': chat_id, 'audio': audio}
        method = 'sendAudio'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_photo(self, chat_id, photo):
        params = {'chat_id': chat_id, 'photo': photo}
        method = 'sendPhoto'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

kate_bot = BotHandler('596252103:AAGU3uK7CvxjfRCWrPDrpK5YupKp4XZGUY8')  


def main():  
    new_offset = 135
    moment = 0

    while True:
        kate_bot.get_updates(new_offset)

        last_update = kate_bot.get_last_update()
 
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        
        if last_chat_text.lower() == '/start':
            kate_bot.send_message(last_chat_id, 'Привееееет, Катя!')
            time.sleep(2)
            kate_bot.send_message(last_chat_id, 'Я твой деньрождественский бот: я буду тебя поздравлять, развлекать и направлять, в общем, прикладывать все усилия, чтобы ты не грустила.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Кстати говоря')
            time.sleep(2)
            kate_bot.send_message(last_chat_id, 'Катя, с Днем Рождения тебя!\nПусть все твои твои надежды сбываются, а страхи не оправдываются!\nТы очень, очень крутая! Это я тебе как бот говорю.')
            time.sleep(20)
            kate_bot.send_message(last_chat_id, 'А теперь к квесту. У тебя будет несколько заданий, при выполнении каждого из которых, ты будешь получать кодовую фразу, которую нужно сказать мне, чтобы я понял, что ты справилась.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, '(Только не бей меня, когда увидишь фразы.)')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'А ещееееее')
            time.sleep(2)
            kate_bot.send_message(last_chat_id, 'А еще, есть секретная суперигра. Только никому не говори, потому что она секретная. Так вот.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'При выполнении каждого из обычных заданий ты будешь получать секретный суперслог, из которых по итогам можно будет составить секретный суперпароль.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'И если ты его получишь и отправишь мне, то все. СЧАСТЬЕ ДЛЯ ВСЕХ, ДАРОМ! И еще суперприз для тебя. Насчет счастья, на самом деле, не до конца уверен, но суперприз точно есть.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Ладно, ты как истинный экспериментатор, наверное, уже устала от теории и ждешь-недождешься экшона?')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Все как ты скажешь. Держи экшон.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Для разминки найди следующую штуку по фотке:')
            time.sleep(5)
            kate_bot.send_photo(last_chat_id, 'AgADAgADf6gxG-wtkEnH85JExThh07wDnA4ABFwGbntirnFfwr4CAAEC')
            
        elif last_chat_text.lower() == 'я самая красивая!':
            moment = 1
            kate_bot.send_message(last_chat_id, 'Ииииии это правильный ответ!')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Я тут подумал.')
            time.sleep(2)
            kate_bot.send_message(last_chat_id, 'Ты ведь обидешься, если за весь свой День Рождения ни разу не окажешь в сугробе. Или наоборот? В общем, неважно. Следующая штука ждет тебя на вершине самого большого сугроба на нк.')
            time.sleep(5)

        elif last_chat_text.lower() == 'я самая ловкая!':
            moment = 2
            kate_bot.send_message(last_chat_id, 'Вау! Ты прям снежный барс.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Я понимаю, что у тебя сейчас главный вопрос: "Нахрена мне лопата?". Лопата вообще-то очень полезная штука по жизни.Но дело не в этом, а в том, что она тебе еще сегодня пригодится.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Итак, твой следующий пункт назначения - гк-415. Ты за свою учебу на физтехе не так, чтобы оч много использовала шпоры. Но это очень важны экспириенс, поэтому представь, что у тебя сейчас экзамен в 415 гк, и ты спрятала заранее шпору, самое время ее достать!')
            #time.sleep(600)
            kate_bot.send_message(last_chat_id, 'Хотя, наверное, проще просто нагуглить. Так что тебе стоит сходить в ближайший туалет, левую кабинку))')

        elif last_chat_text.lower() == 'я самая умная!':
            moment = 3
            kate_bot.send_message(last_chat_id, 'отл(10)! Поздравляю!')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'А книжку можешь не читать, если не хочешь. Но она вроде забавная.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Ладно, следующий ход.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Дальше тебе нужно пойти к твоему самому любимому месту. Туда, где ты чувствуешь себя наиболее комфортно и безопасно. Я понимаю, что там, конечно, есть некоторые проблемы с температурой: то жарко, то холодно, но это маленький минус.')
            #time.sleep(300)
            kate_bot.send_message(last_chat_id, 'Уже пришла? Как-то ты быстро, ну, ладно. Посмотри у изголовье под простыней.')


        elif last_chat_text.lower() == 'я самая милая!':
            moment = 4
            kate_bot.send_message(last_chat_id, 'Теперь тебе еще нужно найти подсказку, где находится следующий чекпоинт.')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'И этоооо музыкальный вопрос!!!')
            time.sleep(5)
            kate_bot.send_audio(last_chat_id, 'CQADAgADcgEAAuwtkEkGHERrPnWhGwI')
            #time.sleep(60)
            kate_bot.send_message(last_chat_id, 'Короч, коробочка под кроватью у шкафа, зелененькая такая.')
            time.sleep(1)
            kate_bot.send_photo(last_chat_id, 'AgADAgADD6kxG8x-kEnKKzv9Tk43LJb6Mg4ABD0YKa5joOycFHIFAAEC')
            #time.sleep(500)
            kate_bot.send_message(last_chat_id, 'На пазле изображено место, куда тебе идти')
            time.sleep(5)
            
        elif last_chat_text.lower() == 'Я самая дерзкая!':
            moment = 5
            kate_bot.send_message(last_chat_id, 'Урааааааааааааааааааааа!!!!')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Ты победила!!')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Успех')
            time.sleep(5)
            kate_bot.send_message(last_chat_id, 'Осталось получить суперприз!')
            time.sleep(5)
        
        elif last_chat_text.lower() == 'толя любит катю.':
            kate_bot.send_message(last_chat_id, 'Хочется суперприз? Ну, что ж, лови инструкцию:')
            kate_bot.send_photo(last_chat_id, 'AgADAgADF6kxG8x-kElZEygDv1LPQAYDMw4ABGXVQ-Y8vzGgbmoFAAEC')
            time.sleep(10)
            kate_bot.send_photo(last_chat_id, 'AgADAgADGKkxG8x-kEnOBW4vYeU4r5waMw4ABAaUQjrJ6_0Dc2kFAAEC')
            time.sleep(10)
            kate_bot.send_photo(last_chat_id, 'AgADAgADGqkxG8x-kEm01rDuMM1niqkCnA4ABN1annqThZ_9vsgCAAEC')
            time.sleep(10)
            kate_bot.send_photo(last_chat_id, 'AgADAgADEqkxG8x-kEkzgAtS7IX42U2dmg4ABOmmlwoUauEWoscCAAEC')
            time.sleep(10)
            kate_bot.send_photo(last_chat_id, 'AgADAgADE6kxG8x-kEnSWnPfc6v2BO-jmg4ABJ2WWTsmvWiKoswCAAEC')
            time.sleep(10)
            kate_bot.send_photo(last_chat_id, 'AgADAgADFKkxG8x-kElIGYkK3sEKKxjERg4ABEFIcv9yduteuW0AAgI')
            time.sleep(10)
            kate_bot.send_photo(last_chat_id, 'AgADAgADFakxG8x-kEkQkIEUqhi-jr0CnA4ABE4Fupt23bQYxcYCAAEC')
            time.sleep(10)
            kate_bot.send_photo(last_chat_id, 'AgADAgADFqkxG8x-kEm41vD93hvDs1f5Mg4ABBBQQefvx_8oeW4FAAEC')
            time.sleep(10)


        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()