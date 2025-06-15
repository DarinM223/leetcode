module TwoSum where

import Control.Monad
import Data.IntMap qualified as IM

-- 2, 7, 11, 15 target = 9
-- Output: [0, 1]
-- Build map from
-- 2 -> 0
-- 7 -> 1
-- 11 -> 2
-- 15 -> 3

twoSum :: [Int] -> Int -> Maybe (Int, Int)
twoSum ls target = foldr go Nothing (zip ls [0 ..])
  where
    go :: (Int, Int) -> Maybe (Int, Int) -> Maybe (Int, Int)
    go _ (Just r) = Just r
    go (num, i) Nothing = do
      i' <- IM.lookup (target - num) mapping
      guard $ i /= i'
      pure $ if i' < i then (i', i) else (i, i')
    mapping = IM.fromList $ zip ls [0 ..]