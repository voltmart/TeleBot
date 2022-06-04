import telebot
import random
from telebot import types

# ��������� ������ ���������� ������
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# ��������� ������ ���������
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
# ������� ����
bot = telebot.TeleBot("5282240819:AAGP9OzrqaFlrvizpacEbfiUUYDznxxLktw")
# ������� start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # ��������� ��� ������
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("����")
        item2=types.KeyboardButton("���������")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, '�����: \n���� ��� ��������� ����������� �����\n��������� � ��� ��������� ������ ������ ',  reply_markup=markup)
# ��������� ��������� �� �����
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # ���� ���� ������� 1, ������ ��� ��������� ����
    if message.text.strip() == '����' :
            answer = random.choice(facts)
    # ���� ���� ������� 2, ������ ����� �����
    elif message.text.strip() == '���������':
            answer = random.choice(thinks)
    # �������� ����� ��������� � ��� ���
    bot.send_message(message.chat.id, answer)
# ��������� ����
bot.polling(none_stop=True, interval=0)