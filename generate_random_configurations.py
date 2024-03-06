import random

def random_position(world_size):
    x = random.randint(1, world_size + 1)
    y = random.randint(1, world_size + 1)
    return (x, y)

def generate_random_configurations():
    sample_size = 381  # 381+4(already existing caves cave0.jess ...) = 385
    world_size = 4
    max_pits = 13
    max_gold_amount = 100
    for n in range(sample_size):
        cave_number = n + 4  # because we already have 4 existing caves
        filename = f"cave{cave_number}.jess"
        with open(filename, 'w') as writer:
            writer.write(f"(deffacts caves\n (worldsize {world_size} {world_size})\n")
            wumpus_position = random_position(world_size)
            writer.write(f" (wumpus (x {wumpus_position[0]}) (y {wumpus_position[1]}))\n")
            
            random_number_pits = random.randint(1, max_pits + 1)
            print("random pit nbr:", random_number_pits)
            for i in range(random_number_pits):
                pit_position = random_position(world_size)
                if pit_position != wumpus_position:
                    writer.write(f" (pit (x {pit_position[0]}) (y {pit_position[1]}))\n")
            
            gold_position = random_position(world_size)
            gold_amount = random.randint(1, max_gold_amount + 1)
            writer.write(f" (gold (x {gold_position[0]}) (y {gold_position[1]}) (amount {gold_amount}))\n")
            
            writer.write(" (exit (x 1) (y 1))\n")
            writer.write(" (hunter (agent HAK)))\n")


generate_random_configurations()
