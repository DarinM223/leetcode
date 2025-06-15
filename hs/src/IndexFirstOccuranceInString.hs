module IndexFirstOccuranceInString where

import Data.List (mapAccumL)
import Data.Vector qualified as V

-- "sadbutsad" "sad" -> 0
-- "leetcode" "leeto" -> -1
-- "abcabababc" "ababc" -> 5
-- "" "" -> -1

-- | We want to build an aho corasick automaton, but since
-- we already have the transition table (the next character in the string)
-- and the success state table (is the index at the end of the string), we
-- only need to build the failure link table.
--
-- Step 1: Build the failure link table.
-- Step 2: Iterate over the haystack stepping through the automaton.
--
-- This algorithm is Knuth-Morris-Pratt which is a simplified version of Aho-Corasick.
-- Worst case time complexity for search is O(2n) -> O(n).
strStr :: String -> String -> Int
strStr haystack needle = go 0 $ zip [0 ..] haystack
  where
    go :: Int -> [(Int, Char)] -> Int
    go state ((i, ch) : rest)
      | needleVec V.! state == ch =
          if state == V.length needleVec - 1
            then i - V.length needleVec + 1
            else go (state + 1) rest
      | state == 0 = go state rest
      | otherwise = go (failure V.! (state - 1)) ((i, ch) : rest)
    go _ [] = -1

    failure :: V.Vector Int
    failure = V.fromList . snd $ mapAccumL calcFailureLink 0 [0 .. V.length needleVec - 1]

    calcFailureLink :: Int -> Int -> (Int, Int)
    calcFailureLink _ 0 = (0, 0)
    calcFailureLink prev0 i = goFailureLinks prev0
      where
        goFailureLinks prev
          | needleVec V.! prev == needleVec V.! i = (prev + 1, prev + 1)
          | prev == 0 = (prev, 0)
          | otherwise = goFailureLinks $ failure V.! (prev - 1)

    needleVec :: V.Vector Char
    needleVec = V.fromList needle