<?php

define('COMMAND_FILE', 'commands.txt');

if ($_GET['acknowledge'] == 'yes') {
    acknowledge_command();
    die('OK');
} elseif (isset($_GET['message'])) {
    die(write_command($_GET['message']));
} else {
    die(get_command());
}


function write_command($cmd) {
    $fh = fopen(COMMAND_FILE, 'w+') or die("can't open file");
    $cmd = str_replace('<?', '', $cmd);
    fwrite($fh, $cmd);
    fclose($fh);
    return 'OK';
}

function get_command() {
    if (file_exists(COMMAND_FILE)) {
        return file_get_contents(COMMAND_FILE);
    } else {
        return '';
    }
}

function acknowledge_command() {
    $fh = fopen(COMMAND_FILE, 'w+') or die("can't open file");
    $stringData = '';
    fwrite($fh, $stringData);
    fclose($fh);
}