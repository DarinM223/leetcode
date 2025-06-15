module SmallestValueOfRearrangedNumber where

import Data.List (sort)

-- 310 -> 103
-- -7605 -> -7650
-- 95005 -> 50059
-- 0 -> 0

smallestValue :: Int -> Int
smallestValue num0
  | num0 <= 0 = -foldl' (\acc digit -> acc * 10 + digit) 0 (reverse digits)
  | otherwise = foldl' (\acc digit -> acc * 10 + digit) 0 $ swapNonZeroDigit digits
  where
    swapNonZeroDigit :: [Int] -> [Int]
    swapNonZeroDigit l
      | _ : rest <- top, ch : rest' <- nonZero = ch : rest ++ 0 : rest'
      | otherwise = l
      where
        top = takeWhile (== 0) l
        nonZero = dropWhile (== 0) l
    digits = sort . buildDigits [] $ abs num0
    buildDigits acc 0 = acc
    buildDigits acc num = buildDigits (num `mod` 10 : acc) (num `div` 10)