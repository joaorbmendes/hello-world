<?php  
session_start(); 
$id = $_GET['id'];
	
// verifica se existe o cookie
if(isset($_COOKIE["favoritas"])) {
	
// descodifica array do cookie
$favoritas = unserialize($_COOKIE['favoritas']); 
// acrescenta um valor ao array
array_push($favoritas, $id); 
// codifica novamente o array
$favoritas = serialize($favoritas); 
// atualiza o cookie
setcookie('favoritas', $favoritas, time()+(86400 * 30));	
header("Location: " . $_SESSION['actual_link']);
} else {
	
// cria o array	
$lista = array();	
array_push($lista, $id); 
// codifica o array
$favoritas = serialize($lista); 
// cria o cookie
setcookie("favoritas", $favoritas, time()+(86400 * 30));	
header("Location: " . $_SESSION['actual_link']);
}
?>
