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
<html>
<head><title>lab 2 -- Part 1</title></head>
<body>
<?php
//Setting variable for todays date and time. 
//I used escapes because I have never used them within PHP before, so 
//I decided to use them in here.
$today = date("\T\h\e \c\u\\r\\r\e\\n\\t \d\a\\t\e \& \\t\i\m\e \i\s\: Y-m-d H:i"); 

//Sets a variable to be used within the horizonal like html tag to ajust the width
//based off the current hour of the day.
//the "* 800 / 24" is to makes it actually fill a bar in noticable increments, rather then just
//max out at 24px 
$width = date("H") * 800 / 24;

//Basic variables with HTML tags and text within them
//Only created for expermientation with how PHP works
$br = "<br>";
$helloWorld = "<h1>Hello World!</h1>";

//Masterfully used deprecated HTML attributes to modify horizontal lines (reference back to $width comments)
//first one is a unchangeable horizontal line
//second one is a changeable line that uses the variable $width, and it also blue.
$horizontalLine = "<hr width='800' align='left'>";;
$blueLine = "<hr width='$width' color='#0000FF' size= '15' align='left'>";

//Prints Hello World! in header 1 font size.
echo $helloWorld;

//Print statement using a query string
echo "Welcome " . htmlspecialchars($_GET["name"]) . "!" . $br;

//Prints todays date
echo $today;

//Show horizontal lines that fill as day's hours progress
echo $horizontalLine . $blueLine . $horizontalLine;

//Print Browser the user is using on the screen
echo $_SERVER["HTTP_USER_AGENT"];

//link back to main page
echo $br . "<a href='lab2.html'>Main Page</a>";
?>
</body></html>