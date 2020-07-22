<?php
require_once("connection.php");
$question=$_POST["question"];
$valid=1;
$time=date('Y/m/d h:i:s a', time());
$query1="delete from buffer where 1";
$query2="insert into buffer values ('$valid','$question','$time')";
if(mysqli_query($con,$query1)){
	echo "Deletion Successful";
	if(mysqli_query($con,$query2)){
		echo "Successfully Inserted";
	} else{
		echo "Insertion Unsuccessful";
	}
} else{
	echo "Connection Failure";
}

?>
