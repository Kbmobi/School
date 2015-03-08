<?php 
function square ($size) {
  // Output the header telling the browser this is a png image.
  header ('Content-type: image/png');

  $im = imagecreatetruecolor($size, $size) or die('Cannot Initialize new GD image stream');
  $fgcolor = imagecolorallocate($im, 255, 255, 255);
  $bgcolor = imagecolorallocate($im, 0,0,0);
  imagefill($im, 0, 0, $bgcolor); 

  imagerectangle($im, 0, 0, $size-1, $size-1, $fgcolor);

  imagepng($im);
  imagedestroy($im);  
}
?>