<?php

error_reporting(0);

function debug(){

	$f = fopen("/tmp/access_log", "a+");

	$d = "[". date("Y-m-d H:i:s") . "] " . $_SERVER['REMOTE_ADDR'] . " -> ".$_SERVER['REQUEST_URI']." \n";

	foreach($_GET as $key => $value){
		$d .= "   \$_GET[".$key."] => ".$value ."\n";
	}
	foreach($_POST as $key => $value){
        $d .= "   \$_POST[".$key."] => ".$value ."\n";
	}
    foreach($_COOKIE as $key => $value){
        $d .= "   \$_COOKIE[".$key."] => ".$value ."\n";
    }
	foreach($_SERVER as $key => $value){
		$d .= "   \$_SERVER[".$key."] => ".$value."\n";
	}
	foreach($_FILES as $key => $value){
        $d .= "   \$_FILES[".$key."] => ".$value."\n";
	}
	fwrite($f, $d);
	fclose($f);
}

if(__LOADED__ == "__LOADED__"){
	debug();
	define("__LOADED__", "TRUE");
}

?>
