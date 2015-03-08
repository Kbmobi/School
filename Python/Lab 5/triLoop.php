<!--
    line = 1
    blank = n/2
    img = 1
    while line <= n/2+1:
        print 'triEmpty'*blank,'triSmall'*img,'triEmpty'*blank
        blank -= 1
        img += 2
        line += 1 -->
		
<?php
$n = $_POST['number'];

$blank = $n / 2;
$img = 1;
$line = 1;

$tri = <img src="triSmall.png">
$empty = <img src="triEmpry.png">

while(line <= n/2+1) {
	echo '$empty * $blank' . '$tri * $img' . '$empty * $blank' . '<br>';
	$blank -= 1
	$img += 2
	$line += 1
}

?>		