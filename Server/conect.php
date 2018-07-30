  <?php
    //Conexion
    $server='localhost';
    $user='root';
    $pass='root';
    $DB ="LevelUp";
    $table="Registros";
    //Conexion a la base de datos
    $conect=new mysqli($server,$user,$pass);

    mysqli_select_db($conect,$DB) OR DIE ("Error: No es posible establecer la conexión");
?>

<?php
  //Sacar Datos
  $Arreglo=array();
  $i=0;
  //Lectura de la DB
  $consulta = "SELECT * FROM $table"; // Adquiere los datos de la base
  $ejecutar = $conect->query($consulta);
  while($fila = $ejecutar-> fetch_array()): 
    //Genera el arreglo con la DB
    $Arreglo[$i]=$fila;
    $i++;
  endwhile;
?>



