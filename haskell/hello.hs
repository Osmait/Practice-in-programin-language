module Main where

dobleSmallNumber x =
  if x > 100
    then x
    else x * 2

main :: IO ()
main = do
  let result = dobleSmallNumber 10
  print result
