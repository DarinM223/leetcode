module LongestConsecutiveSequence where

import Data.IntMap qualified as IM
import Data.Set qualified as S

-- | This is nlogn instead of n because looking up in a set or map is logn instead of 1.
longestConsecutive :: [Int] -> Int
longestConsecutive [] = 0
longestConsecutive ls = maximum arr
  where
    go :: Int -> Int
    go num
      | S.member (num - 1) set = arr IM.! (num - 1) + 1
      | otherwise = 1
    arr = IM.fromList [(num, go num) | num <- ls]
    set = S.fromList ls