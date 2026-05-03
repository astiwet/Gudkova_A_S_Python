from SubjectTable import SubjectTable


db = SubjectTable("postgresql://postgres:123@localhost/QASQL")

def test_add_subject():
    body = db.get_subject()
    len_before = len(body)
    max_id = db.get_max_id()
    name = "QA"
    result = db.create(name, max_id+1)
    body = db.get_subject()
    len_after = len(body)
    max_id = db.get_max_id()
    db.delete(max_id)
    assert len_after - len_before == 1

def test_edit():
    max_id = db.get_max_id()
    name = "QA"
    db.create(name, max_id+1)
    maxx_id = db.get_max_id()
    new_name = "IT"
    edited = db.edit_subject(new_name, maxx_id)
    subject = db.get_subject_by_id(maxx_id)
    db.delete(maxx_id)
    assert subject[-1]["subject_title"] == new_name


def test_delete():
    max_id = db.get_max_id()
    name = "QA"
    db.create(name, max_id+1)
    max_id = db.get_max_id()
    db.delete(max_id)
    rows = db.get_subject_by_id(max_id)
    assert len(rows) == 0


