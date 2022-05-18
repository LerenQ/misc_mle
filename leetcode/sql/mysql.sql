/*595 big_country */
select name, population, area 
from World 
where area > 3000000
union
select name, population, area
from World
where population > 25000000;

/*#627 swap_salary */
/*
UPDATE salary
SET sex=IF(sex='m', 'f', 'm');
*/

/*
update salary
set 
    sex = CASE sex
    when 'm' Then 'f'
    else 'm'
    END;
*/

update salary
set sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex));

/*#620 Not Boring Movies */
select *
from Cinema
where mod(id,2) = 1 and description != 'boring'
order by rating desc;

/*#182 Duplicate Emails */
select email
from Person
group by email
having count(*) > 1;

/*#175. Combine Two Tables */
select p.firstName, p.lastName, a.city, a.state
from Person as p
left join Address as a
on p.personID = a.personID

/*#181. Employees Earning More Than Their Managers */
select e1.name as Employee
from Employee as e1
inner join Employee  as e2
on e1.managerID = e2.id
where e1.salary > e2.salary;

/*#183. Customers Who Never Order */
select c.name as Customers
from Customers as c
left join Orders as o
on c.id = o.customerID
where o.id is Null;

/*#596. Classes More Than 5 Students */
select class
from Courses
group by class
having count(distinct student) >= 5;

/*#176. Second Highest Salary */
select(
    select distinct salary
    from Employee
    order by salary desc
    limit 1 offset 1
    ) as SecondHighestSalary 

