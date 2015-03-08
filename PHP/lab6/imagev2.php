<?php 
function square ($size, $r, $g, $b) {
  // Output the header telling the browser this is a png image.
  header ('Content-type: image/png');

  // create the empty image.
  $im = imagecreatetruecolor($size, $size) or die('Cannot Initialize new GD image stream');

  /* Define the foreground and background colours and fill the image with the bacground colour.
     The foreground colour is passed as a parameter, the background colour is white */
  $fgcolor = imagecolorallocate($im, $r, $g, $b);
  $bgcolor = imagecolorallocate($im, 255,255,255);
  imagefill($im, 0, 0, $bgcolor); 

  // Draw a rectangle. The upper left coordinate is 0,0. The lower right is size-1, size-1 since we started counting at 0. 
  imagerectangle($im, 0, 0, $size-1, $size-1, $fgcolor);

  /* Write the image to standard out - in the case of the web server to the network to the browser
     and free up any memory used by the image */
  imagepng($im);
  imagedestroy($im);  
}

function triangle($size, $r, $g, $b){
  // Output the header telling the browser this is a png image.
  header ('Content-type: image/png');

  // create the empty image.
  $im = imagecreatetruecolor($size, $size) or die('Cannot Initialize new GD image stream');

  /* Define the foreground and background colours and fill the image with the bacground colour.
     The foreground colour is passed as a parameter, the background colour is white */
  $fgcolor = imagecolorallocate($im, $r, $g, $b);
  $bgcolor = imagecolorallocate($im, 255,255,255);
  imagefill($im, 0, 0, $bgcolor); 

  // Draw a triangle.  
  imagepolygon($im, array(($size / 2), 1, 1, $size-1, $size-1, $size-1), 3, $fgcolor);

  /* Write the image to standard out - in the case of the web server to the network to the browser
     and free up any memory used by the image */
  imagepng($im);
  imagedestroy($im);  
}

function circle($size, $circ, $r, $g, $b){
  // Create a blank image.
  $image = imagecreatetruecolor($size, $size);

  // Select the background color.
  $bg = imagecolorallocate($image, 0, 0, 0);

  // Fill the background with the color selected above.
  imagefill($image, 0, 0, $bg);

  // Choose a color for the ellipse.
  $col_ellipse = imagecolorallocate($image, $r, $g, $b);

  // Draw the ellipse.
  imageellipse($image, ($size/2), ($size/2), $circ, $circ, $col_ellipse);

  // Output the image.
  header("Content-type: image/png");
  imagepng($image);
}

?>