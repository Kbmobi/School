<!--
Lab Number: 10
Program Name if applicable: Lab10
Author name and email addres: Keegan Bailey, kbailey.v@gmail.com
Date of submission: 3/12/2013
Time estimated to complete the lab: 5 hours
Actual time taken to complete the lab: 3 hours
A description of the program: Use Sessions to save states of a CSS file
required to run the program if applicable: index.php, default/one/two/three.css
-->
<?php
//Start a session
session_set_cookie_params(3600);
session_start();
?>
<html>
<head>
<title>Comp 170 -- Lab 10</title>
<?php
 //Check to see if anything has been selected in the forum
if(isset($_POST["theme"])){
  $_SESSION["selectedTheme"] = $_POST["theme"];  
}  

  // Pick a theme based off of the input selected.
if(isset($_SESSION["selectedTheme"])){
  $theme = $_SESSION["selectedTheme"];
	if($theme == "default"){
    echo '<link rel="stylesheet" type="text/css" href="default.css" />';
	session_destroy();
  } elseif($theme == "one"){
    echo '<link rel="stylesheet" type="text/css" href="one.css" />';
  } elseif($theme == "two"){
    echo '<link rel="stylesheet" type="text/css" href="two.css" />';
  } elseif($theme == "three"){
    echo '<link rel="stylesheet" type="text/css" href="three.css" />';
  }
}


?>
</head>
<body>
<form method="post" action="">
  <fieldset>
  <legend>Theme Select</legend>
  <select name="theme" onchange="submit();">
  <option></option>
  <option value="default">Default</option>
  <option value="one"> Red + White Text </option>
  <option value="two"> Black + RGB Text </option>
  <option value="three">Annoying</option>
  </select>
  </fieldset>
  </form>

  <h1>This is a Header 1</h1>
  <p id="one">This is a paragraph.</p>

  <h2>This is a Header 2</h2>
  <p id="two">This is another paragraph.</p>

  <h3>This is a Header 3</h3>
  <p id="three">This is yet another paragraph.</p>

  </body>
  </html>