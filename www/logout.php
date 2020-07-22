<?php
/*
error 1 means log out error
*/
require_once('connection.php');
$query="delete from sessiontable where 1";
if(mysqli_query($con,$query)){
	session_start();
	$_SESSION["username"]=null;
	session_destroy();
	header("Location: login.php");
} else{
	header("Location: index.php?error=1");
}
?>
