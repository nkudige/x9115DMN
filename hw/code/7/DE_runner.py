from DE import DE

for model in ["Golinski", "Schaffer", "Kursawe", "Osyczka"]:
    de = DE(model)
    print "Running DE for " + model + "with 33% elite sampling"
    de.run(s=0.33)
    print "Running DE for " + model + "with 50% elite sampling"
    de = DE(model)
    de.run(s=0.50)
    print "Running DE for " + model + "with 70% elite sampling"
    de = DE(model)
    de.run(s=0.70)
    print "Running DE for " + model + "with 100% elite sampling"
    de = DE(model)
    de.run(s=1)