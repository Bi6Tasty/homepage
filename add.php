<?php

$v = $_POST["vards"];
$u = $_POST["uzvards"];
$l = $_POST["login"];
$p = md5($_POST["password"]);

include("cfg.php");
$mysqli->query("INSERT `idk` SET `id`=null,`name`='$v',`sname`='$u',`login`='$l',`password`='$p'");

?>