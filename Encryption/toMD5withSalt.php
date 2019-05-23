<?php

$salt = 'jirlaogbfj';
// print(mb_detect_encoding($salt));
// input
while ($line = fgets(STDIN)) {
   $text[] = trim($line);
}

$num = count($text);
for ($i = 0; $i < $num; $i++) {
    //print "$text[$i]¥n";
    $salt_text = $text[$i].$salt;
    $hash_text = hash('md5', $salt_text);
    echo $hash_text."\n";
}
?>