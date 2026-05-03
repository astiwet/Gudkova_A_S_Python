from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:
    __scripts = {
        "select": text("SELECT * FROM subject"),
        "insert_new": text("INSERT INTO subject (\"subject_title\", \"subject_id\") values (:subject_title, :subject_id)"),
        "get_max_id": text("SELECT MAX(\"subject_id\") FROM subject"),
        "delete_by_id": text("DELETE FROM subject WHERE subject_id =:subject_id"),
        "edited_subject": text("UPDATE subject SET \"subject_title\" =:subject_title WHERE "
                                      "subject_id =:subject_id"),
        "select_by_id": text("SELECT * FROM subject "
                         "WHERE subject_id =:select_id")
        }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subject(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_id"], {"subject_id": id})
        conn.commit()
        conn.close()

    def create(self, name, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"], {"subject_title": name, "subject_id": id})
        conn.commit()
        conn.close()
   
    
    def edit_subject(self, name, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["edited_subject"], {"subject_title": name, "subject_id": id })
        conn.commit()
        conn.close()

    def get_subject_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_by_id"], {"select_id": id}
                              )
        subject = result.mappings().all()
        conn.close()
        return subject
    