create database Employee;
use Employee;
create table Emp (
Emp_id int primary key,
Emp_name varchar(100),
salary int,
experience int,
joining date
);
insert into Emp (Emp_id, Emp_name, salary, experience, joining)
values (100, 'kiran', 50000, 3, '2022-07-17');
select * from Emp;
update Emp set salary = 60000 where Emp_id = 100;
select * from Emp;
insert into Emp (Emp_id, Emp_name, salary, experience, joining)
values (101, 'madesh', 5000, 1, '2024-07-17');
select * from Emp;
delete from Emp where Emp_id = 101;
select * from Emp;
