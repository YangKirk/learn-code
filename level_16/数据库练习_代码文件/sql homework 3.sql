-- 练习题1.请编写一条SELECT语句，求出销售单价(sale_price列)总和大于进货单价(purchase_price列)总和1.5倍的商品种类以及销售总价和进货总价。

SELECT product_type 商品种类, SUM(sale_price) 销售总价, SUM(purchase_price) 进货总价 FROM product
GROUP BY product_type
HAVING SUM(sale_price) > SUM(purchase_price) * 1.5;

-- 练习题2.查找商品表中商品销售价格的平均价、最高价、最低价

SELECT AVG(sale_price) 销售均价, MAX(sale_price) 最高价, MIN(sale_price) FROM product;

-- 练习题3.查找商品表中每种商品的平均售价，并降序显示

SELECT product_type 商品类别, AVG(sale_price) 销售均价 FROM product
GROUP BY product_type
ORDER BY AVG(sale_price) DESC;

-- 练习题4. 查找商品表中按类型统计商品数大于2的商品类型以及商品数

SELECT product_type 商品类型, COUNT(product_type) 商品数量 FROM product
GROUP BY product_type
HAVING COUNT(product_type) > 2;