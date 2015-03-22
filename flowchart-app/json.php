<?php

/* Flowchart JSON data returner
 * Author Ando Roots 2011
*/

// Get the ID of the next question
if (isset($_GET['next_id']) && !empty($_GET['next_id'])) {
    $next_id = (int)$_GET['next_id'];
} else {
    $next_id = 1;
}

// Data to return
$data = array('id' => $next_id);


// Contains all the questions and answers
// $data['options'] is an array with numeric keys pointing to the next question id (the case number)
switch ($next_id) {
    case 1:
        $data['question'] = 'Are you right?';
        $data['options'] = array(2 => 'Yes');
    break;

    case 2:
        $data['question'] = 'Is he making a logical argument for his point of view?';
        $data['options'] = array(3 => 'Yes',
                                 4 => 'No');
    break;

        case 3:
            $data['question'] = 'Keep talking, without acknowledging what he\'s saying.';
            $data['options'] = array(2 => 'Okay');
        break;

    case 4:
        $data['question'] = 'Have you clearly made your point?';
        $data['options'] = array(5 => 'Yes',
                                 6 => 'No');
    break;

        case 5:
            $data['question'] = 'Are you late for something?';
            $data['options'] = array(7 => 'Yes',
                                     6 => 'No');
        break;
    
        case 6:
            $data['question'] = 'Repeat your point';
            $data['options'] = array(8 => 'Okay');
        break;

    case 7:
        $data['question'] = 'Tell him "Great, now I\'m late, we\'ll finish this later."';
        $data['options'] = array(999 => 'Nice, I won!');
    break;

    case 8:
        $data['question'] = 'Is he angry enough to break up with you?';
        $data['options'] = array(9 => 'Yes',
                                 4 => 'No');
    break;

    case 9:
        $data['question'] = 'Cry';
        $data['options'] = array(10 => 'Okay');
    break;

    case 10:
        $data['question'] = 'Is he still mad?';
        $data['options'] = array(9 => 'Yes',
                                 11 => 'No');
    break;

    case 11:
        $data['question'] = 'Have sex if he apologizes';
        $data['options'] = array(999 => 'Sweet, I won and had sex!');
    break;

    case 999:
        $data['question'] = 'The End';
        $data['options'] = array(1 => 'Back to the beginning');
    break;

    
    // This next_id is not defined, return error
    default:
        $data['question'] = 'Sorry, something went wrong...';
        $data['options'] = array(1 => 'To The Beginning');
    break;
}


die(json_encode($data));

?>