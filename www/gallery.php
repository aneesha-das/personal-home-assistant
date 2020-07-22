<html>
<body>
<div style='overflow-x:scroll;overflow-y:hidden;white-space:nowrap;padding-top:30px;'>
<?php
require_once('connection.php');
require_once('authenticate.php');
$username=$_SESSION['username'];
$query="select * from pictures where username='$username' order by pid desc";
$result=mysqli_query($con,$query);
$i=1;
if($result){
	while($data=mysqli_fetch_row($result)){
		$relativePath=substr($data[2],strpos($data[2],"/pictures"));
		if($i==1){
			echo("<a href='preview.php?path=".$data[2]."' target='previewFrame'><img src='".$relativePath."' id=".$i." style='display:inline;width:350px;border:5px solid black;height:350px;margin-right:20px;margin-left:20px;box-shadow:5px 10px 20px rgba(0, 0, 0, .5);'></a>");
		}
		else{
			echo("<a href='preview.php?path=".$data[2]."' target='previewFrame'><img src='".$relativePath."' id=".$i." style='display:inline;width:280px;border:5px solid black;height:280px;margin-left:10px;'></a>");
		}
		
		$i=$i+1;
	}
	$i--;
	echo("<textarea id='hiddenID' style='display:none;'>".$i."</textarea>");
} else{
	echo("Connection to database failed");
}
echo("<script src='gallery.js'>");
echo("</script>");
?>
</div>
</body>
</html>
