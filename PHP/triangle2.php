<?php
// Create a blank image
$image = imagecreatetruecolor(300, 200);

//create background colow
$bgcolor = imagecolorallocate($image, 255, 255, 255);
imagefill($image, 0, 0, $bgcolor);

// Allocate a color for the polygon
$fgcolor = imagecolorallocate($image, 0, 0, 0);

// Draw the triangle
imagepolygon($image, array(150, 5, 5, 195, 295, 195), 3, $fgcolor);

// Output the picture to the browser
header('Content-type: image/png');

imagepng($image);
imagedestroy($image);
?>