<?php
$l = $_POST["login"];
$p = $_POST["password"];

include("cfg.php");
$result = $mysqli->query("SELECT * FROM users WHERE (login='$l') AND (password='$p')");
if (mysqli_num_row($result) > 0){
    echo "veri gud";
}
else{
    echo "shit, try again";
}

?>


    