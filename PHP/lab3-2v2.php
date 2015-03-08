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
--><?php
//take user input and place it in a variable.
$str = $_POST['str'];
//get regex key words, and put them in a variable.
$keyWords = '/(\bfear\b|\bwaddy\b|\bgear\b|\bfiasco\b|\bfobbing\b)/i';
//get replacement word, and put that in a varable as well. I like turtles.
$repWord = '1969-10-29';

//use the replace function to take the words out of the string, and replace them with the replacement word.
//Then assign that to a new variable
$newStr = preg_replace($keyWords, $repWord, $str);

//Print out new string for user to read, and probably get confused.
echo "<h1>Your new string!</h1>"."<p>".$newStr."</p>";

//give info on what that date is actually important.
echo '<h1>Arpanet (1969-10-29) -- The start of the Internet!</h1><br><br><iframe width="420" height="315" src="http://www.youtube.com/embed/CRD7TnJvIN8" frameborder="0" allowfullscreen></iframe>';
echo "<hr><a href='lab3-1.html'>Click here to try another</a><br><a href='lab3.html'>Click here to head back to main Page</a>";

?>