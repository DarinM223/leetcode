module KthSmallestSumMatrixSortedRows where

import Data.List (sort)

kthSmallest :: [[Int]] -> Int -> Int
kthSmallest [] _ = error "empty matrix"
kthSmallest (sums : rest) k = foldl' go sums rest !! (k - 1)
  where
    go :: [Int] -> [Int] -> [Int]
    go acc row = take k $ sort [s + r | s <- acc, r <- row]