-- script creating hbtn_0d_2 database and a user_0d_2 user
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@host IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON btn_0d_2.* TO user_0d_2@host;
FLUSH PRIVILEGES;
