import time


class UrTube:
    __instance = None
    current_user = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.data_users = {}
        self.data_videos = {}

    def register(self, nickname, password, age):
        if nickname in self.data_users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            user = User(nickname, password, age)
            self.data_users[user.nickname] = {'password': user.password, 'age': user.age}
            self.current_user = nickname

    def log_in(self, nickname, password):
        if nickname in self.data_users:
            if User.__hash__(password) == self.data_users[nickname].get('password'):
                self.current_user = nickname
        else:
            print('Пользователь не найден.')

    def log_out(self, nickname):
        if nickname == self.current_user:
            self.current_user = None
            exit()

    def add(self, *args):
        for i in args:
            if i.title in self.data_videos:
                break
            else:
                self.data_videos[i.title] = {'duration': i.duration, 'time_now': i.time_now, 'adult_mode': i.adult_mode}

    def get_videos(self, search_str):
        get_list = []
        search_str = search_str.lower()
        for key in self.data_videos:
            title_lower = key.lower()
            if search_str in title_lower:
                get_list.append(key)
        return get_list

    def __lt__(self, value):
        current_age = self.data_users[self.current_user].get('age')
        if current_age < value:
            print(f'Вам нет 18 лет, пожалуйста, покиньте страницу. Возраст: {current_age}')
            exit()

    def watch_video(self, search_title):
        if self.current_user:
            if search_title in self.data_videos:
                if self.data_videos[search_title].get('adult_mode'):
                    self.__lt__(18)
                duration = self.data_videos[search_title].get('duration')
                for time_now in range(duration):
                    time_now = self.data_videos[search_title].get('time_now')
                    time.sleep(1)
                    time_now += 1
                    self.data_videos[search_title].update({'time_now': time_now})
                    print(time_now)
                    if time_now == duration:
                        print('Конец видео.')
                        i = 0
            else:
                print('Такого видео не существует.')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            exit()


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = User.__hash__(password)
        self.age = age

    def __hash__(self):
        password = hash(self)
        return password


if __name__ == '__main__':
    ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v1)

# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))

# # Проверка на вход/выход пользователя
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# time.sleep(3)
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# time.sleep(3)
# ur.register('vasya_popkin', 'lolkekcheburek', 13)
# time.sleep(3)
# ur.log_in('vasya_pupkin', 'lolkekcheburek')
# time.sleep(3)
# ur.log_out('vasya_pupkin')

# Проверка на просмотр видео и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
