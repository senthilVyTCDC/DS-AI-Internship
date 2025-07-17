create database banking_details;
use banking_details;
CREATE TABLE customer_details (
    name VARCHAR(100),
    account_no BIGINT PRIMARY KEY,
    account_balance DECIMAL(10, 2)
);
insert into customer_details(name, account_no, account_balance) values ('Olivia', 546732, 55000.00), 
('Jack', 875435, 10000.00), 
('Steve', 904268, 50000.00);
select * from customer_details;