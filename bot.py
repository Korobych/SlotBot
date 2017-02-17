import config
import telebot
from telebot import types
import time
import slot_machine


bot = telebot.TeleBot(config.alternative_token)
markup_casino = types.ReplyKeyboardMarkup(row_width=2)
markup_casino.row('Потянуть рычаг! 💰', 'Изменить ставку')
markup_casino.row('Выйти из казино', 'Правила игры 📝')
markup_default = types.ReplyKeyboardMarkup(row_width=2)
markup_default.row('Пойти в казино', 'Пойти в ...')
markup_default.row('Инвентарь', 'еще?')


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id, "Приветствую тебя, путник!", reply_markup=markup_default)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text == "Пойти в казино":
        bot.send_message(message.chat.id, "Добро пожаловать в казино! Не забудь выбрать ставку! (изначальная 20 $)\n"
                         + "Твой текущий счёт " + str(slot_machine.credit) + " $!\n" +
                         "Самое время начать игру! -> Тяни рычаг!", reply_markup=markup_casino)
    elif message.text == "Потянуть рычаг! 💰":
        if slot_machine.cash >= slot_machine.credit:
            bot.send_message(message.chat.id, "Ставка слишком высока!\nПонизь ставку, что бы продолжать игру.",
                             reply_markup=markup_casino)
        elif slot_machine.credit >= 15 and slot_machine.credit - slot_machine.cash > 0:
            bot.send_message(message.chat.id, "Твоя ставка " + str(slot_machine.cash) + " $!\n" +
                             slot_machine.play_game() + "\n"
                             + "Твой текущий счёт " + str(slot_machine.credit) + " $\n"
                             , reply_markup=markup_casino)
            if slot_machine.flag:
                bot.send_message(message.chat.id, "Поздравляю, ты выиграл " + str(slot_machine.total_won) + " $!",
                                 reply_markup=markup_casino)
        else:
            bot.send_message(message.chat.id, "Недостаточно средств для продолжения игры.\n" +
                                              "Увы, путник, на этом твоя игра закончена. Заходи в следующий раз!",
                             reply_markup=markup_casino)
    elif message.text == "Изменить ставку":
        bot.send_message(message.chat.id, "Введи новую ставку (не меньше чем 15)!", reply_markup=markup_casino)
    elif message.text == "Правила игры 📝":
        bot.send_message(message.chat.id, "Приветствую тебя, игрок! Игра очень проста, каждый игровой ход проходит"
                                          " за 4 этапа:\n"
                         + "1) Нажатие на кнопку Потянуть рычаг! 💰 запускает автомат.\n Списывается ставка, отображается"
                         + " игровое поле 3x3 и по счастливой случайности (честный рандом) деньги либо проигрываются"
                         + " либо преумножаются.\n2) Если игрок хочет изменить ставку, то нужно всего лишь нажать "
                         + "на кнопку Изменить ставку или набрать нужное число в месте для набора сообщений.\n" +
                "3) Победными являются ряды из 3 одниковых элементов расположенных:\nпо горизонтали\n 🍒🍒 🍒\n"
                        +"по вертикали\n🍏\n🍏\n🍏\nпо диагонали\n7️⃣\n    7️⃣\n         7️⃣\n"
                         + "4) Выигрыш расчитывается из расчёта ставка * коэффициент категории:\n" +
                         " 7️⃣ - 5, 🍒 - 3, 🍏 - 1.5, 🔔- 1\nЕсли ставка превышает количество имеющихся средств,"
                         + " соотвествующее уведомление будет отображено на экране диалога.\n Удачной игры!",
                         reply_markup=markup_casino)
    elif message.text == "Выйти из казино":
        bot.send_message(message.chat.id, "Еще увидимся, путник!\nНо куда мне теперь идти?",
                         reply_markup=markup_default)
    elif int(message.text) % 1 == 0 and int(message.text) >= 15:
        if int(message.text) < slot_machine.credit:
            slot_machine.cash = int(message.text)
            bot.send_message(message.chat.id, "Новая ставка " + message.text + "$ принята!", reply_markup=markup_casino)
        else:
            bot.send_message(message.chat.id, "Ставка не принимается. Недостаточно средств: " +
                             str(slot_machine.credit), reply_markup=markup_casino)
    else:
        bot.send_message(message.chat.id, "Путник, видимо, ты из совсем далёких краёв. Я ничего не понял.",
                         reply_markup=markup_casino)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)

