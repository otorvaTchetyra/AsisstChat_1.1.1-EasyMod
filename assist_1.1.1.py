import threading
import time

def send_message(message):
    print(message)

def check_time():
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Пример сообщения, которое будет отправлено в 12:00
        if hour == 12 and minute == 0 and second == 0:
            send_message("Время обеда! Пора подкрепиться!")

        # Пример сообщения, которое будет отправляться каждую минуту
        if minute % 5 == 0:
            send_message(f"Прошло {minute // 5} пятеринок минут с начала часа.")

        time.sleep(1)  # Ждем 1 секунду перед следующей итерацией цикла

if __name__ == "__main__":
    thread = threading.Thread(target=check_time)
    thread.start()

    try:
        while True:
            message = input("Введите сообщение: ")
            send_message(message)
    except KeyboardInterrupt:
        pass