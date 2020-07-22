<?php
require_once('connection.php');
require_once('authenticate.php');
$question="take a picture";
$valid=1;
$time=date('Y/m/d h:i:s a', time());
$query1="delete from buffer where 1";
$query2="insert into buffer values ('$valid','$question','$time')";
if(mysqli_query($con,$query1)){
	if(mysqli_query($con,$query2)){
		sleep(1);
		echo("<script>parent.window.location.href='voiceinput.php?path=default'</script>");
	} else{
		sleep(1);
		echo("<script>parent.window.location.href='photostudio.php?path=default'</script>");
	}
} else{
	echo "Connection Failure";
}
?>
