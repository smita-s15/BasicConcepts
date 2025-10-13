SELECT *  Customers c INNER JOIN Orders o 
ON c.customer_id==o.customer_id ;
select * from Customers
select first_name , last_name , country from Customers
select * from Customers where country="USA"
select * from Customers where age < 28
select count(*) as customer_count, first_name, last_name from Customers group by first_name, last_name;
select count(*) as count from Customers where country="USA"
select * from Customers ORDER BY last_name ASC LIMIT 3
select AVG(age) from Customers
select * from  Customers c  INNER JOIN Orders o ON c.customer_id == o.customer_id
select * from  Customers c  LEFT JOIN Orders o ON c.customer_id == o.customer_id
select * from Customers as c JOIN Orders as o ON c.customer_id = o.customer_id  
select c.first_name, c.last_name from Customers c join Orders o ON c.customer_id = o.customer_id where o.amount>(select avg(amount) from Orders)

select c.first_name , c.last_name from Customers as c JOIN Orders as o ON c.customer_id = o.customer_id where o.amount > (select avg(amount) from Orders )
INSERT INTO Customers VALUES(6,"SMITA", "SHINDE",26,"INDIA")


--ALTER TABLE Customers DROP COLUMN last_name

ALTER TABLE Customers ALTER COLUMN age string
ALTER TABLE Customers ADD customer_email string