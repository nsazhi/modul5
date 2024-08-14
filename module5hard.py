import time


class UrTube:
    __instance = None
    users = []
    videos = []
    current_user = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.data_users = {}
        self.data_videos = {}

    def __add__(self):
        if isinstance(self, User):
            UrTube.users.append(self)
        if isinstance(self, Video):
            UrTube.videos.append(self)

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        self.data_users['nickname'] = user.nickname
        self.data_users['password'] = User.__hash__(password)
        self.data_users['age'] = user.age
        if UrTube.users:
            for i in UrTube.users:
                check_user = i.nickname
                if nickname == check_user:
                    print(f'Пользователь {nickname} уже существует.')
                else:
                    UrTube.__add__(user)
                    break
        else:
            UrTube.__add__(user)
            UrTube.current_user = nickname
        # print(f'Пользователи: {UrTube.users}')

    def log_in(self, nickname, password):
        if UrTube.users:
            for i in UrTube.users:
                check_user = i.nickname
                check_password = i.password
                if nickname == check_user and User.__hash__(password) == check_password:
                    UrTube.current_user = nickname
                else:
                    print('Пользователь не найден.')
                    break
        else:
            print('Список пользователей пуст.')

    def log_out(self, nickname):
        self.nickname = nickname
        if nickname == UrTube.current_user:
            UrTube.current_user = None
            exit()

    def add(self, *args):
        for i in args:
            self.data_videos = i
            search_title = self.data_videos.title
            if UrTube.videos:
                for j in UrTube.videos:
                    if j.title == search_title:
                        break
                    else:
                        UrTube.__add__(i)
                        break
            else:
                UrTube.__add__(i)
        # print(f'Видео: {UrTube.videos}')

    def get_videos(self, search_str):
        self.search_str = search_str
        get_list = []
        search_str = search_str.lower()
        for i in UrTube.videos:
            title_lower = i.title.lower()
            if search_str in title_lower:
                get_list.append(i.title)
        return get_list

    def __lt__(self, value):
        for i in UrTube.users:
            if i.age < value:
                print(f'Вам нет 18 лет, пожалуйста покиньте страницу.')
                exit()
            else:
                break

    def watch_video(self, search_title):
        self.search_title = search_title
        if UrTube.current_user:
            for i in UrTube.videos:
                if search_title != i.title:
                    continue
                if i.adult_mode:
                    UrTube.__lt__(self, 18)
                duration = i.duration
                duration_list = []
                for j in range(1, duration + 1):
                    time.sleep(1)
                    duration_list.append(j)
                    print(*duration_list)
                    j += 1
                    if j > duration:
                        duration_list.append('Конец видео.')
                        print(*duration_list)
                        j = 1
                        duration_list = []
                        break
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
    database = UrTube()

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# # Проверка на вход/выход пользователя
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# time.sleep(5)
# ur.register('vasya_popkin', 'lolkekcheburek', 13)
# time.sleep(5)
# ur.log_in('vasya_pupkin', 'lolkekcheburek')
# time.sleep(5)
# ur.log_out('vasya_pupkin')


# Проверка на просмотр видео и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
