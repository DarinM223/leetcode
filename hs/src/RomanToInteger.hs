module RomanToInteger where

-- I -> 1
-- V -> 5
-- X -> 10
-- L -> 50
-- C -> 100
-- D -> 500
-- M -> 1000

-- IV -> 4
-- IX -> 9

-- XL -> 40
-- XC -> 90

-- CD -> 400
-- CM -> 900

-- "III"
-- 3

-- "LVIII"
-- 58

romanToInt :: String -> Int
romanToInt s = snd $ foldl' go (Nothing, 0) s
  where
    go (!prev, !acc) ch = (Just ch, acc + increment)
      where
        increment :: Int
        increment =
          case (prev, ch) of
            (Just 'I', 'V') -> 3
            (Just 'I', 'X') -> 8
            (Just 'X', 'L') -> 30
            (Just 'X', 'C') -> 80
            (Just 'C', 'D') -> 300
            (Just 'C', 'M') -> 800
            (_, 'I') -> 1
            (_, 'V') -> 5
            (_, 'X') -> 10
            (_, 'L') -> 50
            (_, 'C') -> 100
            (_, 'D') -> 500
            (_, 'M') -> 1000
            _ -> error "Invalid character"