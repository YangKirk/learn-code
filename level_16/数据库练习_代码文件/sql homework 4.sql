USE book_management;

-- 1.找出姓李的读者姓名（NAME）和所在单位(COMPANY).
SELECT NAME, COMPANY FROM reader
WHERE NAME LIKE '李%';

-- 2.列出图书库中所有藏书的书名(BOOK_NAME)以及出版单位(OUTPUT).
SELECT DISTINCT BOOK_NAME, OUTPUT FROM BOOK;	-- 暗含排除重复条件

-- 3.查找“高等教育出版社”的所有图书名称（BOOK_NAME）及单价（PRICE）,结果按单价降价排序.
SELECT BOOK_NAME, PRICE FROM BOOK
WHERE OUTPUT = '高等教育出版社'
ORDER BY PRICE DESC;

-- 4.查找价格介于10元和20元之间的图书种类(SORT),结果按出版单位(OUTPUT)和单价（PRICE）升序排序.
SELECT SORT FROM BOOK
WHERE PRICE BETWEEN 10 AND 20
ORDER BY OUTPUT, PRICE;

-- 5.查找书名以“计算机” 开头的所有图书和作者(WRITER)。
SELECT DISTINCT BOOK_NAME, WRITER FROM BOOK
WHERE BOOK_NAME LIKE '计算机%';

-- 6.查找所有借了书的读者的姓名(NAME)及所在单位(COMPANY).
SELECT r.NAME, r.COMPANY  FROM READER r INNER JOIN borrow b
ON r.READER_ID = b.READER_ID;

-- 7.找出李某所借所有图书的书名及借书日期（BORROW_DATE）
-- SELECT BOOK.BOOK_NAME 书名, borrow.BORROW_DATE 借阅日期 FROM book INNER JOIN borrow INNER JOIN reader
-- ON book.BOOK_ID = borrow.BOOK_ID AND borrow.READER_ID = reader.READER_ID
-- WHERE reader.`NAME` LIKE '李%';

SELECT BOOK.BOOK_NAME 书名, borrow.BORROW_DATE 借阅日期 FROM book INNER JOIN borrow ON book.BOOK_ID = borrow.BOOK_ID  INNER JOIN reader on reader.READER_ID = borrow.READER_ID
WHERE reader.`NAME` LIKE '李_';

-- 8.查询2006年7月以后没有借书的读者借书证号、姓名及单位。
-- SELECT DISTINCT READER_ID FROM borrow WHERE BORROW_DATE > "2006-07";
SELECT READER_ID, `NAME`, COMPANY FROM reader WHERE READER_ID NOT IN 
(SELECT DISTINCT READER_ID FROM borrow WHERE BORROW_DATE > "2006-07");

-- 9.求出各个出版社图书的最高价格、最低价格和总册数。
SELECT DISTINCT MAX(PRICE), MIN(PRICE), COUNT(*), OUTPUT FROM book
GROUP BY OUTPUT;

-- 10.找出与‘赵正义’ 在同一天借书的读者姓名、所在单位及借书日期

-- SELECT reader.`NAME`, reader.COMPANY, borrow.BORROW_DATE 
-- FROM reader INNER JOIN borrow
-- ON reader.READER_ID = borrow.READER_ID
-- WHERE BORROW_DATE IN (
-- 											SELECT BORROW_DATE FROM borrow 
-- 											WHERE READER_ID = (
-- 											SELECT READER_ID FROM reader 
-- 											WHERE `NAME` = '赵正义')) AND reader.`NAME` !='赵正义';

-- SELECT BORROW_DATE FROM reader INNER JOIN borrow ON reader.READER_ID = borrow.READER_ID WHERE `NAME`='赵正义';
SELECT reader.`NAME`, reader.COMPANY, borrow.BORROW_DATE 
FROM reader INNER JOIN borrow
ON reader.READER_ID = borrow.READER_ID
WHERE BORROW_DATE IN (SELECT BORROW_DATE FROM reader INNER JOIN borrow
ON reader.READER_ID = borrow.READER_ID WHERE `NAME`='赵正义') AND reader.`NAME` <>'赵正义';
