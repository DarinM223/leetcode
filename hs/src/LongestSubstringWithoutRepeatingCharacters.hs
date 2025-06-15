module LongestSubstringWithoutRepeatingCharacters where

import Data.Map qualified as M

-- | Use sliding window approach. We only need to track the start
-- index of the current substring. The length of the current substring
-- at any point in time is the current index of the character - start index.
-- We have to check again when we hit the end of the string also.
--
-- The main question is how to check if a character is
-- in the current substring while the substring is sliding?
-- We don't want to have to shift the map's keys whenever we hit
-- a duplicated character.
--
-- The answer is to make a map of character to the character's index
-- and only accept lookups if the mapped index is greater than the
-- current start. This means that the map can contain more elements
-- than the current substring but they will be ignored if their index
-- is too low.
lengthOfLongestSubstring :: String -> Int
lengthOfLongestSubstring s0 =
  (\(currMax, start, _) -> max currMax (length s0 - start))
    . foldl' go (0, 0, M.empty)
    $ zip [0 ..] s0
  where
    go :: (Int, Int, M.Map Char Int) -> (Int, Char) -> (Int, Int, M.Map Char Int)
    go (!currMax, !start, !dict) (i, ch) =
      case M.lookup ch dict of
        Just start' | start' >= start -> (max currMax (i - start), start' + 1, dict')
        _ -> (currMax, start, dict')
      where
        dict' = M.insert ch i dict