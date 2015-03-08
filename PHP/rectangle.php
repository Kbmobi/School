<?php

function draw_grid(&$img, $x0, $y0, $width, $height, $cols, $rows, $color) {
    //draw outer border
    imagerectangle($img, $x0, $y0, $x0+$width*$cols, $y0+$height*$rows, $color);
    //first draw horizontal
    $x1 = $x0;
    $x2 = $x0 + $cols*$width;
    for ($n=0; $n<ceil($rows/2); $n++) {
        $y1 = $y0 + 2*$n*$height;
        $y2 = $y0 + (2*$n+1)*$height;
        imagerectangle($img, $x1,$y1,$x2,$y2, $color);
    }
    //then draw vertical
    $y1 = $y0;
    $y2 = $y0 + $rows*$height;
    for ($n=0; $n<ceil($cols/2); $n++) {
        $x1 = $x0 + 2*$n*$width;
        $x2 = $x0 + (2*$n+1)*$width;
        imagerectangle($img, $x1,$y1,$x2,$y2, $color);
    }
}

//example
$img = imagecreatetruecolor(300, 200);
$red   = imagecolorallocate($img, 255, 255, 255);
draw_grid($img, 0,0,15,20,20,10,$red);
header("Content-type: image/png");
imagepng($img);
imagedestroy($img);
?>