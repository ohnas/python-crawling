import sqlite3


class DBManager:
    def __init__(self, table_name, data):
        # cron으로 python script 실행할려면 로컬파일의 절대경로가 필요 상대경로일때는 홈 디렉토리에서 cron 이 실행되기때문에 찾지 못함
        self.con = sqlite3.connect(
            "/Users/ohnaseong/Documents/python-crawling/crawling.db"
        )
        self.cur = self.con.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_idiom
                (id INTEGER PRIMARY KEY, date text, name text, link text, meaning text, example text)
        """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS all_idioms
                (id INTEGER PRIMARY KEY, name text, link text, meaning text, example text)
        """
        )
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_word
                (id INTEGER PRIMARY KEY, date text, word text, img_src text, link text)
        """
        )
        self.table_name = table_name
        self.data = data

    def create(self):
        if self.table_name == "daily_idiom":
            self.cur.execute(
                "INSERT INTO daily_idiom (date, name, link, meaning, example) VALUES (?,?,?,?,?)",
                self.data,
            )
        elif self.table_name == "daily_word":
            self.cur.execute(
                "INSERT INTO daily_word (date, word, img_src, link) VALUES (?,?,?,?)",
                self.data,
            )
        elif self.table_name == "all_idioms":
            self.cur.executemany(
                "INSERT INTO all_idioms (name, link, meaning, example) VALUES (?,?,?,?)",
                self.data,
            )

        self.con.commit()
        self.con.close()

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


def is_empty():
    # cron으로 python script 실행할려면 로컬파일의 절대경로가 필요 상대경로일때는 홈 디렉토리에서 cron 이 실행되기때문에 찾지 못함
    con = sqlite3.connect("/Users/ohnaseong/Documents/python-crawling/crawling.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM all_idioms")
    res = cur.fetchone()

    return res[0]
