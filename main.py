from playsound import playsound
import schedule
import time
import datetime

# https://pypi.org/project/schedule/
def sound_bell():
    waktu = datetime.datetime.now()
    print(waktu)
    print('Membunyikan bel pada {waktu}'.format(waktu=waktu))
    playsound('alarm.wav')


schedule.every().day.at("07:45").do(sound_bell)
schedule.every().day.at("09:30").do(sound_bell)
schedule.every().day.at("10:00").do(sound_bell)
schedule.every().day.at("11:30").do(sound_bell)
schedule.every().day.at("13:00").do(sound_bell)
schedule.every().day.at("14:30").do(sound_bell)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Bel Sekolah SD IA')
    while True:
        schedule.run_pending()
        time.sleep(1)
