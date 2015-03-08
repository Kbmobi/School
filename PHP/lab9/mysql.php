<?php
/*
Lab Number: 9
Program Name if applicable: Lab9
Author name and email addres: Keegan Bailey, kbailey.v@gmail.com
Date of submission: 3/2/2013
Time estimated to complete the lab: 6 hours
Actual time taken to complete the lab: 10 minutes (all heavy lifting was done in lab5)
A description of the program: Use Ajax to make SQL querys
required to run the program if applicable: lab9.html, jquery.js, mysql.php
*/
//assign posts to variables
$ds = $_POST['select'];
$df = $_POST['from'];
	
//set up regex for input ghetto checks	
$notCoolBro = '/(\binput\b|\bdrop\b|\btruncate\b|;)/i';

preg_match($notCoolBro, $ds, $sCheck);
preg_match($notCoolBro, $df, $fCheck);	

	
//if a match is found, return out and print error msg. If no matches are found, strip any slashes, and assign new variable.	
if ($sCheck != NULL ) {
	die('made it to select');
} else {
	$s = stripslashes($ds);
}

if ($fCheck != NULL ) {
	die('made it to from');
} else {
	$f = stripslashes($df);
}

//Check to see if there WHERE field was used.
if($_POST['where'] != NULL){
	$dw = $_POST['where'];
		
	//more input checking and assembling of query based off of where verb.		
	preg_match($notCoolBro, $dw, $wCheck);		

	if ($wCheck != NULL) {
		die('made it to where');
	} else {
		$w = stripslashes($dw);
	}	

$query = 'select '.$s.' from '.$f.' where '.$w.';';	
} else {
$query = 'select '.$s.' from '.$f.';';
}
	
// Connect to the MySQL server.
include '../../../sq_connect.inc';

// Die if no connect
if (!$LinkID) {
	die('Could not connect: ' . mysql_error());
}

// Choose the DB and run a query.
mysql_select_db("comp170", $LinkID);
$result = mysql_query( $query ,$LinkID);
	
// Display the results.
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
echo "</tr></table>";
?>