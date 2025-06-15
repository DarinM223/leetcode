module MaskingPersonalInformation where

import Data.Char (toLower)
import Data.List (intercalate)
import Data.List.Split (splitOn)

maskPII :: String -> String
maskPII s
  | '@' `elem` s = maskEmail s
  | otherwise = maskPhoneNumber s

maskEmail :: String -> String
maskEmail email
  | ((hd : name) : rest) <- substrings = mconcat . fmap (fmap toLower) $ (hd : "*****" ++ [last (hd : name)]) : rest
  | otherwise = error "Invalid email"
  where
    substrings = splitOn "@" email

maskPhoneNumber :: String -> String
maskPhoneNumber phoneNum = intercalate "-" $ if totalDigits > 10 then countryCode : phoneNum' else phoneNum'
  where
    phoneNum' = ["***", "****", lastDigits]
    countryCode = '+' : replicate (totalDigits - 10) '*'
    (totalDigits, lastDigits) = foldr go (0, "") phoneNum
    go :: Char -> (Int, String) -> (Int, String)
    go ch (totalDigits', lastDigits')
      | ch `elem` ['+', '-', '(', ')', ' '] = (totalDigits', lastDigits')
      | length lastDigits' < 4 = (totalDigits' + 1, ch : lastDigits')
      | otherwise = (totalDigits' + 1, lastDigits')