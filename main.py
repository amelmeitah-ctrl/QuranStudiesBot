import os
import telebot
from telebot import types
from datetime import datetime
from hijridate import Gregorian

# ط¥ط¹ط¯ط§ط¯ ط§ظ„ط¨ظˆطھ ط¨ط§ط³طھط®ط¯ط§ظ… ط§ظ„ظ…ظپطھط§ط­ ط§ظ„ط³ط±ظٹ ط§ظ„ظ…ط¨ط±ظ…ط¬ ظپظٹ ظ„ظˆط­ط© ط§ظ„ط£ط³ط±ط§ط±
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')
bot = telebot.TeleBot(BOT_TOKEN)

def notify_admin(text: str):
    """Send a message to the admin's chat. Silently fails if not configured."""
    if not ADMIN_CHAT_ID:
        return
    try:
        bot.send_message(ADMIN_CHAT_ID, text, parse_mode="Markdown")
    except Exception as e:
        print(f"[notify_admin] failed: {e}")

# ط§ظ„ظ‡ظٹظƒظ„ ط§ظ„ط£ط³ط§ط³ظٹ ط§ظ„ظ…طھظˆط§ظپظ‚ ظ…ط¹ ط¨ظٹط§ظ†ط§طھ ط§ظ„ط£ط²ط±ط§ط± ظˆط§ظ„طھط­ظƒظ… ظˆط§ظ„طھط¹ظ„ظٹظ…
list_data = {
    "admin_id": None,
    "readers": [],
    "listeners": [],
    "is_open": True
}

def get_current_date_text():
    days_ar = ["ط§ظ„ط£ط­ط¯", "ط§ظ„ط¥ط«ظ†ظٹظ†", "ط§ظ„ط«ظ„ط§ط«ط§ط،", "ط§ظ„ط£ط±ط¨ط¹ط§ط،", "ط§ظ„ط®ظ…ظٹط³", "ط§ظ„ط¬ظ…ط¹ط©", "ط§ظ„ط³ط¨طھ"]
    months_ar_greg = ["ظٹظ†ط§ظٹط±", "ظپط¨ط±ط§ظٹط±", "ظ…ط§ط±ط³", "ط£ط¨ط±ظٹظ„", "ظ…ط§ظٹظˆ", "ظٹظˆظ†ظٹظˆ",
                      "ظٹظˆظ„ظٹظˆ", "ط£ط؛ط³ط·ط³", "ط³ط¨طھظ…ط¨ط±", "ط£ظƒطھظˆط¨ط±", "ظ†ظˆظپظ…ط¨ط±", "ط¯ظٹط³ظ…ط¨ط±"]
    months_ar_hijri = ["ظ…ط­ط±ظ…", "طµظپط±", "ط±ط¨ظٹط¹ ط§ظ„ط£ظˆظ„", "ط±ط¨ظٹط¹ ط§ظ„ط¢ط®ط±",
                       "ط¬ظ…ط§ط¯ظ‰ ط§ظ„ط£ظˆظ„ظ‰", "ط¬ظ…ط§ط¯ظ‰ ط§ظ„ط¢ط®ط±ط©", "ط±ط¬ط¨", "ط´ط¹ط¨ط§ظ†",
                       "ط±ظ…ط¶ط§ظ†", "ط´ظˆط§ظ„", "ط°ظˆ ط§ظ„ظ‚ط¹ط¯ط©", "ط°ظˆ ط§ظ„ط­ط¬ط©"]

    now = datetime.now()
    day_name = days_ar[(now.weekday() + 1) % 7]
    greg_str = f"{now.day} {months_ar_greg[now.month - 1]} {now.year} ظ…"

    hijri = Gregorian(now.year, now.month, now.day).to_hijri()
    hijri_str = f"{hijri.day} {months_ar_hijri[hijri.month - 1]} {hijri.year} ظ‡ظ€"

    return f"ًں“… {day_name} {greg_str} | {hijri_str}"

