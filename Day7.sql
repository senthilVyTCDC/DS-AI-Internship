create database datascience_projects;
use datascience_projects;

create table Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    domain VARCHAR(50),
    type VARCHAR(50),   
    start_date DATE,
    end_date DATE,
    status VARCHAR(30)
);

insert into Projects (project_id, project_name, domain, type, start_date, end_date, status)
values (101 ,'Diabetic Retinopathy Detection', 'Healthcare', 'Computer Vision', '2025-07-15', '2025-08-15', 'In Progress');

Select * from Projects;

update Projects set status = 'Completed' WHERE project_id = 101;

select * from Projects;

insert into Projects (project_id, project_name, type, status)
VALUES (102, 'Iris Flower Dataset', 'classification', 'in-progress');

select * from Projects;

delete from Projects where project_id = 102;

select * from Projects;





