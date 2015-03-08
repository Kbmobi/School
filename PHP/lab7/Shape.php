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
class Shape { 
	protected $canvasSize;
	protected $shapeSize;
	protected $x;
	protected $y;

	public function __construct($inCanvasSize, $inShapeSize, $inX, $inY) {
		//clean variables
		$inCanvasSize = htmlspecialchars(strip_tags(trim($inCanvasSize)), ENT_QUOTES);
		$inShapeSize = htmlspecialchars(strip_tags(trim($inShapeSize)), ENT_QUOTES);
		$inX = htmlspecialchars(strip_tags(trim($inX)), ENT_QUOTES);
		$inY = htmlspecialchars(strip_tags(trim($inY)), ENT_QUOTES);
		
		//set vars
		$this->canvasSize = $inCanvasSize;
		$this->shapeSize = $inShapeSize;
		$this->x = $inX;
		$this->y = $inY;
		
		//Start creating colors an the canvas
		$this->canvas = imagecreatetruecolor($this->canvasSize, $this->canvasSize) or die('Cannot Initialize new GD image stream'); 
		$this->fg = imagecolorallocate($this->canvas, 255, 255, 255);
		$this->bg = imagecolorallocate($this->canvas, 0,0,0);
		$this->fill = imagefill($this->canvas, 0, 0, $this->bg);
	}
	
	public function __destruct() { 
		if(isset($this->canvas)) { 
			imagedestroy($this->canvas); 
		}	 
	}

	public function disp() {
		header ('Content-type: image/png');
		imagepng($this->canvas);
	}

	//Functions to move and resize image
	
	public function makeBigger ($di) {
		$i = htmlspecialchars(strip_tags(trim($di)), ENT_QUOTES);
		
		//get test data
		$iTest1 = $i + $this->x;
		$iTest2 = $i + $this->y;

		//check to see if input amount is no good
		if($i <= 0  || $iTest1 > $this->canvas || $iTest2 > $this->canvas){
			$i == 0;
		}	   	
		
		//increase size
		$this->shapeSize += $i;
	}

	public function makeSmaller ($di) {
		$i = htmlspecialchars(strip_tags(trim($di)), ENT_QUOTES);

		//test data
		$iTest1 = $this->shapeSize - $i;

		//check to see if input amount is no good
		if($i <= 0 || $iTest1 <= 0) {
			$i == 0;
		}	
  
		$this->shapeSize -= $i;
	}

	public function moveUp ($di) {
		$i = htmlspecialchars(strip_tags(trim($di)), ENT_QUOTES);
		
		//test data
		$iTest1 = $this->y - $i;

		if($i <= 0|| $iTest1 <= 0) {
			$i == 0;
		}
		
		$this->y -= $i;
	}

	public function moveRight ($di) {
		$i = htmlspecialchars(strip_tags(trim($di)), ENT_QUOTES);
		
		$iTest1 = $this->x + $i + $this->shapeSize;
		
		if($i <= 0 || $iTest1 >= $this->canvas) {
			$i == 0;
		}
	
		$this->x += $i;
	}

	public function moveDown ($di) {
		$i = htmlspecialchars(strip_tags(trim($di)), ENT_QUOTES);
	
		//test data
		$iTest1 = $this->y + $this->shapeSize + $i;

		if($i <= 0|| $iTest1 >= $this->canvas) {
			$i == 0;
		}
		
		$this->y += $i;
	}

	public function moveLeft ($di) {
		$i = htmlspecialchars(strip_tags(trim($di)), ENT_QUOTES);

		//test data
		$iTest1 = $this->x - $i;
		
		if($i <= 0 || $iTest1 >= 0) {
			$i == 0;
		}
	
		$this->x -= $i;
	}


}
?>