import time, os
from datetime import datetime
from ed_scraper import fetch_domains
from telegram_bot import bot_send
from storage import load_sent, save_sent

INTERVAL = int(os.getenv("CHECK_INTERVAL", 1800))  # default 30 phút

def main():
    sent = load_sent()
    while True:
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            domains = fetch_domains()
            new_domains = [d for d in domains if d not in sent]

            if new_domains:
                bot_send(f"🔔 [{now}] Tìm được {len(new_domains)} domain mới:")
                for d in new_domains:
                    bot_send(f"✅ {d}")
                    sent.add(d)
                save_sent(sent)
            else:
                bot_send(f"📘 [{now}] Không có domain mới. Bot vẫn chạy.")

        except Exception as e:
            bot_send(f"❌ Lỗi khi quét domain: {e}")

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
