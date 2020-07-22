<?php
/*
success=1 is addition successful
success=2 means fields empty
success=3 email or name exists
success=0 database error
*/
require_once("connection.php");
session_start();
$useremail=$_SESSION["username"];
$contactname=$_POST["nameName"];
$contactemail=$_POST["emailName"];
if($contactname=="" || $contactemail==""){
	//echo("<script>parent.location.href='contacts.php?success=2'</script>");
}
$query="select * from contacts where useremail='$email' and (contactemail='$contactemail' or contactname='$contactname');";
$result=mysqli_query($con,$query);
if($result){
	if($data=mysqli_fetch_row($result)){
		echo("<script>parent.location.href='contacts.php?success=3'</script>");
	}
	else{
		$query="insert into contacts values ('$useremail','$contactemail', '$contactname')";
		if(mysqli_query($con, $query)){
			echo("<script>parent.location.href='contacts.php?success=1'</script>");
		} else{
			echo("<script>parent.location.href='contacts.php?success=0'</script>");
		}
	}
}
?>
