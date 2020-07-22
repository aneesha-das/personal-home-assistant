<html>
<head>
</head>
<body>
<?php
require_once('authenticate.php');
?>
<div style="background-color:#000;color:#42C0FB;font-size:1.7em;padding-left:20px;padding-top:3px;padding-bottom:3px;">
<center><h1>Contacts</h1></center>
</div>
<br/><br/>
<center>
<form action="addcontact.php" method="post">
<fieldset style="border:3px inset #000;margin-top:5%;">
<legend style="font-size:2.5em;">Add New Contact</legend>
<br/><br/>
<span style="font-size:2.5em;">Name:</span> <input type=text name="nameName" style="border:3px inset #000;font-size:2.5em;width=5%;" id="NameId"/><br/><br/><br/>
<span style="font-size:2.5em;">Email: </span><input type=email name="emailName" style="border:3px inset #000;font-size:2.5em;width=5%;" id="EmailId"/>
<br/><br/>
<br/>
<input type="submit" name="submit" id="submitId" value="Add" style="padding: 5px 10px 5px 10px;font-size:2.5em;background-color:#EE82EE;color:#FFF;padding:15px 15px 15px 15px;box-shadow:2px 5px 5px rgba(0, 0, 0, .5);width:15%;">
<br/><br/>
</fieldset>
</form>
</center>
<center>
<hr style="border:3px solid black;"/>
<div style="background-color:#BFEFFF;padding-top:23px;">
<h4 style="font-size:3em;">Saved Contacts</h4>
<hr style="border:3px solid black;"/>
</div>
<br/>
<div style="overflow-y: scroll; height:37%;">
<table style="border:5px solid black;width:100%;font-size:2.5em;">
<tr>
<th  style="border:2px solid black;">
Name
</th>
<th style="border:2px solid black;" colspan=3>
Email
</th>
</tr>
<?php
require_once('connection.php');
$email=$_SESSION['username'];
$query="select contactemail,contactname from contacts where useremail='$email' order by contactname;";
$result=mysqli_query($con,$query);
if($result){
	while($data=mysqli_fetch_row($result)){
		echo("<tr><td  style='border:2px solid black;'>".$data[1]."</td>");
		echo("<td  style='border:2px solid black;'>".$data[0]."</td>");
		$str="editcontact.php?email=".$data[0]."&&contactname=".$data[1];
		echo("<td style='border:2px solid black;padding:10px 10px 10px 10px;background-color:#EE82EE;'><a style='color:#000;' href=".$str.">Edit</a></td>");
		$str="deletecontact.php?email=".$data[0];
		echo("<td style='border:2px solid black;padding:10px 10px 10px 10px;background-color:#BFEFFF;'><a style='color:red;' href=".$str.">Delete</a></td></tr>");
	}
}
?>
</table>
</div>
</center>
<script>
window.onload=function(){
	var name=document.getElementById("NameId");
	var email=document.getElementById("EmailId");
	var submit=document.getElementById("submitId");
	submit.onclick=function(){
		if(name.value=="" || email.value==""){
			alert("Please Fill Up All The Fields");
			return false;
		}
		else{
			return true;
		}
	}
}
</script>
</body>
</html>
