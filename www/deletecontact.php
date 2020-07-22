<?php
require_once("authenticate.php");
require_once("connection.php");
$contact_email=$_GET["email"];
session_start();
$username=$_SESSION['username'];
$query="delete from contacts where useremail='$username' and contactemail='$contact_email';";
if(mysqli_query($con, $query)){
	echo("<script>parent.location.href='contacts.php?success=1'</script>");
} else{
	echo("<script>parent.location.href='contacts.php?success=0'</script>");
}
?> 
