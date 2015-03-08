<?php
$pswd = $_POST['pswd'];

$regex = '/\A(?=[-_a-zA-Z0-9]*?[A-Z])(?=[-_a-zA-Z0-9]*?[a-z])(?=[-_a-zA-Z0-9]*?[0-9])\S{6,}\z/';
$result = preg_match_all($regex, $pswd, $result);

if ($result == 0) {
	echo $pswd . " is a <span style='color:red;'>bad password</span>";
} else {
	echo $pswd . " is <span style='color:green;'>good</span>";
}
echo "<hr><a href='pswd.html'>Click here to try another</a>";
?>