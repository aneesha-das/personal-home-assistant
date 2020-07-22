<?php
/*
error 1 means password is invalid
error 2 means email id does not exist
error 3 means database error
error 4 means invalid entry
*/
require_once('connection.php');
$email=$_POST['emailName'];
$password=$_POST['passwordName'];
$encryptedPassword=password_hash($password, PASSWORD_DEFAULT);
if($email!="" && $password!=""){
	$query="select password from users where emailid='$email'";
	if($result=mysqli_query($con,$query)){
		if(mysqli_num_rows($result)==1){
			$data=mysqli_fetch_row($result);
			if(password_verify($password,$data[0])){
				$query="delete from sessiontable where 1;";
				if(mysqli_query($con,$query)){
					$sessionID="abc";
					$query="insert into sessiontable values('$email',NOW())";
					if(mysqli_query($con,$query)){
						session_start();
						$_SESSION["username"]=$email;
						header('Location: index.php');
					} else{
						header('Location: login.php?error=3');
					}
				} else{
					header('Location: login.php?error=3');
				}
			} else{
				header('Location: login.php?error=1');
			}
		} else{
			echo($password."<br/>".$encryptedPassword);
			header('Location: login.php?error=2');
		}
	} else{
		header('Location: login.php?error=3');
	}
}else{
	header('Location:login.php?error=4');
}

?>
