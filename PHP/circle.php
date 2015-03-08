<?php
// Create a blank image
$image = imagecreatetruecolor(300, 200);

//create background colow
$bgcolor = imagecolorallocate($image, 255, 255, 255);
imagefill($image, 0, 0, $bgcolor);

// Allocate a color for the polygon
$fgcolor = imagecolorallocate($image, 0, 0, 0);

// Draw the circle
imageellipse($image, 100, 150, 75, 75, $col_ellipse);

// Output the picture to the browser
header('Content-type: image/png');

imagepng($image);
imagedestroy($image);
?>