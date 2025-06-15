module MergeTwoSortedLists where

-- [1, 3, 5] [2, 3, 6] -> [1, 2, 3, 3, 5, 6]
-- [] [] -> []
-- [] [0] -> [0]

mergeTwoLists :: [Int] -> [Int] -> [Int]
mergeTwoLists [] [] = []
mergeTwoLists [] l = l
mergeTwoLists l [] = l
mergeTwoLists (x : xs) (y : ys)
  | x < y = x : mergeTwoLists xs (y : ys)
  | otherwise = y : mergeTwoLists (x : xs) ys