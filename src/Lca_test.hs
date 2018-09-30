module Lca_test where

import           Lca
import           Test.Hspec


main :: IO ()
main =  hspec $ do
  describe "LCA Function" $ do

    it "returns 1 for LCA 1 and 3" $ do
      (lca_show myTree 1 3) == "1" `shouldBe` True

    it "returns 1 for LCA 4 and 5" $ do
      (lca_show myTree 4 5) == "2" `shouldBe` True
