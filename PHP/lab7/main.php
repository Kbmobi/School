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

include('./Square.php');
include('./Circle.php');
include('./Triangle.php');


if($_GET['x'] == 1) {
	//Draw a square
	$test = new Square(300, 50, 100, 100);
	$test->draw();
	$test->makeSmaller(25);
	$test->moveUp(25);
	$test->moveLeft(30);
	$test->draw();
	$test->moveUp(5);
	$test->moveLeft(5);
	$test->makeBigger(65);
	$test->draw();
	$test->disp();
}

elseif($_GET["x"] == 2) {
	//Draw a Circle
	$test2 = new Circle(300, 50, 100, 100);
	$test2->draw();
	$test2->makeSmaller(10);
	$test2->moveRight(50);
	$test2->draw();
	$test2->makeBigger(20);
	$test2->moveDown(50);
	$test2->moveLeft(30);
	$test2->draw();
	$test2->disp();
}

elseif($_GET["x"] == 3) {
	//Draw a triangle
	$test3 = new Triangle(300, 50, 100, 100);
	$test3->draw();
	$test3->moveLeft(10);
	$test3->moveUp(20);
	$test3->makeBigger(150);
	$test3->draw();
	$test3->makeSmaller(125);
	$test3->moveDown(95);
	$test3->moveRight(75);	
	$test3->draw();
	$test3->disp();
}

?>