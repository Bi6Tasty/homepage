<?php
$l = $_POST["login"];
$p = $_POST["password"];

include("cfg.php");
$mysqli = new mysqli("SELECT * FROM users WHERE login=$l and password")

echo "Hello user $l, Password used $p";

?>


