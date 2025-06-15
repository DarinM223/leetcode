module SearchInsertPosition where

import Data.Vector qualified as V

searchInsert :: V.Vector Int -> Int -> Int
searchInsert array target
  | V.null array = 0
  | otherwise = go 0 (V.length array)
  where
    go :: Int -> Int -> Int
    go start end
      | target == array V.! mid = mid
      | target > array V.! mid = if start == mid then start + 1 else go mid end
      | end == mid = if end - 1 < 0 then 0 else end - 1
      | otherwise = go start mid
      where
        mid = (start + end) `div` 2