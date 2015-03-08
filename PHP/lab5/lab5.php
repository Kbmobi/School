<html><head><title>Test MySQL</title></head><body>
<?php

// Connect to the MySQL server.
$LinkID = mysql_connect("localhost", "170user", "phphasclass");

// Die if no connect
if (!$LinkID) {
	die('Could not connect: ' . mysql_error());
}

// Choose the DB and run a query.
mysql_select_db("comp170", $LinkID);
$result = mysql_query( "select * from jobs" ,$LinkID);

// Display the results.
print "Results<br>";
if ($result) {
	while ($x=mysql_fetch_row($result)) {
		echo "$x[0], $x[1], $x[2], $x[3]<br>\n";
		}
		?>
		<p>
		<?php
	
		// Reset the result pointer and display again in a table with titles.
		mysql_data_seek ($result, 0);
	
		// Fetch a row with the column labels
		$x=mysql_fetch_assoc($result);
	
		// Print the column labels
		print "<table border=1><tr><b>";
		foreach (array_keys($x) as $k) {
			print "<td>$k</td>";
			}
		print "</tr><tr>";
	
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
?>
</tr></table></body></html>
