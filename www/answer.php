<?php
require_once('connection.php');
//require_once('authenticate.php');
$commonWords=["a","an","if","the","it","aarti","on","of","then"];
$total=$_GET['total'];
$i=0;
$keyword="";
$question=$_GET['question'];
$query=("insert into questions (question) values('$question');");
$result=mysqli_query($con,$query);
$qid=mysqli_insert_id($con);
$responses=array();
while($i<$total){
	$x="response".($i+1);
	array_push($responses,$_GET[$x]);
	$query=("select rid from responses where response='$responses[$i]';");
	$result=mysqli_query($con, $query);
	$data=mysqli_fetch_row($result);
	if($data[0]=="" || $data[0]==null){
		$query=("insert into responses (response) values('$responses[$i]');");
		mysqli_query($con, $query);
		$rid=mysqli_insert_id($con);
		$query=("insert into qrmap (qid,rid) values('$qid','$rid');");
		mysqli_query($con,$query);
	}else{
	$query=("insert into qrmap (qid,rid) values('$qid','$data[0]');");
	mysqli_query($con,$query);	
	}
	$i++; 
}
$questionArray=explode(" ",$question);
foreach($questionArray as $x){
	if(!in_array($x,$commonWords)){
		$keyword=$keyword.$x." ";
	}
}
if(strlen($keyword)>0){
	$keyword=substr($keyword,0,strlen($keyword)-1);
	$query=("insert into keywords (qid,keyword) values('$qid','$keyword');");
	mysqli_query($con,$query);	
	$query="delete from unanswered where question='$question';";
	mysqli_query($con,$query);
	$query="select * from unanswered";
	$result=mysqli_query($con,$query);
	echo(mysqli_fetch_row($result)[0]);
}
?>
