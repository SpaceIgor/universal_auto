import os

DEVELOPER_CHAT_ID = int(os.environ.get('DEVELOPER_CHAT_ID', '803129892'))

share_phone_text = "Будь ласка розшарьте номер телефону для роботи з нашим ботом"
user_greetings_text = "Тебе вітає Ninja Taxi"
help_text = "Для першого кроку зробіть реєстрацію або авторизуйтеся командою /start"

main_buttons = (
    "\U0001f696 Викликати Таксі",
    "\U0001f4e2 Залишити відгук",
    "\U0001F4E8 Залишити заявку на роботу",
    "\U0001f4f2 Надати номер телефону",
    "\U0001F4B0 Розпочати роботу",
    "\u270A Завершити роботу"
)