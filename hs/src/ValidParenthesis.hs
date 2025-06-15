module ValidParenthesis where

-- "()" True
-- "()[]{}" True
-- "(]" False
-- "([])" True
-- "([)]" False

validParenthesis :: String -> Bool
validParenthesis = go []
  where
    go :: [Char] -> String -> Bool
    go stack ('(' : rest) = go (')' : stack) rest
    go stack ('[' : rest) = go (']' : stack) rest
    go stack ('{' : rest) = go ('}' : stack) rest
    go (ch : stack) (ch' : rest) = ch == ch' && go stack rest
    go [] [] = True
    go _ _ = False
