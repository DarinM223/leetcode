module AddBinary where

import Data.Char (chr, ord)

addBinary :: String -> String -> String
addBinary str1 str2 =
  case go str1' str2' of
    (0, l) -> l
    (carry, l) -> digitToChar carry : l
  where
    digitToChar :: Int -> Char
    digitToChar i = chr $ ord '0' + i

    go :: String -> String -> (Int, String)
    go (x : xs) (y : ys)
      | added > 1 = (1, digitToChar (added - 2) : rest)
      | otherwise = (0, digitToChar added : rest)
      where
        added = x' + y' + carry
        x' = ord x - ord '0'
        y' = ord y - ord '0'
        (carry, rest) = go xs ys
    go _ _ = (0, "")

    str1', str2' :: String
    (str1', str2')
      | str1Len < str2Len = (replicate (str2Len - str1Len) '0' ++ str1, str2)
      | str2Len < str1Len = (str1, replicate (str1Len - str2Len) '0' ++ str2)
      | otherwise = (str1, str2)

    str1Len, str2Len :: Int
    str1Len = length str1
    str2Len = length str2