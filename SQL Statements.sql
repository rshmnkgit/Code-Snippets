
select id, departments.name from departments where EXISTS 
(select department_id from sales where 
 sales.department_id = departments.id and price>98)

select id, departments.name from departments where id IN
(select department_id from sales where 
 sales.department_id = departments.id and price>98)

/*    Postgres   */
select CONCAT(prefix,' ',first,' ',last,' ',suffix) as title from names  
SELECT concat_ws(' ', prefix,first,last,suffix) AS title FROM names

SELECT FLOOR(number1) AS number1, CEIL(number2) AS number2, ROUND(number1) from decimals
/*  FLOOR - Round down to the nearest integer
    CEIL/CEILING - Round up to the nearest integer  */

/*   SQL Server  */
Select prefix +' '+first+' '+last+' '+suffix as title from names   