<?php
require_once('connection.php');
$question=$_POST["questionName"];
$query=("delete from unanswered where question='$question';");
if(mysqli_query($con,$query)){
header("Location:unanswered.php?success=1");
}else{
header("Location:unanswered.php?success=0");
}
?>
