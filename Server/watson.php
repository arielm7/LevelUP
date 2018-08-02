<?php
//Get Parameter
$data = $_GET['request'];

//Save the Get Parameter in a text file.
file_put_contents('GetParam.txt', $data);

//Execute external python script
$pythonScript= 'python3 /var/www/html/WatsonCommunication.py ' . ' ' . $data ; # replace with the script direction
echo shell_exec( $pythonScript);
?> 

