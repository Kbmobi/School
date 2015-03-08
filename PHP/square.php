<?php 
// calls to print off the right squares. 
if($_GET["s"] == 1){
  square(110, 0, 0, 0);
}

elseif($_GET["s"] == 2){
  square(50, 0, 0, 0);
  }

elseif($_GET["t"] == 1){
  triangle(300, 0, 0, 0);
  }

elseif($_GET["t"] == 2){
  triangle(150, 0, 0, 0);
  }



function square ($size, $r, $g, $b) {
  // Output the header telling the browser this is a png image.
  header ('Content-type: image/png');

  // create the empty image.
  $im = imagecreatetruecolor($size, $size) or die('Cannot Initialize new GD image stream');

  /* Define the foreground and background colours and fill the image with the bacground colour.
     The foreground colour is passed as a parameter, the background colour is white */
  $fgcolor = imagecolorallocate($im, 0,0,0);
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
  $fgcolor = imagecolorallocate($im, 0,0,0);
  $bgcolor = imagecolorallocate($im, 255,255,255);
  imagefill($im, 0, 0, $bgcolor); 

  // Draw a rectangle. The upper left coordinate is 0,0. The lower right is size-1, size-1 since we started counting at 0. 
  imagepolygon($im, array($size-1, 1, 1, $size-1, $size-1, $size-1), 3, $fgcolor);

  /* Write the image to standard out - in the case of the web server to the network to the browser
     and free up any memory used by the image */
  imagepng($im);
  imagedestroy($im);  
}

?>