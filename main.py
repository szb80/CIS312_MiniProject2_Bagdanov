# CIS312 Final Project
# Created by Seth Bagdanov 2/7/2017
# Calculates and displays a recipe based on the batch size

# Welcome message
print("CIS312 Cookie Recipe Calculator")

# Set minimum for regular batch to become bulk batch
bulkBatchSizeMin = 96

# Set base quantity variables for standard batch
standardBatch = 24  # base recipe size

numGSaltedButter = 150.0 / standardBatch
numGBrownSugar = 80.0 / standardBatch
numGWhiteSugar = 80.0 / standardBatch
numTspVanilla = 2.0 / standardBatch
numEaEgg = 1.0 / standardBatch
numGWhiteFlour = 225.0 / standardBatch
numTspBakingSoda = 0.25 / standardBatch
numTspSalt = 0.25 / standardBatch
numGChocolateChip = 200 / standardBatch

# Set regular pricing variables for items
unitCostSaltedButter = 0.006158940397
unitCostBrownSugar = 0.002560706402
unitCostWhiteSugar = 0.001719955899
unitCostVanilla = 0.406666666667
unitCostEgg = 0.131666666667
unitCostWhiteFlour = 0.001128747795
unitCostBakingSoda = 0.002202643172
unitCostSalt = 0.005384615385
unitCostChocolateChip = 0.008058823529

# Set bulk pricing variables for items
unitBulkCostSaltedButter = 0.006158940397
unitBulkCostBrownSugar = 0.002560706402
unitBulkCostWhiteSugar = 0.001719955899
unitBulkCostVanilla = 0.034192708333
unitBulkCostEgg = 0.131666666667
unitBulkCostWhiteFlour = 0.001128747795
unitBulkCostBakingSoda = 0.001902149950
unitBulkCostSalt = 0.000997372088
unitBulkCostChocolateChip = 0.005703804300

# Take input from user as to how many cookies
batchSize = int(input('Please enter the batch quantity:  '))

print("\nYour batch instructions are as follows: ")
# Determine batch size, regular or bulk

# Size is under min, proceed with regular pricing
if batchSize < bulkBatchSizeMin:
    print("      COST   QUANTITY   ITEM")  # table header
    # Salted Butter
    print("{:10.2f}".format(unitCostSaltedButter * batchSize * numGSaltedButter), \
          "{:10.2f}".format(numGSaltedButter * batchSize), \
          '  Salted Butter')
    # Brown Sugar
    print("{:10.2f}".format(unitCostBrownSugar * batchSize * numGBrownSugar), \
          "{:10.2f}".format(numGBrownSugar * batchSize), \
          '  Brown Sugar')
    # White Sugar
    print("{:10.2f}".format(unitCostWhiteSugar * batchSize * numGWhiteSugar), \
          "{:10.2f}".format(numGWhiteSugar * batchSize), \
          '  White Sugar')
    # Vanilla
    print("{:10.2f}".format(unitCostVanilla * batchSize * numTspVanilla), \
          "{:10.2f}".format(numTspVanilla * batchSize), \
          '  Vanilla')
    # Egg
    print("{:10.2f}".format(unitCostEgg * batchSize * numEaEgg), \
          "{:10.2f}".format(numEaEgg * batchSize), \
          '  Eggs')
    # White Flour
    print("{:10.2f}".format(unitCostWhiteFlour * batchSize * numGWhiteFlour), \
          "{:10.2f}".format(numGWhiteFlour * batchSize), \
          '  White Flour')
    # Baking Soda
    print("{:10.2f}".format(unitCostBakingSoda * batchSize * numTspBakingSoda), \
          "{:10.2f}".format(numTspBakingSoda * batchSize), \
          '  Baking Soda')
    # Salt
    print("{:10.2f}".format(unitCostSalt * batchSize * numTspSalt), \
          "{:10.2f}".format(numTspSalt * batchSize), \
          '  Salt')
    # Chocolate Chip
    print("{:10.2f}".format(unitCostChocolateChip * batchSize * numGChocolateChip), \
          "{:10.2f}".format(numGChocolateChip * batchSize), \
          '  Chocolate Chips')


# Size is over minimum, use bulk pricing
elif batchSize >= bulkBatchSizeMin:
    print("      COST   QUANTITY   ITEM")  # table header
    # Salted Butter
    print("{:10.2f}".format(unitBulkCostSaltedButter * batchSize * numGSaltedButter), \
          "{:10.2f}".format(numGSaltedButter * batchSize), \
          '  Salted Butter')
    # Brown Sugar
    print("{:10.2f}".format(unitBulkCostBrownSugar * batchSize * numGBrownSugar), \
          "{:10.2f}".format(numGBrownSugar * batchSize), \
          '  Brown Sugar')
    # White Sugar
    print("{:10.2f}".format(unitBulkCostWhiteSugar * batchSize * numGWhiteSugar), \
          "{:10.2f}".format(numGWhiteSugar * batchSize), \
          '  White Sugar')
    # Vanilla
    print("{:10.2f}".format(unitBulkCostVanilla * batchSize * numTspVanilla), \
          "{:10.2f}".format(numTspVanilla * batchSize), \
          '  Vanilla')
    # Egg
    print("{:10.2f}".format(unitBulkCostEgg * batchSize * numEaEgg), \
          "{:10.2f}".format(numEaEgg * batchSize), \
          '  Eggs')
    # White Flour
    print("{:10.2f}".format(unitBulkCostWhiteFlour * batchSize * numGWhiteFlour), \
          "{:10.2f}".format(numGWhiteFlour * batchSize), \
          '  White Flour')
    # Baking Soda
    print("{:10.2f}".format(unitBulkCostBakingSoda * batchSize * numTspBakingSoda), \
          "{:10.2f}".format(numTspBakingSoda * batchSize), \
          '  Baking Soda')
    # Salt
    print("{:10.2f}".format(unitBulkCostSalt * batchSize * numTspSalt), \
          "{:10.2f}".format(numTspSalt * batchSize), \
          '  Salt')
    # Chocolate Chip
    print("{:10.2f}".format(unitBulkCostChocolateChip * batchSize * numGChocolateChip), \
          "{:10.2f}".format(numGChocolateChip * batchSize), \
          '  Chocolate Chips')

else:
    print("I'm sorry, you cannot make that many cookies!")
