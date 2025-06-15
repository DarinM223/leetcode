module MinimumCoinsForFruits where

import Data.Array qualified as A
import Data.Vector qualified as V

-- | O(n^2) DP solution there is a O(n) solution using a deque.
minimumCoins :: [Int] -> Int
minimumCoins prices = arr A.! (0, 0)
  where
    go ::
      -- The index of the current fruit.
      Int ->
      -- The number of free fruits that can be taken at this time.
      Int ->
      -- The minimum number of coins to acquire the fruits at this point.
      Int
    go i _ | i >= V.length prices' = 0
    go i 0 = prices' V.! i + arr A.! (i + 1, i + 1)
    go i n = min (prices' V.! i + arr A.! (i + 1, i + 1)) (arr A.! (i + 1, n - 1))

    arr :: A.Array (Int, Int) Int
    arr = A.array ((0, 0), (V.length prices', V.length prices' + 1)) [((i, typ), go i typ) | i <- A.range (0, V.length prices'), typ <- A.range (0, V.length prices' + 1)]
    prices' = V.fromList prices