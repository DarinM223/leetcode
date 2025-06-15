module FindDuplicateNumber where

import Data.Vector qualified as V

-- | Similar to finding a cycle in a linked list.
-- Each number in the array is an index into the array for the next node.
-- To find intersection, have one pointer going one step and another one going
-- two steps. If they meet then there is a cycle.
-- Then find the start of the cycle by putting the slow pointer back to the
-- beginning and stepping both of them one at a time until they meet.
findDuplicate :: V.Vector Int -> Int
findDuplicate arr = findCycleStart slow0 $ findIntersection slow0 fast0
  where
    findCycleStart :: Int -> Int -> Int
    findCycleStart slow fast
      | slow == fast = slow
      | otherwise = findCycleStart (arr V.! slow) (arr V.! fast)

    findIntersection :: Int -> Int -> Int
    findIntersection slow fast
      | slow' == fast' = fast'
      | otherwise = findIntersection slow' fast'
      where
        slow' = arr V.! slow
        fast' = arr V.! (arr V.! fast)

    (slow0, fast0) = (arr V.! 0, arr V.! 0)