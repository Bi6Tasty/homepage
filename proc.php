<?php
$l = $_POST["login"];
$p = $_POST["password"];

include("cfg.php");
$result = $mysqli->query("SELECT * FROM idk WHERE login = '$l' and password = '$p'");
if (mysqli_num_rows($result) > 0){
    echo "veri gud";
}
else{
    echo "shit, try again";
}
?>


    