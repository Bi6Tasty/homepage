<?php
$l = $_POST["login"];
$p = $_POST["password"];

include("cfg.php");
$result = new mysqli("SELECT * FROM users WHERE login=$l AND password=$p");
if (mysql_num_row($result) > 0){
    echo "veri gud";
}
else{
    echo "shit, try again";
}

?>


    