def generate_list_text():
    status_em = "ًں”“ ظ…ظپطھظˆط­ط© ط§ظ„ط¢ظ†" if list_data["is_open"] else "ًں”’ ظ…ط؛ظ„ظ‚ط© ط§ظ„ط¢ظ†"
    
    text = f"ًں•Œ *ط£ظƒط§ط¯ظٹظ…ظٹط© ط¹ظ„ظˆظ… ط§ظ„ظ‚ط±ط¢ظ† ظˆط§ظ„ط³ظ†ط©* ًں•Œ\n"
    text += f"âœ¨â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬âœ¨\n"
    text += f"{get_current_date_text()}\n"
    text += f"âœ¨â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬âœ¨\n\n"
    text += f"ط§ظ„ط³ظ„ط§ظ… ط¹ظ„ظٹظƒظ… ظˆط±ط­ظ…ط© ط§ظ„ظ„ظ‡ ظˆط¨ط±ظƒط§طھظ‡ ًںŒ¸\n\n"
    text += f"ط­ط§ظ„ط© ط§ظ„ظ‚ط§ط¦ظ…ط©: {status_em}\n\n"
    text += f"ًں“– *ظ‚ط§ظ„ ط±ط³ظˆظ„ ط§ظ„ظ„ظ‡ ï·؛:*\n"
    text += f"آ« *ط§ظ‚ظ’ط±ظژط،ظڈظˆط§ ط§ظ„ظ’ظ‚ظڈط±ظ’ط¢ظ†ظژ ظپظژط¥ظگظ†ظژظ‘ظ‡ظڈ ظٹظژط£ظ’طھظگظٹ ظٹظژظˆظ’ظ…ظژ ط§ظ„ظ’ظ‚ظگظٹظژط§ظ…ظژط©ظگ ط´ظژظپظگظٹط¹ظ‹ط§ ظ„ظگط£ظژطµظ’ط­ظژط§ط¨ظگظ‡ظگ* آ» ًںŒ¸\n\n"
    
    text += f"ًںŒ¹ *ط§ظ„ظ…ط³ط¬ظ„ط§طھ ظ„ظ„ظ‚ط±ط§ط،ط©:* ًںŒ¹\n"
    if not list_data["readers"]:
        text += f"ًں”¸ ظپظٹ ط§ظ†طھط¸ط§ط± ط£ظˆظ„ظ‰ ط§ظ„ط·ط§ظ„ط¨ط§طھ...\n"
    else:
        for i, user in enumerate(list_data["readers"], 1):
            status_check = " âœ…" if user["read"] else ""
            text += f"{i}. {user['name']}{status_check}\n"
    text += f"ًں”· ط¥ط¬ظ…ط§ظ„ظٹ ط§ظ„ط·ط§ظ„ط¨ط§طھ: {len(list_data['readers'])}\n\n"
    
    text += f"ًںژ§ *ط§ظ„ظ…ط³طھظ…ط¹ط§طھ ظˆط§ظ„ط­ط§ط¶ط±ط§طھ:* ًںژ§\n"
    if not list_data["listeners"]:
        text += f"ًں”¸ ظ„ط§ ظٹظˆط¬ط¯ ظ…ط³طھظ…ط¹ط§طھ ط­ط§ظ„ظٹط§ظ‹...\n"
    else:
        for i, user in enumerate(list_data["listeners"], 1):
            text += f"{i}. {user['name']}\n"
    text += f"ًں”· ط¥ط¬ظ…ط§ظ„ظٹ ط§ظ„ظ…ط³طھظ…ط¹ط§طھ: {len(list_data['listeners'])}\n\n"
    
    text += f"âœ¨â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬âœ¨\n"
    text += f"ًںŒ¸ ظ…ط¹ طھط­ظٹط§طھ ط¥ط¯ط§ط±ط© ط§ظ„ظ…ط¹ظ„ظ…ط© طµط§ط¨ط±ظٹظ† ًںŒ¸"
    return text

