module SplitWithMinimumSum where

import Data.List (sort)

splitNum :: Int -> Int
splitNum num0 = (\(_, num1, num2) -> num1 + num2) $ foldl' go (True, 0, 0) digits
  where
    go :: (Bool, Int, Int) -> Int -> (Bool, Int, Int)
    go (!addToNum1, !num1, !num2) digit
      | addToNum1 = (not addToNum1, num1 * 10 + digit, num2)
      | otherwise = (not addToNum1, num1, num2 * 10 + digit)

    digits = sort $ buildDigits [] num0
    buildDigits acc num
      | num > 0 = buildDigits (num `mod` 10 : acc) (num `div` 10)
      | otherwise = acc