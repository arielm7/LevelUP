
<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>LevelUp</title>
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
	<link rel="stylesheet" href="css/style.css">
	<link href='http://fonts.googleapis.com/css?family=Oswald:400,700' rel='stylesheet' type='text/css'>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>
	

	
	<header>
		<div class="menu">
			<div class="container">
				<div class="logo">LevelUp - Electrising</div>
				<nav>
					<ul>
						<li><a href="/index.php">Nuevo Hospedaje</a></li>
						<li><a href="/reg.php">Huespedes Activos</a></li>
						<li><a href="#">Registro de Peticiones</a></li>
					</ul>
				</nav>
			</div>
		</div>
	</header>
 

		
	<div class="main container">
		<br><br><br>
		<article>
			<div class="texto">

			
			<h2>Electrising</h2>
			<br>
			<p>Reservaciones Activas</p>


			
  <?php include "conect.php";?>



  <!-- Table starts here -->
  <table id="table" class="table table-hover table-mc-light-blue">
      <thead>
        <tr>
          <th>ID</th>
	  <th>Fecha de Ingreso</th>
          <th>Habitación</th>
          <th>Nombre</th>
          <th>Nivel de Autorización</th>
          <th>Estado</th>
        </tr>
      </thead>
      <tbody>
	

	<?php
    	$cont=0;
    	while($cont != $i):
	$conect->close();
  	?>

        <tr>
          <td data-title="ID"><?php echo $Arreglo[$cont]["ID"] ?></td>
          <td data-title="Date"><?php echo $Arreglo[$cont]["Date"] ?></td>
          <td data-title="Room"><?php echo $Arreglo[$cont]["Room"] ?></td>
	  <td data-title="FName"><?php echo $Arreglo[$cont]["FName"] ?></td>
	  <td data-title="Authorization"><?php echo $Arreglo[$cont]["Authorization"] ?></td>
	  <td data-title="Status"><?php echo $Arreglo[$cont]["Status"] ?></td>
        </tr>
        <?php $cont++; endwhile; ?>
      </tbody>
    </table>



		
		</div>
		</article>


</body>
</html>
