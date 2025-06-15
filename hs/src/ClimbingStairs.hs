module ClimbingStairs where

import Data.Vector qualified as V

climbStairs :: Int -> Int
climbStairs n = table V.! 0
  where
    go :: Int -> Int
    go i
      | i < n - 1 = table V.! (i + 1) + table V.! (i + 2)
      | i < n = table V.! (i + 1)
      | otherwise = 1
    table :: V.Vector Int
    table = V.fromList $ fmap go [0 .. n]