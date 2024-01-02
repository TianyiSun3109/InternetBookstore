SET NAMES UTF8;
-- DROP DATABASE IF EXISTS jd;
-- CREATE DATABASE jd CHARSET=UTF8;
USE jd;

-- CREATE TABLE jd_user(
--   uid INT PRIMARY KEY AUTO_INCREMENT, 
--   uname VARCHAR(32),
--   upwd VARCHAR(32)
-- );


-- INSERT INTO jd_user VALUES
-- ('1','qiangdong','123456'),
-- ('2','naicha','456789');


CREATE TABLE IF NOT EXISTS jd_book (
    year INT,
    `Rank` INT,
    picture VARCHAR(255),
    name VARCHAR(255),
    pinglun VARCHAR(63),
    author VARCHAR(63),
    chuban VARCHAR(63),
    jiage VARCHAR(63),
    yuanjia VARCHAR(63),
    discount VARCHAR(63),
    id INT PRIMARY KEY AUTO_INCREMENT
);

LOAD DATA LOCAL INFILE'C:/CodeField/CODE_PYTHON/InternetBookstore/book.csv'
INTO TABLE jd_book character set utf8
FIELDS TERMINATED BY ','  -- 根据实际情况修改分隔符
LINES TERMINATED BY '\r\n'  -- 根据实际情况修改行分隔符
IGNORE 1 LINES;
