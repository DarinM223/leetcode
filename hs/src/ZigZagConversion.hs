module ZigZagConversion where

import Data.IntMap qualified as IM

convert :: String -> Int -> String
convert s numRows
  | numRows == 1 || numRows >= length s = s -- Need to handle this case!
  | otherwise = buildString $ foldl' go (False, 1, initRows) s
  where
    initRows = IM.fromList $ fmap (,[]) [1 .. numRows]
    buildString (_, _, rows) = mconcat . fmap (reverse . snd) $ IM.toList rows
    go :: (Bool, Int, IM.IntMap String) -> Char -> (Bool, Int, IM.IntMap String)
    go (!goingDown, !currRow, !rows) ch = (goingDown', currRow', rows')
      where
        rows' = IM.adjust (ch :) currRow rows
        goingDown' = if currRow == numRows || currRow == 1 then not goingDown else goingDown
        currRow'
          | goingDown' = currRow + 1
          | otherwise = currRow - 1