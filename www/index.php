<html>
<head>
<title>AARTI CONTROL PANEL</title>
</head>
<body style="background-color:#BFEFFF;">
<?php
require_once('authenticate.php');
?>
<a href="logout.php"><button style="float:right;width:200px;height:5%;font-size:x-large;font-weight:bold;background-color:#FFF;">Log out</button></a>

<?php
require_once('connection.php');
$username=$_SESSION['username'];
$query="select gmail from users where emailid='$username';";
$result=mysqli_query($con,$query);
if($result){
	$data=mysqli_fetch_row($result);
	if($data[0]!=""){
		echo("<a href='settings.php'><button style='height:5%;font-size:x-large;font-weight:bold;background-color:#FFF;padding:0px 20px 0px 20px;'>".$data[0]."</button></a>");
	} else{
		echo("<a href='settings.php'><button style='width:200px;height:5%;font-size:x-large;font-weight:bold;background-color:#FFF;'>Settings</button></a>");
	}
} else{
	echo("<a href='settings.php'><button style='width:200px;height:5%;font-size:x-large;font-weight:bold;background-color:#FFF;'>Settings</button></a>");
}
?>
<a href="changedate.php"><button style="width:200px;height:5%;font-size:x-large;font-weight:bold;background-color:#FFF;margin-left:17%;">Clock</button></a>
<br/><br/>
<center>
<table style="border: 1px solid black;" width=100% height=93%>
<tr>
<td style="border: 1px solid black; ">
<a href="voiceinput.php"><button style="width:100%;height:100%;font-size:xx-large;font-weight:bold;">Voice Input</button></a>
</td>
<tr>
<td style="border: 1px solid black; ">
<a href="photostudio.php?path=default"><button  style="width:100%;height:100%;font-size:xx-large;background-color:#FFF;font-weight:bold;">Photo Studio</button></a>
</td>
</tr>
</tr>
<tr>
<td style="border: 1px solid black; ">
<a href="movebot.php"><button  style="width:100%;height:100%;font-size:xx-large;font-weight:bold;">Aarti Remote</button></a>
</td>
</tr>
<tr>
<td style="border: 1px solid black; ">
<a href="contacts.php"><button  style="width:100%;height:100%;background-color:#FFF;font-size:xx-large;font-weight:bold;">Contacts</button></a>
</td>
</tr>
<tr>
<td style="border: 1px solid black; ">
<a href="surveillance.php"><button  style="width:100%;height:100%;font-size:xx-large;font-weight:bold;">Surveillance</button></a>
</td>
</tr>
</table>
</center>
</body>
</html>

