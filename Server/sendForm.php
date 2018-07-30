<html>
<body>

<!-- Post data?-->
<?php 
$room= $_POST["room"];
$firstname= $_POST["firstname"];
$nfc= $_POST["nfc"];
$authorization= $_POST["authorization"]; 
$date= date("y-m-d"); 

?>

<?php include "conect.php";?>


<!--insert form in mysql database -->
<?php
$sql = "INSERT INTO Registros (`ID`, `Date`, `Room`, `FName`, `LName`, `NFC`, `Authorization`, `Status`) 
VALUES ('2', '$date', $room, '$firstname', 'fgfg', '3432', '$authorization ', 'Activo')";

if ($conect->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conect->error;
}

?>

</body>
</html>
