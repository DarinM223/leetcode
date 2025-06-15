module LengthOfLastWord where

import Data.Vector qualified as V

lengthOfLastWord :: String -> Int
lengthOfLastWord str = go 0 (V.length strVec - 1)
  where
    go :: Int -> Int -> Int
    go !acc i
      | i < 0 = acc
      | strVec V.! i == ' ' = if acc > 0 then acc else go acc (i - 1)
      | otherwise = go (acc + 1) (i - 1)
    strVec = V.fromList str