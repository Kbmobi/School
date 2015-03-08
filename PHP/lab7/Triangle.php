<?php
/* 
Lab Number: 7
Program Name if applicable: Lab7
Author name and email addres: Keegan Bailey, kbailey.v@gmail.com
Date of submission: 2/22/2013
Time estimated to complete the lab: 8 hour
Actual time taken to complete the lab: over 20 hours 
A description of the program: Use objects to create and manipulate images.		
required to run the program if applicable: lab7.html, main.php, Shape.php, Square.php, Triangle.php, Circle.php
*/
include_once('Shape.php');

class Triangle extends Shape {

	public function draw () {
		$arrayForTrianglePoints = array($this->x, $this->y, $this->x, $this->x + $this->shapeSize, $this->x + $this->shapeSize, $this->y + $this->shapeSize);
		imagepolygon($this->canvas, $arrayForTrianglePoints, 3, $this->fg);
	}

}


?>
