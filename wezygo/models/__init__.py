from models.base_person import BasePerson
from os import getenv

if getenv("WEGO_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.filestorage import FileStorage
    storage = FileStorage()
storage.reload()


#echo 'create State name="California"' | WEGO_MYSQL_USER=wezygo_dev WEGO_MYSQL_PWD=wezygo_dev_pw WEGO_MYSQL_HOST=localhost WEGO_MYSQL_DB=wezygo_dev_db WEGO_TYPE_STORAGE=db ./console.py 