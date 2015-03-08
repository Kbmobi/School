<html><head><title>Lab5-1 Keegan Bailey</title></head><body>
<!-- Lab Number -- 5
Program Name if applicable -- Lab5
Author name and email address - Keegan Bailey, kbailey.v@gmail.com
Date of submission - 2 / 8 / 2013
Time estimated to complete the lab - 6 hours
Actual time taken to complete the lab - 8->10ish hours
A description of the program - 	1st = complete querys
								
								2nd = make your own querys.
								
Things required to run the program: lab5.html, lab5-1.php, lab5-2.php -->
<?php
print 	"<h1>Lab 5 -- Part 1</h1>
		<p> Keegan Bailey</p>";
		
// Connect to the MySQL server.
$LinkID = mysql_connect("localhost", "170user", "phphasclass");

// Die if no connect
if (!$LinkID) {
	die('Could not connect: ' . mysql_error());
}

// Choose the DB and run a query.
mysql_select_db("comp170", $LinkID);
$result = mysql_query( "
SELECT employees.last_name AS \"Last Name\", 
	jobs.job_title AS \"Job\", 
	departments.department_id AS \"Depo#\", departments.department_name AS \"Department Name\"
FROM employees, departments, jobs, locations
WHERE departments.department_id = employees.department_id
AND employees.job_id = jobs.job_id
AND departments.location_id = locations.location_id
AND UPPER(locations.city) = 'SOUTHLAKE';
 " ,$LinkID);

// Display the results.
print 	"<h3>Question #1</h3>
		<p>Write a query to display the last name, job, department number, and department name for all employees who work in Southlake, Texas. 
		Be sure to handle case when checking that the city is Southlake. 
		(Note: in this case, you may assume that the only \"Southlake\" is in Texas.)
		<br>------<br>";
if ($result) {
		echo "<p>";
		// Reset the result pointer and display again in a table with titles.
		mysql_data_seek ($result, 0);
	
		// Fetch a row with the column labels
		$x=mysql_fetch_assoc($result);
	
		// Print the column labels
		print "<table border=1><tr><b>";
		foreach (array_keys($x) as $k) {
			print "<td>$k</td>";
			}
		print "</b></tr><tr>";
	
		// Print the values for the first row
		foreach ($x as $v) {
			print "<td>$v</td>";
		}
		print "</tr><tr>";
	
		// Print the rest of the rows.
		while ($x=mysql_fetch_row($result)) {
			foreach ($x as $v) {
				print "<td>$v</td>";
			}
			print "</tr><tr>";
		}
	}
echo "</tr></table><br><br><br>";

$result = mysql_query( "
SELECT e.last_name AS \"Lst Nm\",
	ifNULL(d.department_name, 'None') AS \"Dpt Nm\"
FROM employees e
LEFT OUTER JOIN departments d
ON d.department_id = e.department_id
WHERE UPPER(e.last_name) LIKE 'G%';
 " ,$LinkID);

// Display the results.
print 	"<h3>Question #2</h3>
		<p>Write a query that will list all of the employees (last names), whose last name starts with 'G' 
		(be sure to handle case), and the departments (give the name) to which they belong. Include all employees 
		who have not yet been assigned to any department. (Note: do not use IS NULL or IS NOT NULL in your query.) 
		<br>------<br>";
if ($result) {
		echo "<p>";
		// Reset the result pointer and display again in a table with titles.
		mysql_data_seek ($result, 0);
	
		// Fetch a row with the column labels
		$x=mysql_fetch_assoc($result);
	
		// Print the column labels
		print "<table border=1><tr><b>";
		foreach (array_keys($x) as $k) {
			print "<td>$k</td>";
			}
		print "</b></tr><tr>";
	
		// Print the values for the first row
		foreach ($x as $v) {
			print "<td>$v</td>";
		}
		print "</tr><tr>";
	
		// Print the rest of the rows.
		while ($x=mysql_fetch_row($result)) {
			foreach ($x as $v) {
				print "<td>$v</td>";
			}
			print "</tr><tr>";
		}
	}
echo "</tr></table><br><br><br>";

$result = mysql_query( "
SELECT e.last_name AS \"Employee\", 
	e.employee_id AS \"Emp#\",
	m.last_name AS \"Manager\",
	m.manager_id AS \"Mgr#\"
FROM employees e, employees m
WHERE e.manager_id = m.employee_id
AND UPPER(e.last_name) LIKE 'G%';
 " ,$LinkID);

// Display the results.
print 	"<h3>Question #3</h3>
		<p>Display the employee last name and employee number along with their manager’s last name and manager number (in other 
		words the manager's employee id) for all employees whose last name begins with 'G' (be sure to handle case). Label the 
		columns Employee, Emp#, Manager, and Mgr#, respectively (note the use of upper and lower case). 
		<br>------<br>";
if ($result) {
		echo "<p>";
		// Reset the result pointer and display again in a table with titles.
		mysql_data_seek ($result, 0);
	
		// Fetch a row with the column labels
		$x=mysql_fetch_assoc($result);
	
		// Print the column labels
		print "<table border=1><tr><b>";
		foreach (array_keys($x) as $k) {
			print "<td>$k</td>";
			}
		print "</b></tr><tr>";
	
		// Print the values for the first row
		foreach ($x as $v) {
			print "<td>$v</td>";
		}
		print "</tr><tr>";
	
		// Print the rest of the rows.
		while ($x=mysql_fetch_row($result)) {
			foreach ($x as $v) {
				print "<td>$v</td>";
			}
			print "</tr><tr>";
		}
	}
echo "</tr></table><br><br><br><hr><a href='http://deepblue.cs.camosun.bc.ca/~cst228/comp170/lab5.html'>Return to Main Page</a>";
?>
</body></html>
