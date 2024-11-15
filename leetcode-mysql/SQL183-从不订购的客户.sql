# Customers 表：
# +----+-------+
# | Id | Name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders 表：
# +----+------------+
# | Id | CustomerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# 例如给定上述表格，你的查询应返回：
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+


select Name as Customers from Customers as c
where c.Id not in(select CustomerId from Orders)

# 2
select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);