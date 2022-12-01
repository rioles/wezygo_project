CREATE DATABASE IF NOT EXISTS wezygo_dev_db;
CREATE USER IF NOT EXISTS 'jose'@'localhost' IDENTIFIED BY 'jose';
GRANT ALL PRIVILEGES ON `wezygo_dev_db`.* TO 'jose'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'jose'@'localhost';
FLUSH PRIVILEGES;


echo 'create Merchant first_name="California" surn_name="aude"' | WEGO_MYSQL_USER=jose WEGO_MYSQL_PWD=jose WEGO_MYSQL_HOST=localhost WEGO_MYSQL_DB=wezygo_dev_db WEGO_TYPE_STORAGE=db ./console.py