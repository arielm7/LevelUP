<!DOCTYPE html>
<html>
<body>

<?php

//Get and decode the JSON file
$data = json_decode(file_get_contents('php://input'), true);
//Save the JSON string to a text file.
file_put_contents('json_array.txt', $data);

?> 


</body>
</html>
