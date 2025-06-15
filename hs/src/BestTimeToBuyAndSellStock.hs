module BestTimeToBuyAndSellStock where

maxProfit :: [Int] -> Int
maxProfit [] = 0
maxProfit (x : xs) = snd $ foldl' go (x, 0) xs
  where
    go :: (Int, Int) -> Int -> (Int, Int)
    go (!bestBuy, !bestProfit) num = (min num bestBuy, max (num - bestBuy) bestProfit)