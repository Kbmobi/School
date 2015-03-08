<html>
<head><title>Dec to Bin</title></head>
<body>
<?php
//Query string to get your number
$dec = htmlspecialchars($_GET["x"]);

//Convert that number to binary
$bin = decbin($dec);

//Print that bitch.
echo $dec . " in decimal = " . $bin . " in binary!";
?></body></html>