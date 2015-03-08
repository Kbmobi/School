<!--
Lab Number -- 2
Program Name if applicable -- Lab2
Author name and email address - Keegan Bailey, kbailey.v@gmail.com
Date of submission - 1 / 16 / 2013
Time estimated to complete the lab - 4 hours
Actual time taken to complete the lab - the whole lab, not individual parts - 4ish hours
A description of the program - 	1st = basic "hello world" PHP and uses $_GET and you must use, 
								and you must use quary string eg: lab2-1.php?name=foobafizzle 
								to get it to display your name.
								
								2nd = crappy calculator that uses $_POST; just fill in the blanks.
								
A description of any files/networks/data/html required to run the program if applicable: contains 4 files
																						 lab2.html
																						 lab2-1.php
																						 lab2-2.html
																						 lab2-2.php
																						 
																						 Internet may be required, maybe..
-->
<?php
//set form values to variables
$val1 = $_POST['val1'];
$val2 = $_POST['val2'];
$op = $_POST['op'];

//create an array with all possible answer
$answer = array('+' => '$val1 + $val2', 
		'-' => '$val1 - $val2',
		'/' => '$val1 / $val2',
		'*' => '$val1 * $val2',
		'**' => 'pow($val1, $val2)');

//Evauate the array with the correct string in it, and assign it to a variable.
$answer = eval("echo $answer[$op];");
		
//print the selected values
echo " = ". $val1 . $op . $val2;
echo $answer;

//Create a link to go back to the form.
echo '<br><a href="http://deepblue.cs.camosun.bc.ca/~cst228/comp170/lab2-2.html">Click here to do another calculation</a>';
echo '<br><a href="lab2.html">Main Page</a></br>';
?>