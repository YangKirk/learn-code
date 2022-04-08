-- 练习题1. 根据要求创建一个Product表，并向其中插入以下数据。
-- Table: Product  | 字段1：product_id(商品id)，4位字符，非空，主键  |  字段2：product_name(商品名称)，可变字符100位，非空  | 字段3: product_type(商品类型)，可变长32位，非空 | 字段4：sale_price（销售价格），整型，字段5：purchase_price(进货价格)，整型 | 字段6：regist_date(注册日期)，日期型
-- 插入数据如下:
-- '0001','T恤','衣服',1000,500,'2009-09-20'
-- '0002','打孔器','办公用品',500,320,'2009-09-11'
-- '0003','运动T恤','衣服',4000,2800,NULL);
-- '0004','菜刀','厨房用具',3000,2800,'2009-09-20'
-- '0005','高压锅','厨房用具',6800,5000,'2009-01-15'
-- '0006','叉子','厨房用具',500,NULL,'2009-09-20'
-- '0007','擦菜板','厨房用具',880,790,'2008-04-28'
-- '0008','圆珠笔','办公用品',100,NULL,'2009-11-11'

USE demo;
CREATE TABLE IF NOT EXISTS Product(
	product_id CHAR(4) NOT NULL PRIMARY KEY,
	product_name VARCHAR(100) NOT NULL,
	product_type VARCHAR(32) NOT NULL,
	sale_price INT,
	purchase_price INT,
	regist_date DATE
	) ENGINE=INNODB DEFAULT CHARACTER SET utf8;

INSERT INTO Product VALUES('0001','T恤','衣服',1000,500,'2009-09-20');
INSERT INTO Product VALUES('0002','打孔器','办公用品',500,320,'2009-09-11');
INSERT INTO Product VALUES('0003','运动T恤','衣服',4000,2800,NULL);
INSERT INTO Product VALUES('0004','菜刀','厨房用具',3000,2800,'2009-09-20');
INSERT INTO Product VALUES('0005','高压锅','厨房用具',6800,5000,'2009-01-15');
INSERT INTO Product VALUES('0006','叉子','厨房用具',500,NULL,'2009-09-20');
INSERT INTO Product VALUES('0007','擦菜板','厨房用具',880,790,'2008-04-28');
INSERT INTO Product VALUES('0008','圆珠笔','办公用品',100,NULL,'2009-11-11');

-- 练习题2. 编写一条SQL语句，从Product（商品）表中选出“登记日期(regist_date)在2009年4月28日之后”的商品。查询结果要包含product_name和regist_date两列。

SELECT product_name 商品名称, regist_date 注册日期 FROM Product
WHERE regist_date >'2009-04-28';

-- 练习题3. 请写出一条SELECT 语句，从Product表中选取出满足“销售单价打九折之后利润高于100元的办公产品和厨房用具”条件的记录。查询结果要包括product_name列、product_type列以及销售单价打九折之后的利润(别名设定为profit).

SELECT product_name 商品名称, product_type 商品类别, sale_price*0.9-purchase_price profit FROM Product
WHERE sale_price*0.9-purchase_price >100 AND product_type IN ('办公用品','厨房用具');

-- 练习题4. 筛选出sale_price比purchase_price高出500元及以上的商品的product_name,sale_price,purchase_price。

SELECT product_name 商品名称, sale_price 销售价格, purchase_price 进货价格 FROM Product
WHERE sale_price - purchase_price >= 500;

-- 练习题5.将所有销售价格在1000到4000之间的所有商品的信息打印出来。

SELECT * FROM Product
WHERE sale_price BETWEEN 1000 AND 4000;

-- 练习题6.找出所有销售价格大于等于4000的商品并按照进货价格降序排列。

SELECT * FROM Product
WHERE sale_price>=4000
ORDER BY purchase_price DESC;

-- DROP TABLE product;