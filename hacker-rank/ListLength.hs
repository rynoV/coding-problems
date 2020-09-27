len :: [a] -> Int
len = foldr (\_ a -> a + 1) 0

len2 :: [a] -> Int
len2 [] = 0
len2 (x:xs) = len2 xs + 1
