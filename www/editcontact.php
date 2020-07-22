<html>
<head>
<title>Edit Contact</title>
</head>
<body style="background-color:#BFEFFF;">
<?php
require_once("authenticate.php");
$contact_email=$_GET["email"];
$contact_name=$_GET["contactname"];
echo("<br/><br/>");
echo("<center>");
echo("<form action='update.php?email=".$contact_email."'  method=post>");
echo("<fieldset style='border:3px inset #000;margin-top:5%;background-color:#FFF;'>");
echo("<legend style='font-size:2.5em;'>EDIT CONTACT</legend>");
echo("<span style='font-size:1.5em;'>Contact Name:</span>");
echo("<input type='text' name='editcontactname' value='".$contact_name."' style='font-size:1.5em;margin-left:10px;border:3px inset #000;'/>");
echo("<br/><br/><span style='font-size:1.5em;'>Contact Email</span>");
echo("<input type='email' name='editcontactid' value='".$contact_email."'style='font-size:1.5em;margin-left:10px;border:3px inset #000;'/>");
echo("<input type='hidden' name='hiddenemail' value='".$contact_email."'/>");
?>
<br/><br/>
<input type='submit' value="save" style="padding: 5px 10px 5px 10px;font-size:2em;background-color:#EE82EE;color:#FFF;padding:15px 15px 15px 15px;box-shadow:2px 5px 5px rgba(0, 0, 0, .5);width:15%;"/>
<br/><br/>
</fieldset>
</form>
</center>
</body>
</html>

