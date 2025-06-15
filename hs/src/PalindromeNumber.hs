module PalindromeNumber where

-- x = 121 -> True
-- x = -121 -> False
-- x = 10 -> False
palindromeNumber :: Int -> Bool
palindromeNumber num0
  | num0 < 0 = False
  | otherwise =
      -- Easy way is to do `show num == reverse (show num)`
      go 1 (countDigits num0) num0
  where
    go begin end num
      | begin >= end = True
      | otherwise = endNum == beginNum && go (begin + 1) (end - 1) num
      where
        endNum = indexNum num (end - 1)
        beginNum = indexNum num (begin - 1)
    indexNum num i = num `div` (10 ^ i) `mod` 10

countDigits :: Int -> Int
countDigits n0 = if n0 == 0 then 1 else go 0 (abs n0)
  where
    go !acc n
      | n == 0 = acc
      | otherwise = go (acc + 1) (n `div` 10)
