-- Creates the MySQL User user_0d_1 with all privileges
-- and password set to user_0d_1_pwd

CREATE USER 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;