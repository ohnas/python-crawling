from dotenv import load_dotenv
import os
import pymysql
import logging

load_dotenv()

HOST = os.environ.get("HOST")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
PORT = int(os.environ.get("PORT"))
CHARSET = os.environ.get("CHARSET")


logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(levelname)s : %(asctime)s : %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S %p",
)


class DBManager:
    def __init__(self, table_name, data):
        self.con = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            db=DB_NAME,
            charset=CHARSET,
            port=PORT,
        )
        self.cur = self.con.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_idiom
                (id INTEGER PRIMARY KEY AUTO_INCREMENT, date text, name text, link text, meaning text, example text)
        """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS all_idioms
                (id INTEGER PRIMARY KEY AUTO_INCREMENT, name text, link text, meaning text, example text)
        """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_word
                (id INTEGER PRIMARY KEY AUTO_INCREMENT, date text, word text, img_src text, link text)
        """
        )
        self.table_name = table_name
        self.data = data

    def create(self):
        try:
            if self.table_name == "daily_idiom":
                self.cur.execute(
                    "INSERT INTO daily_idiom (date, name, link, meaning, example) VALUES (%s,%s,%s,%s,%s)",
                    self.data,
                )
            elif self.table_name == "daily_word":
                self.cur.execute(
                    "INSERT INTO daily_word (date, word, img_src, link) VALUES (%s,%s,%s,%s)",
                    self.data,
                )
            elif self.table_name == "all_idioms":
                self.cur.executemany(
                    "INSERT INTO all_idioms (name, link, meaning, example) VALUES (%s,%s,%s,%s)",
                    self.data,
                )

            self.con.commit()
            self.con.close()
            logging.info("create is done.")

        except Exception as err:
            logging.error(f"An error occurred: {err} in create of DBManager")

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


def is_empty():
    # cron으로 python script 실행할려면 로컬파일의 절대경로가 필요 상대경로일때는 홈 디렉토리에서 cron 이 실행되기때문에 찾지 못함
    con = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DB_NAME,
        charset=CHARSET,
        port=PORT,
    )
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM all_idioms")
    res = cur.fetchone()

    return res[0]
