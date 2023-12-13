# Write your MySQL query statement below
select unique_id, name from EmployeeUNI as u right join Employees as e on u.id = e.id