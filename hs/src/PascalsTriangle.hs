{-# OPTIONS_GHC -Wno-x-partial #-}

module PascalsTriangle where

generate :: Int -> [[Int]]
generate n
  | n <= 0 = []
  | otherwise = scanl go [1] [1 .. n - 1]
  where
    go :: [Int] -> Int -> [Int]
    go prev _ = 1 : fmap (uncurry (+)) (zip prev (tail prev)) ++ [1]