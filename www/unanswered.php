<html>
<head>
<title>Teach Me Stuff</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="unanswered.js"></script>
</head>
<body style="background-color:#EEEEEE;">
<div style="background-color:#000;color:#42C0FB;font-size:1.7em;padding-left:20px;padding-top:3px;padding-bottom:3px;">
<center>
<h1>Teach Me</h1>
</center>
</div>
</br></br>
<form action="delete.php" method="post">
<?php
require_once('connection.php');
//require_once('authenticate.php');
$query="select * from unanswered";
$result=mysqli_query($con,$query);
if($result){
	$data=mysqli_fetch_row($result);
	echo("<textarea readonly id='questionID' name='questionName' cols=100 rows=1 style='resize:none;border:3px solid black;font-size:3em;width:75%;padding:10px 10px 10px 10px;'>".$data[0]."</textarea>");
} else{
	echo("Database Error");
}
?>
&nbsp&nbsp&nbsp&nbsp
<input type="submit" id="deleteID" value="Delete" style="font-size:3em;padding:25px 25px 25px 25px;background-color:#BFEFFF;color:red;border:3px solid black;"/>
</form>
<br/><br/>
<span style="font-size:3em;">Number of answers</span> <input type="text" name="numberOfAnswers" id="numberOfAnswersID" style="resize:none;border:3px solid black;font-size:3em;width:20%;padding:10px 10px 10px 10px;"/>
&nbsp&nbsp&nbsp&nbsp
<button id="setButton" style="font-size:3em;padding:10px 25px 10px 25px;background-color:#BFEFFF;color:black;border:3px solid black;">Set</button>
<br/><br/>
<div id="answerBox"></div>
</body>
</html>
