<?php
/*
Lab Number: 8
Program Name if applicable: Lab8
Author name and email addres: Keegan Bailey, kbailey.v@gmail.com
Date of submission: 3/2/2013
Time estimated to complete the lab: 6 hours
Actual time taken to complete the lab: 8 hours
A description of the program: Use MVC to make SQL querys
required to run the program if applicable: controller.php, model.php, toXML.php, view.xsl, sq_connect.inc
*/
//Model Module
function sqlsearch($select, $from, $where) {
	$ds = $select;
	$df = $from;

	//set up regex for input checks	
	$notCoolBro = '/(\bselect\b|\bfrom\b|\bwhere\b|\binput\b|\bdrop\b|\btruncate\b|;)/i';

	preg_match($notCoolBro, $ds, $sCheck);
	preg_match($notCoolBro, $df, $fCheck);	

	
	//if a match is found, return out and print error msg. If no matches are found, strip any slashes, and assign new variable.	
	if ($sCheck != NULL ) {
		die('bad');
	} else {
		$s = stripslashes($ds);
	}

	if ($fCheck != NULL ) {
		die('bad');
	} else {
		$f = stripslashes($df);
	}

	//Check to see if there WHERE field was used.
	if($where != NULL){
		$dw = $where;

		//more input checking and assembling of query based off of where verb.		
		preg_match($notCoolBro, $dw, $wCheck);		

		if ($wCheck != NULL) {
			die('bad');
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
	$result = mysql_query($query, $LinkID);
	
	mysql_data_seek($result, 0);
	// Fetch a row with the column labels
	$x = mysql_fetch_assoc($result);
	$resultArray = array();
	$one = array();
	$two = array();
			
	foreach($x as $x=>$k) {
		$one[] = $x;
		$two[] = $k;
	}
	
	$resultArray[] = $one;
	$resultArray[] = $two;

	while ($x = mysql_fetch_row($result)) {
		$one = array();
		foreach($x as $x=>$k) {
			$one[] = $k;
		}
	$resultArray[] = $line;
	}
   
// Create the output array
    $list['name']     = "Lab 8";
    $list['outTitle'] = "Output";
    $list['outValue'] = $resultArray;

// Create the input array
    $list['inTitle']  = "Input";
    $list['inValue']['select']  = $select;
    $list['inValue']['from']  = $from;
    $list['inValue']['where']  = $where;

// Return the array
    return $list;
  }
?>