<?php
//Start a session that lasts 7 days
session_set_cookie_params(604800);
session_start();
?>
<html>
<head>
<title>Comp 170 -- Lab 10 -- Forum Post</title>
<?php
//Check to see if anything has been selected in the forum
if(isset($_POST["theme"])){
  $_SESSION["time"] = date("Y-m-d H:i:s");
  echo "Last action at:  " . $_SESSION["time"];
}  

// Post Time based off of last selecting an option
if(isset($_SESSION["selectedTheme"])){
  echo "Last action at:  " . $_SESSION["time"];
}


?>
</head>
<body>
<form method="post" action="">
  <fieldset>
  <legend>Look a cool box!</legend>
  <select name="theme" onchange="submit();">
  <option></option>
  <option value="noOneCare">YES!! :D</option>
  <option value="ifYouLikeTurtles">Noo :(</option>
  </select>
  </fieldset>
  </form>
  <h1>Do you like Turtles??</h1>
  <a scr="turtle.jpg" alt="It's a picture of a turtle">

  </body>
  </html>