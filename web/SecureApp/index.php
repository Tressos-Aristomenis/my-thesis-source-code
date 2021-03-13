<?php
  $is_admin = 0;

  if (isset($_GET['ct'])) {
    session_start();

    $key = $_SESSION['key'];
    $iv  = $_SESSION['iv'];
    $ciphertext = hex2bin($_GET['ct']);

    $plaintext = openssl_decrypt($ciphertext, 'AES-128-CBC', $key, OPENSSL_RAW_DATA, $iv);

    if (str_contains($plaintext, '&is_admin=1&username=')) {
      $is_admin = 1;
      //session_destroy();
    }
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
<body>
  <?php
    if ($is_admin) {
      echo '<h1>You are logged in as an administrator!</h1>';
      include 'secret.php';
      echo '<h2>Here\'s the secret : ' . $secret . '</h2>';
    } else {
      echo '<h1>You are logged in as a user!</h1>';
    }
  ?>
</body>
</html>