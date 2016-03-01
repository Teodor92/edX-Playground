-- Exercise 1
n = a `div` length xs
   where a = 10
         xs = [1, 2, 3, 4, 5]
         
         
-- Exercise 2

last xs = head (drop (length xs - 1) xs)

last xs = xs !! (length xs - 1)

last xs = head (reverse xs)

-- Exercise 3

init xs = reverse (tail (reverse xs))

-- Exercise 7

qsort [] = []
qsort (x:xs) = qsort larger ++ [x] ++ qsort smaller
    where smaller = [a | a <- xs, a <= x]
          larger = [b | b <- xs, b > x]
          
qsort [] = []
qsort (x:xs) = qsort larger ++ [x] ++ qsort smaller
    where larger = [a | a <- xs, a > x || a == x]
          smaller = [b | b <- xs, b < x]
          
qsort [] = []
qsort (x:xs)
  = reverse
        (reverse (qsort smaller) ++ [x] ++ reverse (qsort larger))
  where smaller = [a | a <- xs, a <= x]
        larger = [b | b <- xs, b > x]
        
