<!--
Lab Number -- 3
Program Name if applicable -- Lab3
Author name and email address - Keegan Bailey, kbailey.v@gmail.com
Date of submission - 1 / 22 / 2013
Time estimated to complete the lab - 6 hours
Actual time taken to complete the lab - 4ish hours
A description of the program - 	1st = Break down an apache log file entry
								And diplay ip address, connection status code
								bytes transfered.
								
								2nd = replace words within a string.
								
Things required to run the program: lab3.html, lab3-1.html, lab3-1.php, lab3-2.php																
-->
<?php
//assign the input text to a variable. 
$log = $_POST['log'];
$help = "<a href='http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10'>Look up Error Here!</a>"; 

//checks input by striping all special characters out (ex: < >)
$clean = htmlspecialchars(strip_tags(trim($log)), ENT_QUOTES);

//checks the length of the string size, and exits if the size is to big or small
if (strlen($clean) > 300 or strlen($clean < 1)) {
	echo $clean;
	echo "<br>Input Error - Something was wrong with your input. It may have included some odd special characters.";
	echo "<hr><a href='lab3-1.html'>Click here to try another</a><br><a href='lab3.html'>Click here to head back to main Page</a>";
	exit;
}

//regex that matches 0.0.0.0 through 255.255.255.255 within the apache log.
$ip = '/\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b/';
//pull the ip address out of the log, and stick it in an array.
preg_match($ip, $log, $match1);

//pull the connection status code, and bytes transfered out of the log. 
$info = '/\"+\s+\d{3}+\s+\d{1,}+\s+\"/';

//Create an array for input checking
$result = preg_match_all($ip, $log, $result);
$result2 = preg_match_all($info, $log, $result2);

//Check to see if the 2 arrays are empty
if ($result == 0 | $result2 == 0) {
	//error message if it did not work
	echo $log . " did not seem to parse properly, please try again";
	echo "<hr><a href='lab3-1.html'>Click here to try another</a><br><a href='lab3.html'>Click here to head back to main Page</a>";
} else {
	//good message if it did
	preg_match($info, $log, $match2);
	$str = $match2[0];

	//put pulled info into an split array 
	$split = '/\"|\s/';
	$info2 = preg_split($split, $str);

	//assign array to variables
	$code = $info2[2]; 
	$byte = $info2[3];

	//print IP address.
	echo "<br>The IP address is: " . $match1[0] . "<br><br><br>";

	//Check to see if the code is an error 400/500.
	if ($code >= 400) {
		//if error, say so, and link to explanation.
		echo "<br>Connection Failed! <br>Code: ".$code."<br> Bytes Transmitted: 0 <br>".$help;
	} else {
		//if not error, say so, and show bytes transmitted.
		echo "<br>Connection Good! <br>Code: ".$code."<br> Bytes Transmitted: ".$byte;
	}
	echo "<hr><a href='lab3-1.html'>Click here to try another</a><br><a href='lab3.html'>Click here to head back to main Page</a>";
}

?>