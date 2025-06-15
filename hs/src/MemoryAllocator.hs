module MemoryAllocator where

import Control.Monad.State
import Prelude hiding (init)

data Block = Block
  { blockStartIdx :: Int,
    blockSize :: Int,
    blockMID :: Int
  }
  deriving (Show)

newtype MemoryAllocator = MemoryAllocator {blocks :: [Block]}
  deriving (Show)

-- | Starts off with one big empty block (mID == 0).
init :: Int -> MemoryAllocator
init n = MemoryAllocator [Block 0 n 0]

-- | Iterates through the blocks, if it finds an empty block with a bigger size,
-- it breaks up the block.
allocate :: Int -> Int -> MemoryAllocator -> (Int, MemoryAllocator)
allocate size mID MemoryAllocator {blocks} = MemoryAllocator <$> go blocks
  where
    go :: [Block] -> (Int, [Block])
    go (Block blockStart blockSize 0 : rest)
      | blockSize > size = (blockStart, Block blockStart size mID : Block (blockStart + size) (blockSize - size) 0 : rest)
      | blockSize == size = (blockStart, Block blockStart blockSize mID : rest)
    go (block : rest) = (block :) <$> go rest
    go [] = (-1, [])

-- | Iterates through the blocks, if it finds a block with the mID, it sets it
-- to an empty block. Then it goes through a compacting pass merging consecutive empty blocks.
freeMemory :: Int -> MemoryAllocator -> (Int, MemoryAllocator)
freeMemory mID MemoryAllocator {blocks} = MemoryAllocator . compact <$> go blocks
  where
    compact :: [Block] -> [Block]
    compact (Block start size1 0 : Block _ size2 0 : rest) = compact $ Block start (size1 + size2) 0 : rest
    compact (block : rest) = block : compact rest
    compact [] = []

    go :: [Block] -> (Int, [Block])
    go (Block blockStart blockSize mID' : rest)
      | mID == mID' = (numFreed + 1, Block blockStart blockSize 0 : blocks')
      | otherwise = (numFreed, Block blockStart blockSize mID' : blocks')
      where
        (numFreed, blocks') = go rest
    go [] = (0, [])

test :: IO ()
test = flip evalStateT (init 10) $ do
  r1 <- state $ allocate 1 1
  lift $ print r1
  r2 <- state $ allocate 1 2
  lift $ print r2
  r3 <- state $ allocate 1 3
  lift $ print r3
  r4 <- state $ freeMemory 2
  lift $ print r4
  r5 <- state $ allocate 3 4
  lift $ print r5
  r6 <- state $ allocate 1 1
  lift $ print r6
  r7 <- state $ allocate 1 1
  lift $ print r7
  r8 <- state $ freeMemory 1
  get >>= lift . print -- Check if state is properly compacted
  lift $ print r8
  r9 <- state $ allocate 10 2
  lift $ print r9
  r10 <- state $ freeMemory 7
  lift $ print r10