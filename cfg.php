<?php
$servername = "localhost";
$username = "root";
$password = "";
$db = "projekts2023";



$mysqli = new mysqli($servername,$username,$password,$db);

// Check connection
if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}
?>