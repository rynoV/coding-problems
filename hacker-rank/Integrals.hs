-- https://www.hackerrank.com/challenges/area-under-curves-and-volume-of-revolving-a-curv/problem
-- Estimates area under a curve and volume after rotation around the x-axis
import Text.Printf (printf)

solve :: Int -> Int -> [Int] -> [Int] -> [Double]
solve l r a b = [integral poly, pi * integral (\ci -> (poly ci) ** 2)]
  where
    deltaX = 0.001
    ld = fromIntegral l
    rd = fromIntegral r
    c = [ld + deltaX, ld + (2 * deltaX) .. rd]
    integral f = foldr (\ci b -> b + (f ci) * deltaX) 0 c
    poly :: Double -> Double
    poly x = sum $ map calcTerm $ zip a b
      where
        calcTerm (ai, bi) = (fromIntegral ai) * (x ** fromIntegral bi)

main :: IO ()
main = getContents >>= mapM_ (printf "%.1f\n") . (\[a, b, [l, r]] -> solve l r a b) . map (map read . words) . lines