def generate_buttons():
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_read = types.InlineKeyboardButton("ًں“‌ ط£ط±ظٹط¯ ط¯ظˆط± ظ‚ط±ط§ط،ط©", callback_data="register_reader")
    btn_listen = types.InlineKeyboardButton("ًںژ§ ط­ط¶ظˆط± ظƒظ…ط³طھظ…ط¹ط©", callback_data="register_listener")
    btn_delete = types.InlineKeyboardButton("â‌Œ ط¥ط²ط§ظ„ط© ط§ط³ظ…ظٹ", callback_data="delete_me")
    btn_done = types.InlineKeyboardButton("âڑ™ï¸ڈ ظ„ظˆط­ط© ط§ظ„ظ…ط´ط±ظپط§طھ", callback_data="admin_select_read")
    
    markup.add(btn_read, btn_listen)
    markup.add(btn_done, btn_delete)
    
    if list_data["is_open"]:
        btn_close = types.InlineKeyboardButton("ًں”’ ط¥ط؛ظ„ط§ظ‚ ط§ظ„طھط³ط¬ظٹظ„", callback_data="close_list")
        markup.add(btn_close)
    else:
        btn_open = types.InlineKeyboardButton("ًں”“ ظپطھط­ ط§ظ„طھط³ط¬ظٹظ„", callback_data="open_list")
        markup.add(btn_open)
        
    return markup

def generate_select_readers_buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for user in list_data["readers"]:
        status_icon = "âœ… " if user["read"] else "âڈ³ "
        markup.add(types.InlineKeyboardButton(f"{status_icon}{user['name']}", callback_data=f"toggle_read_{user['id']}"))
    markup.add(types.InlineKeyboardButton("ًں”™ ط­ظپط¸ ظˆط±ط¬ظˆط¹ ظ„ظ„ظ‚ط§ط¦ظ…ط©", callback_data="back_to_main"))
    return markup

# â”€â”€ ط¯ظˆط§ظ„ ظ…ط´طھط±ظƒط© ظ„طھظ†ظپظٹط° ظƒظ„ ط¥ط¬ط±ط§ط، â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def action_new_list(chat_id, user_id):
    list_data["admin_id"] = user_id
    list_data["readers"] = []
    list_data["listeners"] = []
    list_data["is_open"] = True
    bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")

def action_show_list(chat_id):
    if list_data["admin_id"] is None:
        bot.send_message(chat_id, "âڑ ï¸ڈ ظ„ط§ طھظˆط¬ط¯ ظ‚ط§ط¦ظ…ط© ظ†ط´ط·ط© ط­ط§ظ„ظٹط§ظ‹.\nط§ظƒطھط¨ظٹ *ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط©* ظ„ط¨ط¯ط،.", parse_mode="Markdown")
        return
    bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")

