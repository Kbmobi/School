<?php
include "imagev2.php";

if($_GET["i"] == 1){
  square(110, 255, 0, 0);
}

elseif($_GET["i"] == 2){
  square(50, 255, 255, 0);
  }

elseif($_GET["i"] == 3){
  triangle(300, 0, 255, 255);
  }

elseif($_GET["i"] == 4){
  triangle(150, 0, 255, 0);
  }

elseif($_GET["i"] == 5){
  circle(400, 200, 255, 0, 0);
  }

elseif($_GET["i"] == 6){
  circle(200, 100, 0, 0, 255);
  }
  
  ?>