<!--
    line = 1
    blank = n/2
    img = 1
    while line <= n/2+1:
        print ' '*blank,'triSmall'*img,' '*blank
        blank -= 1
        img += 2
        line += 1 -->
		
<?php
$dn = $_POST['val1'];
$n = htmlspecialchars(strip_tags(trim($dn)), ENT_QUOTES);

if($n <= 0 | $n >= 10 || $n % 2 != 1 ){
	echo "Your number is even, too high, too low, not a number, or you're stupid.<hr><a href='triLoop.html'>Try Again?</a>";
	
} else {
$tri = '<img src="triSmall.png">';
$empty = '<img src="triEmpty.png">';

$blank = intval($n / 2);
$img = 1;
$line = 1;

while($line <= intval($n / 2 + 1)) {
	$whiteSpace = str_repeat("$empty", $blank);
	$images = str_repeat("$tri", $img);

	echo $whiteSpace . $images . $whiteSpace . '<br>';
	$blank -= 1;
	$img += 2;
	$line += 1;
	}
}
?>	