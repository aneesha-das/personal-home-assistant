<html>
<head>
<title>Aarti Clock</title>
<script src="clock.js"></script>
</head>
<body style="background-color:#BFEFFF;font-size:2.5em;">
<center>
<canvas id="clock" height=800px width=800px style="margin-top:10%;">
</canvas>
</center>
<?php
require_once('connection.php');
require_once('authenticate.php');
$time=date('D M d Y H:i:s', time());
echo("<center>");
if(isset($_POST['dateName']) && $_POST['dateName']!="" && !isset($_POST['hourName'])){
	$date=$_POST['dateName'];
	$month=$_POST['monthName'];
	$year=$_POST['yearName'];
	$argument="change date ".$date." ".$month." ".$year." ".date('H:i:s',time());
	$query="insert into buffer values (1,'$argument','$time')";
	if(mysqli_query($con,$query)){
	//	echo "Successfully Inserted";
		sleep(2);
		echo("<div id='datediv' style='display:none;'>".$time." GMT+0530 (IST)</div>");
		//header("Location: changedate.php?reload=true");
	} else{
	//	echo "Insertion Unsuccessful";
	}
}
else if((!isset($_POST['dateName']) || $_POST['dateName']=="" ) && isset($_POST['hourName'])){
	$hour=$_POST['hourName'];
	$minute=$_POST['minuteName'];
	$argument="change date ".date('d M Y',time())." ".$hour.":".$minute.":00";
	$query="insert into buffer values (1,'$argument','$time')";
	if(mysqli_query($con,$query)){
		//echo "Successfully Inserted";
		sleep(2);
		echo("<div id='datediv' style='display:none;'>".$time." GMT+0530 (IST)</div>");
		//header("Location: changedate.php?reload=true");
	} else{
		//echo "Insertion Unsuccessful";
	}
}
else if(isset($_POST['dateName']) && isset($_POST['hourName'])){
	$date=$_POST['dateName'];
	$month=$_POST['monthName'];
	$year=$_POST['yearName'];
	$hour=$_POST['hourName'];
	$minute=$_POST['minuteName'];
	$argument="change date ".$date." ".$month." ".$year." ".$hour.":".$minute.":00";
	$query="insert into buffer values (1,'$argument','$time')";
	echo("date:".$date);
	echo(" time: ".$hour);
	if(mysqli_query($con,$query)){
		//echo "Successfully Inserted";
		sleep(2);
		echo("<div id='datediv' style='display:none;'>".$time." GMT+0530 (IST)</div>");
		//header("Location: changedate.php?reload=true");
	} else{
		//echo "Insertion Unsuccessful";
	}
} else{
	echo("<div id='datediv' style='display:none;'>".$time." GMT+0530 (IST)</div>");
}

$timezone=date_default_timezone_get();
echo("Current timezone: ".$timezone);
$date=date('d M Y',time());
$time=date('H:i',time());
echo("<br/>Current date:".$date);
?>
<br/><br/>
<form action="changedate.php" method="POST">
<input type="text" name="dateName" style="font-size:1em;width:20%;border:2px solid black;" placeholder="Date"/>
<select  name="monthName" id="monthId" style="font-size:1em;border:2px solid black;">
<option selected disabled>Choose Month</option>
<script>
var month=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","NOV","DEC"];
var sel=document.getElementById("monthId");
for(var i=0;i<month.length;i++){
var opt=document.createElement('option');
opt.innerHTML=month[i];
opt.value=month[i];
sel.appendChild(opt);
}
</script>
</select>
<input type='text' name="yearName" style="font-size:1em;width:20%;border:2px solid black;" placeholder="Year"/>
<select  name="hourName" id="hourId" style="font-size:1em;border:2px solid black;">
<option selected disabled>HH</option>
<script>
var sel=document.getElementById("hourId");
for(var i=0;i<24;i++){
var opt=document.createElement('option');
if(i<10){
opt.innerHTML='0'+i;
opt.value='0'+i;
}
else{
opt.innerHTML=i;
opt.value=i;
}
sel.appendChild(opt);
}
</script>
</select>
<select  name="minuteName" id="minuteId" style="font-size:1em;border:2px solid black;">
<option selected disabled>MM</option>
<script>
var sel=document.getElementById("minuteId");
for(var i=0;i<60;i++){
var opt=document.createElement('option');
if(i<10){
opt.innerHTML='0'+i;
opt.value='0'+i;
}
else{
opt.innerHTML=i;
opt.value=i;
}
sel.appendChild(opt);
}
</script>
</select>
<br/><br/>
<input type="submit" value="Change" style="font-size:1em;border:2px solid black;margin-left:100px;"/>
</form>
<a href="index.php"><button style="font-size:1em;border:2px solid black;margin-left:-200px;margin-top:-93px;">Back</button></a>
</center>
</body>
</html>
