<!DOCTYPE HTML>

<html>
<head>
    <title>DinnerApp.ca</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <meta name="description" content=""/>
    <meta name="keywords" content=""/>
    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,600,700" rel="stylesheet"/>
    <!--[if lte IE 8]>
    <script src="js/html5shiv.js"></script><![endif]-->
    <script src="js/5grid.min.js">{
            prefix:'css/style', preset
        :
            'legacy'
        }</script>
    <noscript>
        <link rel="stylesheet" href="css/5grid-noscript.min.css"/>
        <link rel="stylesheet" href="css/style.css"/>
        <link rel="stylesheet" href="css/style-desktop.css"/>
    </noscript>
    <!--[if lte IE 9]>
    <link rel="stylesheet" href="css/ie9.css"/><![endif]-->
    <!--[if lte IE 8]>
    <link rel="stylesheet" href="css/ie8.css"/><![endif]-->
    <!--[if lte IE 7]>
    <link rel="stylesheet" href="css/ie7.css"/><![endif]-->
    <script src="js/jquery-1.9.1.min.js"></script>
    <script src="js/init.js"></script>
    <script type="text/javascript">
        //Get the submit button to send over the inputs
        $(document).ready(function () {
            $("#btn").click(function () {
                $(document).scrollTop($("#scrollTo").offset().top);
                $("#qr").load("PHP/main.php", {'inputSearch': $('#inputSearch').val()});
            });
        });
    </script>
    <style>
        button.css3button {
            font-family: 'Open Sans', sans-serif;
            font-size: 1.85em;
            color: #3e3e3e;
            font-weight: 600;
            padding: 10px 20px;
            background: -moz-linear-gradient(top, #ec9678 0%, #ec9678);
            background: -webkit-gradient(linear, left top, left bottom, from(#ec9678), to(#ec9678));
            -moz-border-radius: 10px;
            -webkit-border-radius: 10px;
            border-radius: 10px;
            border: 1px solid #3e3e3e;
            -moz-box-shadow: 0px 1px 3px rgba(000, 000, 000, 0.5), inset 0px 0px 1px rgba(255, 255, 255, 0.5);
            -webkit-box-shadow: 0px 1px 3px rgba(000, 000, 000, 0.5), inset 0px 0px 1px rgba(255, 255, 255, 0.5);
            box-shadow: 0px 1px 3px rgba(000, 000, 000, 0.5), inset 0px 0px 1px rgba(255, 255, 255, 0.5);
            text-shadow: 0px -1px 0px rgba(000, 000, 000, 0.7), 0px 1px 0px rgba(255, 255, 255, 0.3);
        }
    </style>
</head>
<body style="overflow:hidden;">

<!-- Nav -->
<nav id="nav">
    <ul>
        <li><a href="#top">Home</a></li>
        <li><a href="#search">Refined Search</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#help">Help</a></li>
    </ul>
</nav>

<!-- Home -->
<div class="wrapper wrapper-style1 wrapper-first">
    <article class="5grid 5grid-container" id="top">
        <div class="row">
            <div class="4u">
                <span class="me image image-full"><img src="images/logo2.jpg" alt=""/></span>
            </div>
            <div class="8u">
                <header>
                    <h1>Welcome to <strong>DinnerApp.ca</strong>.</h1>
                </header>
                <p>Try typing something in.</p>

                <form>
                    <input type="text" id="inputSearch" name="inputSearch"/>
                    <button type="button" id="btn" name="submit" class="css3button">submit</button>
                </form>
            </div>
        </div>
    </article>
</div>

<!-- Search -->
<div class="wrapper wrapper-style2">
    <article id="search">
        <div class="row">
            <div class="">
                <header>
                    <h1>Welcome to <strong>Refined Search</strong>.</h1>
                </header>
            </div>
        </div>
    </article>
</div>

<!-- Results -->
<div id="scrollTo"/>
<div class="wrapper wrapper-style3">
    <br><br>
    <article id="results">
        <div class="row">
            <div class="4u">
                <div id="qr"></div>
            </div>
        </div>
    </article>
</div>

<!-- Help -->
<div class="wrapper wrapper-style4">
    <article id="help">
        <header>
            <h2>Welcome to Dinnerapp.ca</h2>
            <ul>
                <li>Click Home at any time to get back to the search bar</li>
                <li>Check your fridge or whatever for foot items</li>
                <li>Enter items into the Search Box and press Enter or Return</li>
                <li>Try to stick to major ingredients like Chicken, Salmon or Tofu</li>
                <li>Don't type in items like Salt, Olive Oil, or other minor ingredients</li>
            </ul>
        </header>

        <footer>
            <p>Created By: Keegan Bailey, Cory Purnell, Jordan Penisface</p>
        </footer>
    </article>
</div>


</body>
</html>