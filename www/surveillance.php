<?php
require_once("authenticate.php");
require_once("connection.php");
$query="insert into buffer values(1,'surveillance mode on', sysdate());";
$result=mysqli_query($con,$query);
if($result){
	sleep(5);
	$port = '5000';
	header('Location: '
    		. ($_SERVER['HTTPS'] ? 'https' : 'http')
    		. '://' . $_SERVER['HTTP_HOST'] . ':' . $port);
		exit;
}
else{
	echo("databse error");
}
?>
