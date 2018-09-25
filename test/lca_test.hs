module lca_test (spec) where

import           lca
import           Test.Hspec
import           Test.QuickCheck

spec :: Spec
spec = do
  describe "LCA Function" $ do

    it "returns 'Error' for empty tree" $ do
      (lca 1 3) ==  "Error" `shouldBe` True