def action_open_list(chat_id, user_id):
    if user_id != list_data["admin_id"]:
        bot.send_message(chat_id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ")
        return
    list_data["is_open"] = True
    bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")

def action_close_list(chat_id, user_id):
    if user_id != list_data["admin_id"]:
        bot.send_message(chat_id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ")
        return
    list_data["is_open"] = False
    bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")

def action_settings(chat_id, user_id, user_name):
    if user_id != list_data["admin_id"]:
        bot.send_message(chat_id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ")
        return
    text = (
        "âڑ™ï¸ڈ *ط¥ط¹ط¯ط§ط¯ط§طھ ط§ظ„ظ‚ط§ط¦ظ…ط©*\n\n"
        f"ًں‘¤ ط§ظ„ظ…ط´ط±ظپط© ط§ظ„ط­ط§ظ„ظٹط©: {user_name}\n"
        f"ًں“ٹ ط­ط§ظ„ط© ط§ظ„ظ‚ط§ط¦ظ…ط©: {'ًں”“ ظ…ظپطھظˆط­ط©' if list_data['is_open'] else 'ًں”’ ظ…ط؛ظ„ظ‚ط©'}\n"
        f"ًںŒ¹ ط¹ط¯ط¯ ط§ظ„ظ…ط³ط¬ظ„ط§طھ ظ„ظ„ظ‚ط±ط§ط،ط©: {len(list_data['readers'])}\n"
        f"ًںژ§ ط¹ط¯ط¯ ط§ظ„ظ…ط³طھظ…ط¹ط§طھ: {len(list_data['listeners'])}\n\n"
        "ًں“‹ *ط§ظ„ط£ظˆط§ظ…ط± ط§ظ„ظ…طھط§ط­ط©:*\n"
        "â€¢ /start â€” ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط©\n"
        "â€¢ /show â€” ط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ط­ط§ظ„ظٹط©\n"
        "â€¢ /open â€” ظپطھط­ ط§ظ„طھط³ط¬ظٹظ„\n"
        "â€¢ /close â€” ط¥ط؛ظ„ط§ظ‚ ط§ظ„طھط³ط¬ظٹظ„\n"
        "â€¢ /settings â€” ظ‡ط°ظ‡ ط§ظ„ط´ط§ط´ط©\n\n"
        "ط£ظˆ ط§ظƒطھط¨ظٹ ط§ظ„ط£ظ…ط± ط¨ط§ظ„ط¹ط±ط¨ظٹط© ظ…ط¨ط§ط´ط±ط©ظ‹ ط¨ط¯ظˆظ† ط´ط±ط·ط©."
    )
    bot.send_message(chat_id, text, parse_mode="Markdown")


# â”€â”€ ظ…ط¹ط§ظ„ط¬ط§طھ ط§ظ„ط£ظˆط§ظ…ط± ط¨ط§ظ„ط´ط±ط·ط© / â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
@bot.message_handler(commands=['start', 'startlist'])
def cmd_new_list(message):
    action_new_list(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['show'])
def cmd_show(message):
    action_show_list(message.chat.id)

@bot.message_handler(commands=['open'])
def cmd_open(message):
    action_open_list(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['close'])
def cmd_close(message):
    action_close_list(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['settings'])
def cmd_settings(message):
    user_name = message.from_user.first_name
    if message.from_user.last_name:
        user_name += f" {message.from_user.last_name}"
    action_settings(message.chat.id, message.from_user.id, user_name)


# â”€â”€ ظ…ط¹ط§ظ„ط¬ط§طھ ط§ظ„ظ†طµ ط§ظ„ط¹ط±ط¨ظٹ ط¨ط¯ظˆظ† ط´ط±ط·ط© â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
ARABIC_COMMANDS = {
    "ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط©",
    "ط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ط­ط§ظ„ظٹط©",
    "ظپطھط­ ط§ظ„ظ‚ط§ط¦ظ…ط©",
    "ط¥ط؛ظ„ط§ظ‚ ط§ظ„ظ‚ط§ط¦ظ…ط©",
    "ط¥ط¹ط¯ط§ط¯ط§طھ ط§ظ„ظ‚ط§ط¦ظ…ط©",
}

@bot.message_handler(func=lambda m: m.text and m.text.strip() in ARABIC_COMMANDS)
def handle_arabic_commands(message):
    text = message.text.strip()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if message.from_user.last_name:
        user_name += f" {message.from_user.last_name}"

    if text == "ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط©":
        action_new_list(message.chat.id, user_id)
    elif text == "ط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ط­ط§ظ„ظٹط©":
        action_show_list(message.chat.id)
    elif text == "ظپطھط­ ط§ظ„ظ‚ط§ط¦ظ…ط©":
        action_open_list(message.chat.id, user_id)
    elif text == "ط¥ط؛ظ„ط§ظ‚ ط§ظ„ظ‚ط§ط¦ظ…ط©":
        action_close_list(message.chat.id, user_id)
    elif text == "ط¥ط¹ط¯ط§ط¯ط§طھ ط§ظ„ظ‚ط§ط¦ظ…ط©":
        action_settings(message.chat.id, user_id, user_name)


# â”€â”€ ظ…ط¹ط§ظ„ط¬ ظ…ظ†ط´ظˆط±ط§طھ ط§ظ„ظ‚ظ†ط§ط© (channel_post) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
CHANNEL_COMMANDS = {
    "ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط©",
    "ط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ط­ط§ظ„ظٹط©",
    "ظپطھط­ ط§ظ„طھط³ط¬ظٹظ„",
    "ط§ط؛ظ„ط§ظ‚ ط§ظ„طھط³ط¬ظٹظ„",
}

@bot.channel_post_handler(func=lambda message: message.text and message.text.strip() in CHANNEL_COMMANDS)
def handle_channel_post(message):
    text = message.text.strip()
    chat_id = message.chat.id

    if text == "ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط©":
        # طھط¹ظٹظٹظ† ط§ظ„ظ‚ظ†ط§ط© ظ†ظپط³ظ‡ط§ ظ…ط´ط±ظپط©ظ‹ ط­طھظ‰ طھظ†ط¬ط­ ط£ظˆط§ظ…ط± ط§ظ„ظپطھط­ ظˆط§ظ„ط¥ط؛ظ„ط§ظ‚ ظ„ط§ط­ظ‚ط§ظ‹
        list_data["admin_id"] = chat_id
        list_data["readers"] = []
        list_data["listeners"] = []
        list_data["is_open"] = True
        bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")

    elif text == "ط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ط­ط§ظ„ظٹط©":
        if list_data["admin_id"] is None:
            bot.send_message(chat_id, "âڑ ï¸ڈ ظ„ط§ طھظˆط¬ط¯ ظ‚ط§ط¦ظ…ط© ظ†ط´ط·ط© ط­ط§ظ„ظٹط§ظ‹.\nط§ظƒطھط¨ظٹ *ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط©* ظ„ط¨ط¯ط،.", parse_mode="Markdown")
            return
        bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")

    elif text == "ظپطھط­ ط§ظ„طھط³ط¬ظٹظ„":
        # ظ…ظ†ط´ظˆط± ط§ظ„ظ‚ظ†ط§ط© طµط§ط¯ط± ظ…ظ† ظ…ط´ط±ظپ ط¯ط§ط¦ظ…ط§ظ‹ â€” ظ†طھط¬ط§ظˆط² ط§ظ„طھط­ظ‚ظ‚
        list_data["admin_id"] = chat_id
        list_data["is_open"] = True
        bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")

    elif text == "ط§ط؛ظ„ط§ظ‚ ط§ظ„طھط³ط¬ظٹظ„":
        list_data["admin_id"] = chat_id
        list_data["is_open"] = False
        bot.send_message(chat_id, generate_list_text(), reply_markup=generate_buttons(), parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_name = call.from_user.first_name
    if call.from_user.last_name:
        user_name = f"{call.from_user.first_name} {call.from_user.last_name}"
        
    user_id = call.from_user.id
    
    if call.data == "admin_select_read":
        if user_id != list_data["admin_id"]:
            bot.answer_callback_query(call.id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ", show_alert=True)
            return
        if not list_data["readers"]:
            bot.answer_callback_query(call.id, "ظ„ط§ طھظˆط¬ط¯ ط·ط§ظ„ط¨ط§طھ ظ…ط³ط¬ظ„ط§طھ ظپظٹ ط§ظ„ظ‚ط±ط§ط،ط© ط­ط§ظ„ظٹط§ظ‹! âڈ³", show_alert=True)
            return
            
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="âڑ ï¸ڈ *ظ„ظˆط­ط© ط§ظ„ظ…ط´ط±ظپط©:*\nط§ط¶ط؛ط·ظٹ ط¹ظ„ظ‰ ط§ط³ظ… ط§ظ„ط·ط§ظ„ط¨ط© ظ„طھط­ط¯ظٹط¯ظ‡ط§ ظƒظ‚ط§ط±ط¦ط© ط£ظˆ ط¥ظ„ط؛ط§ط، ط§ظ„طھط­ط¯ظٹط¯طŒ ط«ظ… ط§ط¶ط؛ط·ظٹ ط¹ظ„ظ‰ ط²ط± ط§ظ„ط±ط¬ظˆط¹ ط¨ط§ظ„ط£ط³ظپظ„ ظ„ط­ظپط¸ ظˆط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ظ…ط­ط¯ط«ط©:",
            reply_markup=generate_select_readers_buttons(),
            parse_mode="Markdown"
        )
        return
        
    elif call.data.startswith("toggle_read_"):
        if user_id != list_data["admin_id"]:
            bot.answer_callback_query(call.id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ", show_alert=True)
            return
        target_id = int(call.data.replace("toggle_read_", ""))
        for user in list_data["readers"]:
            if user["id"] == target_id:
                user["read"] = not user["read"]
                break
                
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="âڑ ï¸ڈ *ظ„ظˆط­ط© ط§ظ„ظ…ط´ط±ظپط©:*\nط§ط¶ط؛ط·ظٹ ط¹ظ„ظ‰ ط§ط³ظ… ط§ظ„ط·ط§ظ„ط¨ط© ظ„طھط­ط¯ظٹط¯ظ‡ط§ ظƒظ‚ط§ط±ط¦ط© ط£ظˆ ط¥ظ„ط؛ط§ط، ط§ظ„طھط­ط¯ظٹط¯طŒ ط«ظ… ط§ط¶ط؛ط·ظٹ ط¹ظ„ظ‰ ط²ط± ط§ظ„ط±ط¬ظˆط¹ ط¨ط§ظ„ط£ط³ظپظ„ ظ„ط­ظپط¸ ظˆط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ظ…ط­ط¯ط«ط©:",
            reply_markup=generate_select_readers_buttons(),
            parse_mode="Markdown"
        )
        return
        
    elif call.data == "back_to_main":
        if user_id != list_data["admin_id"]:
            bot.answer_callback_query(call.id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ", show_alert=True)
            return
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=generate_list_text(),
            reply_markup=generate_buttons(),
            parse_mode="Markdown"
        )
        return

    elif call.data == "close_list":
        if user_id != list_data["admin_id"]:
            bot.answer_callback_query(call.id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ", show_alert=True)
            return
        list_data["is_open"] = False
        
    elif call.data == "open_list":
        if user_id != list_data["admin_id"]:
            bot.answer_callback_query(call.id, "ط¹ط°ط±ط§ظ‹طŒ ظ‡ط°ط§ ط§ظ„ط¥ط¬ط±ط§ط، ظ…ط®طµطµ ظ„ظ„ظ…ط´ط±ظپط§طھ ظپظ‚ط·! â‌Œ", show_alert=True)
            return
        list_data["is_open"] = True
        
    elif list_data["is_open"]:
        if call.data == "register_reader":
            if not any(u['id'] == user_id for u in list_data["readers"]):
                list_data["listeners"] = [u for u in list_data["listeners"] if u['id'] != user_id]
                list_data["readers"].append({"name": user_name, "id": user_id, "read": False})
                
        elif call.data == "register_listener":
            if not any(u['id'] == user_id for u in list_data["listeners"]):
                list_data["readers"] = [u for u in list_data["readers"] if u['id'] != user_id]
                list_data["listeners"].append({"name": user_name, "id": user_id})
                
        elif call.data == "delete_me":
            list_data["readers"] = [u for u in list_data["readers"] if u['id'] != user_id]
            list_data["listeners"] = [u for u in list_data["listeners"] if u['id'] != user_id]
            
    else:
        bot.answer_callback_query(call.id, "ط¹ط°ط±ط§ظ‹طŒ ط§ظ„ظ‚ط§ط¦ظ…ط© ظ…ط؛ظ„ظ‚ط© ط­ط§ظ„ظٹط§ظ‹ ًں”’", show_alert=True)
        return

    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=generate_list_text(),
            reply_markup=generate_buttons(),
            parse_mode="Markdown"
        )
    except Exception:
        pass



# â”€â”€ ط®ط§ط¯ظ… Flask ظ„ظ„ط¨ظ‚ط§ط، ط­ظٹط§ظ‹ â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
import time
import requests
import urllib3
from flask import Flask, jsonify
from threading import Thread, Event

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask('')
_bot_start_time = datetime.now()

@app.route('/')
def home():
    return "Bot is alive! ًں¤–"

@app.route('/health')
def health():
    uptime_seconds = int((datetime.now() - _bot_start_time).total_seconds())
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return jsonify({
        "status": "ok",
        "bot": "running",
        "uptime": f"{hours}h {minutes}m {seconds}s",
        "list_open": list_data["is_open"],
        "readers": len(list_data["readers"]),
        "listeners": len(list_data["listeners"]),
    })

@app.route('/ping')
def ping():
    return "pong", 200

def run_flask():
    app.run(host='0.0.0.0', port=8000)

# â”€â”€ ط§ظ„ط±ط§ط¨ط· ط§ظ„ط¹ط§ظ… ظ„ظ„ظ†ظ‚ط± ط¹ظ„ظٹظ‡ ظ…ظ† UptimeRobot ط£ظˆ ط§ظ„ظ€ self-ping â”€â”€â”€â”€â”€â”€â”€â”€â”€
def _get_public_ping_url() -> str:
    domains = os.environ.get("REPLIT_DOMAINS", "")
    host = domains.split(",")[0].strip() if domains else ""
    if host:
        return f"https://{host}/ping"
    return "http://127.0.0.1:8000/ping"

def self_ping():
    """
    Ping the PUBLIC Replit URL every 3 minutes.
    Pinging 127.0.0.1 does NOT prevent Replit sleep â€”
    only traffic through the public proxy resets the sleep timer.
    """
    url = _get_public_ping_url()
    print(f"[keep-alive] self-ping target: {url}")
    time.sleep(20)          # ط§ظ†طھط¸ط± ط­طھظ‰ ظٹط¨ط¯ط£ Flask
    while True:
        try:
            r = requests.get(url, timeout=15, verify=False)
            print(f"[keep-alive] ping â†’ {r.status_code}")
        except Exception as e:
            print(f"[keep-alive] ping failed: {e}")
        time.sleep(180)     # ظƒظ„ 3 ط¯ظ‚ط§ط¦ظ‚

def keep_alive():
    flask_thread = Thread(target=run_flask, daemon=True, name="flask")
    ping_thread  = Thread(target=self_ping, daemon=True, name="self-ping")
    flask_thread.start()
    ping_thread.start()

    # â”€â”€ ظ…ط±ط§ظ‚ط¨ ط§ظ„ط®ظٹظˆط·: ظٹط¹ظٹط¯ ط¥ط·ظ„ط§ظ‚ ط£ظٹ ط®ظٹط· ظ…ط§طھ â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    def thread_watchdog():
        threads = {"flask": (flask_thread, run_flask), "self-ping": (ping_thread, self_ping)}
        while True:
            time.sleep(60)
            for name, (t, fn) in list(threads.items()):
                if not t.is_alive():
                    print(f"[thread-watchdog] '{name}' died â€” restarting")
                    new_t = Thread(target=fn, daemon=True, name=name)
                    new_t.start()
                    threads[name] = (new_t, fn)

    Thread(target=thread_watchdog, daemon=True, name="thread-watchdog").start()

@bot.message_handler(commands=['myid'])
def cmd_myid(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.send_message(
        message.chat.id,
        f"ًں†” *ظ…ط¹ط±ظ‘ظپط§طھ ط­ط³ط§ط¨ظƒ:*\n\n"
        f"â€¢ Chat ID: `{chat_id}`\n"
        f"â€¢ User ID: `{user_id}`\n\n"
        f"ط§ظ†ط³ط®ظٹ *Chat ID* ظˆط¶ط¹ظٹظ‡ ظپظٹ ظ…طھط؛ظٹط± ط§ظ„ط¨ظٹط¦ط© `ADMIN_CHAT_ID` ظ„طھظ„ظ‚ظٹ طھظ†ط¨ظٹظ‡ط§طھ ط§ظ„ط¨ظˆطھ.",
        parse_mode="Markdown"
    )


if __name__ == "__main__":
    bot.set_my_commands([
        types.BotCommand("start",    "ط¨ط¯ط، ظ‚ط§ط¦ظ…ط© ط¬ط¯ظٹط¯ط© ًںŒ¹"),
        types.BotCommand("show",     "ط¹ط±ط¶ ط§ظ„ظ‚ط§ط¦ظ…ط© ط§ظ„ط­ط§ظ„ظٹط© ًں“‹"),
        types.BotCommand("open",     "ظپطھط­ ط§ظ„طھط³ط¬ظٹظ„ ًں”“"),
        types.BotCommand("close",    "ط¥ط؛ظ„ط§ظ‚ ط§ظ„طھط³ط¬ظٹظ„ ًں”’"),
        types.BotCommand("settings", "ط¥ط¹ط¯ط§ط¯ط§طھ ط§ظ„ظ‚ط§ط¦ظ…ط© âڑ™ï¸ڈ"),
        types.BotCommand("myid",     "ط§ط¹ط±ظپظٹ ظ…ط¹ط±ظ‘ظپ ط­ط³ط§ط¨ظƒ ًں†”"),
    ])

    domains = os.environ.get("REPLIT_DOMAINS", "")
    public_host = domains.split(",")[0].strip() if domains else "localhost:8000"
    print(f"âœ… Bot is running!")
    print(f"ًںŒگ Uptime Robot URL: https://{public_host}/health")
    print(f"   (Monitor type: HTTP / Keyword 'ok'  â€” interval: 5 min)")

    keep_alive()
    notify_admin("ًںں¢ *ط§ظ„ط¨ظˆطھ ظٹط¹ظ…ظ„ ط§ظ„ط¢ظ†*\nطھظ… طھط´ط؛ظٹظ„ ط§ظ„ط¨ظˆطھ ط¨ظ†ط¬ط§ط­ ظˆظ‡ظˆ ط¬ط§ظ‡ط² ظ„ط§ط³طھظ‚ط¨ط§ظ„ ط§ظ„ط£ظˆط§ظ…ط±.")

    # Watchdog loop: auto-restart polling on crash and alert admin
    while True:
        try:
            print("[watchdog] Starting polling...")
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"[watchdog] Polling crashed: {e}")
            notify_admin(
                f"ًں”´ *طھط­ط°ظٹط±: طھظˆظ‚ظپ ط§ظ„ط¨ظˆطھ!*\n\n"
                f"ط§ظ„ط³ط¨ط¨: `{e}`\n\n"
                f"âڈ³ ط¬ط§ط±ظٹ ط¥ط¹ط§ط¯ط© ط§ظ„طھط´ط؛ظٹظ„ طھظ„ظ‚ط§ط¦ظٹط§ظ‹..."
            )
            time.sleep(5)
            notify_admin("ًںں، *ط¬ط§ط±ظٹ ط¥ط¹ط§ط¯ط© طھط´ط؛ظٹظ„ ط§ظ„ط¨ظˆطھ...*")