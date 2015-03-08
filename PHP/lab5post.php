<html>
	<head>
		<title>Lab5 forum post</title>
	</head>
<body>
<form action="<?php $_SERVER['PHP_SELF'] ?>" method="post" >
	<fieldset style="width:575px;">
		<legend>What number am I thinking of? (between 1 and 100)</legend>
			<input type = 'text' name = 'number' required placeholder = 'example: 7' style="width:500px; height:40px; 
							background-color:black; color:lime; 
									
							-webkit-border-radius:5px;
							-moz-border-radius:5px;
							-o-border-radius:5px;
							-ms-border-radius:5px;
							border-radius:5px;
									
							-moz-transition:padding .25s;
							-webkit-transition:padding .25s;
							-o-transition:padding .25s;
							transition:padding .25s;}" />
	<input value="Query!" type="submit" />
	</fieldset>
</form>

<?php

if(isset($_POST['number'])){
	
	//set vars
	$myGuess = 32;
	$hci = "<hr><a href='http://deepblue.cs.camosun.bc.ca/~cst228/comp170/lab5post.php'>Try Again?</a>";

	//check to see if it's a number

	if (is_int((int)$_POST['number'])) {
    		$cleanInput = $_POST['number'];
		} else {
  	  	echo "is not an integer\n";
		echo $hci;
		return;
		}

	//start testing input against guess
	if($cleanInput > 0){
	  if($cleanInput < 101){ 
		if($cleanInput == $myGuess){
			echo "Holy shit, you did it (you're a cheater)";
			}

		elseif($cleanInput > $myGuess){
			echo "Your guess is too high!";
			}		

		elseif($cleanInput < $myGuess){
			echo "Your guess is too low";
			}
		} else {
			echo "You have input an invalid number";
			}
		}
		echo $hci;
	}
?>