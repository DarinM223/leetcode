module PlusOne where

plusOne :: [Int] -> [Int]
plusOne digits0 =
  case go digits0 of
    (0, l) -> l
    (i, l) -> i : l
  where
    go :: [Int] -> (Int, [Int])
    go [] = (1, [])
    go (x : xs)
      | x + carry > 9 = (x + carry - 9, 0 : rest)
      | otherwise = (0, (x + carry) : rest)
      where
        (carry, rest) = go xs