import threading
import schedule
from time import sleep, localtime


class Time:
    hour: int
    minute: int


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def useless_job():
    current_time = localtime()
    print("I'm working...")
    print(f"It's {current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}")
    sleep(5)


time = Time()


# -
time.hour = 16
time.minute = 18

timezone = "Asia/Novosibirsk"

job1 = useless_job
# job2 = ...

# -

schedule.every().day.at(f"{time.hour:02}:{time.minute:02}", timezone).do(run_threaded, job1)
schedule.every().day.at(f"{time.hour:02}:{time.minute:02}", timezone).do(run_threaded, job1)
schedule.every().day.at(f"{time.hour:02}:{time.minute:02}", timezone).do(run_threaded, job1)
schedule.every().day.at(f"{time.hour:02}:{time.minute:02}", timezone).do(run_threaded, job1)

# job()

while True:
    schedule.run_pending()
    sleep(1)
