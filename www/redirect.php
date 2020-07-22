<?php
$url=$_GET['url'];
$keyName=$_GET['keyName'];
$value=$_GET['value'];
header("Location: ".$url."?".$keyName."=".$value);
?>
