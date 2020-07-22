<html>
<body>
<?php
require_once('authenticate.php');
require_once('connection.php');
$query="select * from temppicture;";
$result=mysqli_query($con,$query);
$path=$_GET['path'];
if($data=mysqli_fetch_row($result)){
	if($data[0]==1){
		echo("<br/><br/>");
		echo("<br/><br/>");
		echo("<img src='/pictures/temp.jpg' width=100% height=700 style='border:5px solid #FFF;'/>");
		echo("<br/><br/>");
		echo("<center><a href='retakepicture.php' ><button style='font-size:2.5em;background-color:#DC143C;color:#FFF;border-radius:10px;'>Retake</button></a>");
		echo("<a href='savepicture.php'><button style='font-size:2.5em;background-color:#1E90FF;color:#FFF;border-radius:10px;margin-left:50px;'>Save</button></a></center>");
	} 
}else{
		if($path=="default"){
			echo("<br/><br/>");
			echo("<br/><br/>");
			$username=$_SESSION["username"];
			$query="select * from pictures where username='$username' order by pid desc;";
			$result=mysqli_query($con,$query);
			if($data=mysqli_fetch_row($result)){
				if($data[2]!=""){
					$relativePath=substr($data[2],strpos($data[2],"/pictures"));
					echo("<img src='$relativePath' width=100% height=700 style='border:5px solid #FFF;'/>");
				}
			}
		} else{
			echo("<br/><br/>");
			echo("<br/><br/>");
			$relativePath=substr($path,strpos($path,"/pictures"));
			echo("<img src='$relativePath' width=100% height=700 style='border:5px solid #FFF;'/>");
		}
	}

?>
</body>
</html>
