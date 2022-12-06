class DataBase:
<<<<<<< HEAD
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataBase, cls).__new__(cls)
=======
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataBase.cls).__new__(cls)
>>>>>>> 870d834fd2f3f7975fb5f7aad5a4271817981b76
        return cls.instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(db is db2)
