<?php
class Solution {
    public function calPoints($ops) {
        $baseballscore = [];

        foreach ($ops as $op) {
            if ($op === 'C') {
                array_pop($baseballscore);
            } elseif ($op === 'D') {
                $baseballscore[] = 2 * end($baseballscore);
            } elseif ($op === '+') {
                $baseballscore[] = end($baseballscore) + $baseballscore[count($baseballscore) - 2];
            } else {
                $baseballscore[] = intval($op);
            }
        }

        return array_sum($baseballscore);
    }
}

// Read inputs
$ops = explode(' ', readline());

// Solution
$solution = new Solution();
$output = $solution->calPoints($ops);

// Print the output
echo "Final Score: " . $output . PHP_EOL;
?>

<?php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $stack = [];
        $map = array(
            ')' => '(',
            '}' => '{',
            ']' => '['
        );
        
        for ($i = 0; $i < strlen($s); $i++) {
            $char = $s[$i];
            if (array_key_exists($char, $map)) {
                $topElement = empty($stack) ? '#' : array_pop($stack);
                if ($topElement != $map[$char]) {
                    return false;
                }
            } else {
                array_push($stack, $char);
            }
        }
        
        return empty($stack);
    }
}

// Test cases
$solution = new Solution();
echo $solution->isValid("()[]{}"); // Should return true
?>