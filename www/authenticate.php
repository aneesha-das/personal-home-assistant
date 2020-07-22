<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

session_start();
if(!isset($_SESSION["username"]) or $_SESSION["username"]==null){
	header('Location: login.php');
}

?>
