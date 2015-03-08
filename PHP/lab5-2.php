<html>
	<head>
		<title>Lab5-2 Keegan Bailey</title>
	</head>
<body>
<!-- Lab Number -- 5
Program Name if applicable -- Lab5
Author name and email address - Keegan Bailey, kbailey.v@gmail.com
Date of submission - 2 / 8 / 2013
Time estimated to complete the lab - 6 hours
Actual time taken to complete the lab - 8->10ish hours
A description of the program - 	1st = complete querys
								
								2nd = make your own querys.
								
Things required to run the program: lab5.html, lab5-1.php, lab5-2.php -->
<img src="http://hal.cs.camosun.bc.ca/~weston/comp155/ERD_HR.gif">
<form action="<?php $_SERVER['PHP_SELF'] ?>" method="post" >
	<fieldset style="width:575px;">
		<legend>Cool stuff here</legend>
		<label>SELECT</label>
			<input type = 'text' name = 'select' required placeholder = 'example: *' style="width:500px; height:40px; 
							background-color:black; color:lime; 
									
							-webkit-border-radius:5px;
							-moz-border-radius:5px;
							-o-border-radius:5px;
							-ms-border-radius:5px;
							border-radius:5px;
									
							-moz-transition:padding .25s;
							-webkit-transition:padding .25s;
							-o-transition:padding .25s;
							transition:padding .25s;}" /><br>
		<label>FROM &nbsp </label>
			<input type = 'text' name = 'from' required placeholder = 'example: employees' style="width:500px; height:40px; 
							background-color:black; color:lime; 
									
							-webkit-border-radius:5px;
							-moz-border-radius:5px;
							-o-border-radius:5px;
							-ms-border-radius:5px;
							border-radius:5px;
									
							-moz-transition:padding .25s;
							-webkit-transition:padding .25s;
							-o-transition:padding .25s;
							transition:padding .25s;}" /><br>
		<label>WHERE</label>
			<input type = 'text' name = 'where' style="width:500px; height:40px; 
							background-color:black; color:lime; 
									
							-webkit-border-radius:5px;
							-moz-border-radius:5px;
							-o-border-radius:5px;
							-ms-border-radius:5px;
							border-radius:5px;
									
							-moz-transition:padding .25s;
							-webkit-transition:padding .25s;
							-o-transition:padding .25s;
							transition:padding .25s;}" /><br> 
	<input value="Query!" type="submit" />
	</fieldset>
</form>



<?php
//check to see if something has been posted by the form
if(isset($_POST['select'])){

//assign posts to variables
	$ds = $_POST['select'];
	$df = $_POST['from'];
	$hci = "<hr><a href='http://deepblue.cs.camosun.bc.ca/~cst228/comp170/lab5.html'>Return to Main Page</a>";
	
//set up regex for input ghetto checks	
	$notCoolBro = '/(\bselect\b|\bfrom\b|\bwhere\b|\binput\b|\bdrop\b|\btruncate\b|;)/i';

	preg_match($notCoolBro, $ds, $sCheck);
	preg_match($notCoolBro, $df, $fCheck);	

	
//if a match is found, return out and print error msg. If no matches are found, strip any slashes, and assign new variable.	
	if ($sCheck != NULL ) {
		echo "Got a dirty select".$hci;
		return;
	} else {
		$s = stripslashes($ds);
	}

	if ($fCheck != NULL ) {
		echo "Got a dirty from".$hci;
		return;
	} else {
		$f = stripslashes($df);
	}

//Check to see if there WHERE field was used.
	if($_POST['where'] != NULL){
		$dw = $_POST['where'];

		
//more input checking and assembling of query based off of where verb.		
		preg_match($notCoolBro, $dw, $wCheck);		

		if ($wCheck != NULL) {
			echo "Got a dirty where dude".$hci;
			return;
		} else {
			$w = stripslashes($dw);
		}	

		$query = 'select '.$s.' from '.$f.' where '.$w.';';
	
		echo $query;
	} else {
		$query = 'select '.$s.' from '.$f.';';

		echo $query;
	}
	
	// Connect to the MySQL server.
	$LinkID = mysql_connect("localhost", "170user", "phphasclass");

	// Die if no connect
	if (!$LinkID) {
		die('Could not connect: ' . mysql_error());
	}

	// Choose the DB and run a query.
	mysql_select_db("comp170", $LinkID);
	$result = mysql_query( $query ,$LinkID);
	
	// Display the results.
	print 	"<h3>Result</h3>
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
		echo "</tr></table><br><br><br>".$hci;
	}
?>
</body>
</html>