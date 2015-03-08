<?php
// Create a blank image   x y
$image = imagecreatetruecolor(400, 300);

//create background colow
$bgcolor = imagecolorallocate($image, 0, 255, 255);
imagefill($image, 0, 0, $bgcolor);

// Allocate a color for the polygon
$color = imagecolorallocate($image, 255, 0, 0);

// Draw the triangle
imagepolygon($image, array(10, 10, 10, 290, 390, 150), 3, $color);

// Output the picture to the browser
header('Content-type: image/png');

imagepng($image);
imagedestroy($image);
?>