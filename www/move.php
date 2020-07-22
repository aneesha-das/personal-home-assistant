<?php
require_once('connection.php');
require_once('authenticate.php');
$d=$_POST['direction'];
if(isset($d) && $d!=""){
	$query="delete from movebot where 1;";
	if(mysqli_query($con,$query)){
		$query="insert into movebot values('$d');";
		if(mysqli_query($con,$query)){
			echo("done");
		} else{
			echo("Insertion unsucccessful");
		}
	} else{
		echo("Deletion unsucccessful");
	}
}
?>
