<?php
  if (isset($_POST['user']) && isset($_POST['pwd'])) {
    session_start();

    $user = $_POST['user'];
    $pwd = $_POST['pwd'];

    $plaintext = 'S3cur34ppl1c4t10nD4t4&is_admin=0&username=' . $user . '&password=' . $pwd;

    $key = openssl_random_pseudo_bytes(16);
    $iv = openssl_random_pseudo_bytes(16);
    $_SESSION['key'] = $key;
    $_SESSION['iv'] = $iv;

    $ciphertext = openssl_encrypt($plaintext, 'AES-128-CBC', $key, OPENSSL_RAW_DATA, $iv);
    
    header('Location: index.php?user='.$user.'&pwd='.$pwd.'&ct=' . bin2hex($ciphertext));
  }
?>

<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta http-equiv='X-UA-Compatible' content='IE=edge'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <link rel="icon" href="icon.png">
  <title>Secure App</title>
</head>
<style>
	#container {
		text-align: center;
		/*margin: auto;*/
		width: 20%;
		border: 2px solid black;
		padding: 10px;
	}
	
	input {
		padding: 5px;
	}
	
	h1 {
		margin: 0px 0px 1.5em 0px;
	}
</style>
<body >
  <div id='container'>
	<h1>Secure App Login Page</h1>
    <form action='' id='login-form' method='POST'>
      <input type='text' name='user' placeholder='Enter username'/><br><br>
      <input type='password' name='pwd' placeholder='Enter password'/><br><br>
      <input type='submit' value='Log In'>
    </form>
  </div>
</body>
</html>