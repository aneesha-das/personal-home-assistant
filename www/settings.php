<html>
<head>
<title>AARTI SETTINGS</title>
</head>
<body style="background-color:#FFF">
<?php
require_once('authenticate.php');
?>

<center>
<br/><br/><br/><br/><br/>
<img src="/images/Gmail_logo.png" width=80% height=30%/>
<div style="background-color:#BFEFFF;font-size:3.7em;font-weight:bold;margin-top:10%;">
<hr/>
Configure Your Gmail Account
<hr/>
</div>
</center>
<br/><br/>
<fieldset style="background-color:#FFF;margin-top:5%;border-color:#BFEFFF;border-style:solid;border-width:10px 10px 10px 10px">
<form action="setgmailid.php" method="post" style="font-size:3em;">
<br/>
<div style="margin-left:19%;">
Gmail ID <input type="email" name="gIDName"style="font-size:1em;"/><br/><br/>
</div>
<div style="margin-left:19%;">
Gmail Password <input type="password" name="gIDPasswordName"style="font-size:1em;"/><br/><br/>
</div>
<center>
<input type=submit value="Save" style="font-size:1.5em;background-color:#BFEFFF;">
</center>
</form>
</fieldset>
</body>
</html>

