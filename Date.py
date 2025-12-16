import random
girls = ["sara","asma","samin","mina","avin","samane","taranom","tahora","tamana","mobina"]
boys = ["sina","saman","mohsen","mahdi","milad","ali","omid","sajad","majid","mmd"]
days = 60
interval = 5
print(" Random date program every 5 days\n ")
print("=" * 40)
for day in range(0, days , interval):
    print(f"\n Day {day} : ")
    selectedgirl = random.choice(girls)
    selectedboy = random.choice(boys)
    print(f" Day {day} : {selectedgirl}-{selectedboy}")
    print("="*40)
    print(f"in total, {days // interval} dates were set in {days} days . ")