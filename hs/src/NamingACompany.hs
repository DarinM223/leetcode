module NamingACompany where

import Control.Monad (guard)
import Data.Set qualified as S

distinctNames :: [String] -> Int
distinctNames ideas = length $ do
  name1 <- ideas
  name2 <- ideas
  guard $ name1 /= name2
  let (name1', name2') = case (name1, name2) of
        (ch1 : n1, ch2 : n2) -> (ch2 : n1, ch1 : n2)
        _ -> (name1, name2)
  guard $ not (S.member name1' ideasSet) && not (S.member name2' ideasSet)
  pure ()
  where
    ideasSet = S.fromList ideas