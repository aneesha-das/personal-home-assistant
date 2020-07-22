<?php
require_once('connection.php');
require_once('authenticate.php');
$query="select * from responsebuffer where valid=1;";
$result=mysqli_query($con,$query);
if($result){
	$data=mysqli_fetch_row($result);
	if($data[0]==1){
		echo($data[1]);
		$query="delete from responsebuffer where 1;";
		$result=mysqli_query($con,$query);
	}
}
?>
