<html>
<head><title>lab 2 -- Part 1</title></head>
<body>
<?php
/*
Lab 2 part 1

Write a php program that will run on deepblue and display:

- Hello World
- your name as entered as a query string
- the current time in SI standard time (yyyy-mm-dd hh:mm)
- a horizontal bar scaled to the hour.
- the type of Web Browser that accessed the php program. For example */

//Setting Variables
$today = date("\T\h\e \c\u\\r\\r\e\\n\\t \d\a\\t\e \& \\t\i\m\e \i\s\: Y-m-d H:i"); 
$width = date("H") * 800 / 24; // multiplying the hour by 10, so you an actually see a difference.
$br = "<br>";
$helloWorld = "<h1>Hello World!</h1>";
$horizontalLine = "<hr>";
$blueLine = "<hr width='$width' color='#0000FF' size= '15' align='left'>";

//Prints
echo $helloWorld;
echo "Welcome " . htmlspecialchars($_GET["name"]) . "!" . $br;
echo $today;
echo $horizontalLine . $blueLine . $horizontalLine;
echo $_SERVER["HTTP_USER_AGENT"];

?>
</body></html>