<?php
/*success==1 means edit successful*/
require_once("authenticate.php");
require_once("connection.php");
$contact_name=$_POST["editcontactname"];
$contact_email=$_POST["editcontactid"];
$prev_contact=$_POST['hiddenemail'];
session_start();
$username=$_SESSION['username'];
$query="update contacts set contactemail='$contact_email', contactname='$contact_name' where useremail='$username' and contactemail='$prev_contact';";
if(mysqli_query($con, $query)){
	echo("<script>parent.location.href='contacts.php?success=1'</script>");
} else{
	echo("<script>parent.location.href='contacts.php?success=0'</script>");
}
?> 
