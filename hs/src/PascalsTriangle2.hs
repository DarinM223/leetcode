{-# OPTIONS_GHC -Wno-x-partial #-}

module PascalsTriangle2 where

getRow :: Int -> [Int]
getRow row = foldl' go [1] [0 .. row - 1]
  where
    go :: [Int] -> Int -> [Int]
    go prev _ = 1 : fmap (uncurry (+)) (zip prev (tail prev)) ++ [1]