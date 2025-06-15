module Sqrt where

-- | If a^2 > target then a > sqrt(target) and same with <.
-- Because of this we can do binary search of the squared value.
mySqrt :: Int -> Int
mySqrt target = go 0 0 target
  where
    go :: Int -> Int -> Int -> Int
    go lastSaved start end
      | end < start = lastSaved
      | mult > target = go lastSaved start (mid - 1) -- Don't save midpoints with squares greater than the target.
      | mult < target = go mid (mid + 1) end
      | otherwise = mid
      where
        mult = mid * mid
        mid = start + (end - start) `div` 2