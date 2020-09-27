sumOdd :: Integral a => [a] -> a
sumOdd = sum . filter odd

sumOdd2 :: Integral a => [a] -> a
sumOdd2 = foldr (+) 0 . filter odd
