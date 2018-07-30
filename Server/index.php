
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>LevelUp-Electrising</title>
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
	<link rel="stylesheet" href="css/style.css">
	<link href='http://fonts.googleapis.com/css?family=Oswald:400,700' rel='stylesheet' type='text/css'>
</head>
<body>

	
	<header>
		<div class="menu">
			<div class="container">
				<div class="logo">LevelUp - Electrising</div>
				<nav>
					<ul>
						<li><a href="/index.php">Nuevo Hospedaje</a></li>
						<li><a href="/reg.php">Huespedes Registrados</a></li>
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
			<p>Registrar una nueva habitación</p>
			

			


			<form action="/sendForm.php" method="post">
			Número de Habitación:<br>
  			<input type="text" name="room"  >
  			<br>
  			Nombre:<br>
  			<input type="text" name="firstname" value="">
  			<br>
			Nivel de Autorización:<br>
  			<input type="number" name="authorization" value="" min="0"  max="9">
  			<br><br>
  			<input type="submit" value="Registrar">
			</form> 

			
			
		</div>
		</article>
 

</body>
</html>
