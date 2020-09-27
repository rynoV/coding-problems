-- Reverse with concats
rev :: [a] -> [a]
rev (x : []) = [x]
rev (x : xs) = rev xs ++ [x]

-- Reverse with just appends
rev2 :: [a] -> [a]
rev2 (x : xs) = h xs [x]
  where
    h :: [a] -> [a] -> [a]
    h (x : []) = (x :)
    h (x : xs) = (h xs) . (x :)