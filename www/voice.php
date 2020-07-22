<html>
<head>
<title>Speech to text</title>
<link rel="stylesheet" type="text/css" href="stylesheetvoice.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="jsindex.js"></script>
</head>
<body style="background-color:#BFEFFF;">
<?php
require_once('authenticate.php');
?>
<br/><br/>
<div style="background-color:#000;color:#42C0FB;font-size:1.7em;padding-left:20px;padding-top:3px;padding-bottom:3px;">
<center><h1>Voice Command</h1></center>
</div>
<br/><br/>
<div id="resultID"></div>
<center>
<img id="micID" src="images/microphone.png" class="mic" height=200 width=150 style="margin-top:50%;margin-left:-60px;"/>
<div id="responseID" style="font-size:3em;color:#000;">*Response*</div>
</center>
</body>
</html>
