CREATE DATABASE IF NOT EXISTS wezygo_dev_db;
CREATE USER IF NOT EXISTS 'jose'@'localhost' IDENTIFIED BY 'jose';
GRANT ALL PRIVILEGES ON `wezygo_dev_db`.* TO 'jose'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'jose'@'localhost';
FLUSH PRIVILEGES;