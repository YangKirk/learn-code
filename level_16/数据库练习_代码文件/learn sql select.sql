USE tmp;
-- *号查询所有列
SELECT * FROM dept;	

-- 选择指定列查询
SELECT deptno, loc FROM dept;

-- 算术表达式查询
SELECT ename, sal, sal+300 FROM emp;

-- 空值查询
SELECT ename, job, comm FROM emp;

SELECT ename NAME, 12*sal+comm "年薪+补助" FROM emp
WHERE ename = 'KING';		-- 包含空值的算法表达式等于空

-- 重命名查询
SELECT ename AS 姓名, sal AS 薪资 FROM emp;
SELECT ename "Name", sal*12 "Annual Salary(年终奖)" FROM emp;	
-- 特殊字或者带空格需要加引号

-- 排除重复查询
SELECT DISTINCT deptno FROM emp;

-- 限制行数查询
SELECT * FROM emp LIMIT 5,6;	-- 从偏移量为5的行开取6行，偏移量为5代表第6行(注意第一行偏移量为0)
SELECT * FROM emp LIMIT 5;	-- 等同于SELECT * FROM emp LIMIT 0,5;
SELECT * FROM emp ORDER BY sal DESC LIMIT 3;	-- 求工资最高的前三个员工信息
SELECT * FROM emp ORDER BY sal DESC LIMIT 3,1;	-- 求工资第四高的员工信息

-- 限制数据条件查询
SELECT * FROM emp WHERE hiredate > '1981-04';
SELECT * FROM emp WHERE ename = 'KING';

-- 条件运算符查询
SELECT ename, sal, comm FROM emp
WHERE sal<=comm;

-- 匹配运算符查询
SELECT ename, sal FROM emp WHERE sal BETWEEN 1000 AND 1500;
SELECT empno, ename, sal, mgr FROM emp WHERE mgr IN (7902,7566,7788);
-- %表视0或多个字符，_表示1个字符
SELECT ename FROM emp WHERE ename LIKE 'S%';	-- S%表示以S开头的字符
SELECT ename FROM emp WHERE ename LIKE '_A%';	-- _A%表示第二个字符为A的字符
-- ISNULL空值条件查询
SELECT ename，mgr FROM emp WHERE mgr IS NULL;
-- 组合条件查询
SELECT empno, ename, job, sal FROM emp
WHERE sal>=1000
AND job='CLERK';
SELECT empno, ename, job, sal FROM emp
WHERE sal>=1100
OR job='CLERK';
SELECT ename, job FROM emp
WHERE job NOT IN ('CLERK','MANAGER','ANALYST');	
-- 运算符运算顺序：比较>NOT>AND>OR
SELECT ename, job, sal FROM emp
WHERE (job='SALESMAN' OR job='PRESIDENT')
AND sal>1500;

-- 排序查询
SELECT ename, job, deptno, hiredate FROM emp
ORDER BY hiredate DESC;		-- 降序排列
SELECT ename, job, deptno, hiredate FROM emp
ORDER BY hiredate ASC;		-- 升序排列
SELECT empno, ename, sal*12 annsal FROM emp
ORDER BY annsal;	-- 使用别名排序

-- 聚合函数查询
SELECT AVG(sal), MAX(sal), MIN(sal), SUM(sal) FROM emp
WHERE job LIKE 'SALES%';
SELECT MIN(hiredate), MAX(hiredate) FROM emp;	-- MIN和MAX也可用于DATE类型数据

-- 聚合分组查询
SELECT COUNT(*) FROM emp WHERE deptno = 30;
SELECT COUNT(comm) FROM emp
WHERE deptno=30;
SELECT AVG(IFNULL(comm,0)) FROM emp;	-- IFNULL函数强制返回包含空值

-- 分组函数查询
SELECT deptno, AVG(sal) FROM emp
GROUP BY deptno;
SELECT deptno, job, sum(sal) FROM emp GROUP BY deptno, job;		-- 多列分组查询

-- 限定分组条件查询
SELECT deptno, max(sal) FROM emp
GROUP BY deptno
HAVING max(sal)>2900;

SELECT job, SUM(sal) PAYROLL FROM emp
WHERE job NOT LIKE 'SALES%'
GROUP BY job
HAVING SUM(sal)>5000
ORDER BY SUM(sal);

-- 子查询
SELECT ename FROM emp
WHERE sal > (SELECT sal FROM emp WHERE empno=7566);

SELECT ename, job
FROM emp
WHERE job=(SELECT job FROM emp
          WHERE empno=7369)
AND sal > (SELECT sal FROM emp
          WHERE empno=7876);

-- 多行子查询
SELECT empno, ename, job, sal FROM emp
WHERE deptno IN (SELECT deptno FROM emp
                WHERE ename='SMITH' OR ename='MILLER');

SELECT empno, ename, job FROM emp
WHERE sal > ANY (SELECT sal
                FROM emp
                WHERE job='CLERK');

SELECT empno, ename, job, sal
FROM emp
WHERE sal > ALL (SELECT AVG(sal)
                FROM emp
                GROUP BY deptno);

-- 子查询中使用聚合函数
SELECT ename, job, sal
FROM emp
WHERE sal=(SELECT MIN(sal)
          FROM emp);

-- HAVING语句中使用子查询结果
SELECT deptno, MIN(sal)
FROM emp
GROUP BY deptno
HAVING MIN(sal) > (SELECT MIN(sal)
                  FROM emp
                  WHERE deptno=20);

-- 多表连接查询
SELECT emp.empno, emp.ename, emp.deptno, dept.deptno, dept.loc
FROM emp INNER JOIN dept
ON emp.deptno = dept.deptno;

SELECT emp.empno, emp.ename, emp.deptno, dept.deptno, dept.loc
FROM emp, dept
WHERE emp.deptno=dept.deptno;

SELECT e.empno, e.ename, e.deptno, d.deptno, d.loc
FROM emp e, dept d
WHERE e.deptno=d.deptno;

SELECT emp.empno, emp.ename, emp.deptno, dept.deptno, dept.loc
FROM emp INNER JOIN dept
ON emp.deptno=dept.deptno AND emp.ename='KING';

SELECT emp.ename, dept.deptno
FROM dept LEFT JOIN emp
ON emp.deptno=dept.deptno;