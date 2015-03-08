<?php
//assign the input text to a variable. 
$log = $_POST['log'];
$help = "<a href='http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10'>Look up Error Here!</a>"; 

//regex that matches 0.0.0.0 through 255.255.255.255 within the apache log.
$ip = '/\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b/';
//pull the ip address out of the log, and stick it in an array.
preg_match($ip, $log, $match1);

//pull the connection status code, and bytes transfered out of the log. 
$info = '/\"+\s+\d{3}+\s+\d{1,}+\s+\"/';
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
	echo "<br>Connection Failed! <br>Code: ".$code."<br> Bytes Transmitted: 0".$help;
} else {
	//if not error, say so, and show bytes transmitted.
	echo "<br>Connection Good! <br>Code: ".$code."<br> Bytes Transmitted: ".$byte;
}
echo "<hr><a href='lab3-1.html'>Click here to try another</a><br><a href="lab3.html">Click here to head back to main Page</a>";
?>
