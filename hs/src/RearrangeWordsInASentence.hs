module RearrangeWordsInASentence where

import Data.Char (toLower, toUpper)
import Data.List (sortBy)
import Data.Ord (comparing)

arrangeWords :: String -> String
arrangeWords = unwords . rewriteWords . sortBy (comparing length) . words
  where
    rewriteWords :: [String] -> [String]
    rewriteWords [] = []
    rewriteWords (x : xs) = modifyHead toUpper x : fmap (modifyHead toLower) xs

    modifyHead :: (Char -> Char) -> String -> String
    modifyHead _ "" = ""
    modifyHead f (c : cs) = f c : cs