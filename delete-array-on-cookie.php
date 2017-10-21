 
<?php  
session_start(); 

$id = $_GET['id'];
	
// verifica se existe o cookie
if(isset($_COOKIE["favoritas"])) {
	
// descodifica array do cookie
$favoritas = unserialize($_COOKIE['favoritas']); 
// elimina um valor ao array
unset($favoritas[array_search($id,$favoritas)]);
// codifica novamente o array
$favoritas = serialize($favoritas); 
// atualiza o cookie
setcookie('favoritas', $favoritas, time()+(86400 * 30));	
header("Location: " . $_SESSION['actual_link']);
} 

?> 
