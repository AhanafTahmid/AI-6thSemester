def food_supply_manager():
    storage_a = int(input("Enter Storage A packets: "))
    storage_b = int(input("Enter Storage B packets: "))

    shelter_needs = {
        "Shelter 1": int(input("Enter Shelter 1 need: ")),
        "Shelter 2": int(input("Enter Shelter 2 need: ")),
        "Shelter 3": int(input("Enter Shelter 3 need: "))
    }

    shelter_received = {
        "Shelter 1": 0,
        "Shelter 2": 0,
        "Shelter 3": 0
    }

    for shelter, need in shelter_needs.items():
        give = min(need, storage_a)
        storage_a -= give
        shelter_received[shelter] += give
        need -= give

        if need > 0:
            give = min(need, storage_b)
            storage_b -= give
            shelter_received[shelter] += give

    
    print("\n--- Distribution Report ---")
    for shelter in shelter_needs:
        received = shelter_received[shelter]
        print(shelter + " received " + str(received) + " packets")
        if received < shelter_needs[shelter]:
            print("WARNING: " + shelter + " did NOT receive all required packets!")

    print("\nRemaining in Storage A: " + str(storage_a) + " packets")
    print("Remaining in Storage B: " + str(storage_b) + " packets")


food_supply_manager()
