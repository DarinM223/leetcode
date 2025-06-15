module KthMissingPositiveNumber where

import Data.Vector qualified as V

findKthPositive :: [Int] -> Int -> Int
findKthPositive l k = go 0 (V.length arr)
  where
    go start end
      | start >= end =
          -- Number must be between arr[end - 1] and arr[end]:
          -- -> arr[end] - (# of missing numbers at end - k + 1)
          -- -> arr[end] - (arr[end] - end - 1 - k + 1)
          -- -> end + k
          end + k
      | arr V.! mid - mid - 1 < k =
          -- If there are no gaps, arr[mid] == mid
          -- arr[mid] - mid is the number of gaps
          -- If the number of gaps < k, then look into upper half
          go (mid + 1) end
      | otherwise = go start mid
      where
        mid = (start + end) `div` 2
    arr = V.fromList l