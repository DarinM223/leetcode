{-# OPTIONS_GHC -Wno-x-partial #-}

module LongestCommonPrefix where

import Data.List

longestCommonPrefix :: [String] -> String
longestCommonPrefix strs
  | any null strs = ""
  | [ch] <- nub (fmap head strs) = ch : longestCommonPrefix (fmap tail strs)
  | otherwise = ""