<html>
<head>
<title>
Photo Studio
</title>
<script src="menu.js"></script>
</head>
<frameset rows=10%,60%,30%>
<?php
require_once('authenticate.php');
$path=$_GET['path'];
echo("<frame src='menu.php' name='menuName'/>");
echo("<frame name='previewFrame' src='preview.php?path=".$path."' style='border:11px solid #42C0FB;background-color:black;'/>");
echo("<frame src='gallery.php' style='border:20px groove #42C0FB;' scrolling='no'/>");
?>
</frameset>
</html>
