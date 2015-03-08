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
require_once "model.php";
require_once "toXML.php";

//check to see if something has been posted by the model
if(isset($_POST['select'])) {
	$select = $_POST['select'];
	$from = $_POST['from'];
	$where = $_POST['where'];
  } else {
	$select = "*";
	$from = "jobs";
	$where = "lower(job_id) = 'ad_pres'";
  }	
	
// Pass it to the model
$things = sqlsearch($select, $from, $where);

// Convert data from the model to xml
$xml = toXML($things);

// Output the xml to the view;
header('Content-Type: text/xml');
echo $xml; 	
?>