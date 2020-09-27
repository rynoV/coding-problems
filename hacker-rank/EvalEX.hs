-- https://www.hackerrank.com/challenges/eval-ex/problem
-- Estimates e^x
{-# LANGUAGE DuplicateRecordFields #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE UndecidableInstances #-}

module Main where

import Control.Monad
import Data.Array
import Data.Bits
import Data.List
import Debug.Trace
import System.Environment
import System.IO
import System.IO.Unsafe

fac n
  | n <= 1 = 1
  | otherwise = n * fac (n - 1)

eX x = foldr (\a b -> b + x ** a / fac a) 0 [0 .. 9]

main :: IO ()
main = do
  n <- readLn :: IO Int

  forM_ [1 .. n] $ \n_itr -> do
    x <- readLn :: IO Double
    print $ eX x
