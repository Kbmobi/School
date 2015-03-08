<?php Calculate the hull speed of a displacement hull given the length at waterline.?>
<?php
/* 
Calculate the hull speed of a displacement hull given the length
of the vessel at the water line.
Deid Reimer 
reimer@camosun.bc.ca
2009-02-04
*/

// Check that the supplied input is numeric. If so do the calculation
// else print an error message and exit. I know if you are just doing lab 2, if is still a secret, but
// pretend you know what it means.

// Pick up the boat length from $_post array. It will have the index of length as that is what we named it in the html form.
// If the value is numeric - do the calculation and display. If not, bitch!
if (is_numeric($_POST['length'])) {
	print sqrt(1.34 * $_POST['length']) . "<br>";
} else {
	print "<b><span style=\"color: rgb(153, 0, 0);\">The input must be numeric</span></b>";
}
?>
<br>
<a href="hSpeed.html">Do Another</a>