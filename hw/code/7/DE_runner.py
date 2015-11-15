from DE import DE

de = DE("Golinski")
print "Running DE with 33% elite sampling"
de.run(s=0.33)
print "Running DE with 50% elite sampling"
de = DE("Golinski")
de.run(s=0.50)
print "Running DE with 70% elite sampling"
de = DE("Golinski")
de.run(s=0.70)
print "Running DE with 100% elite sampling"
de = DE("Golinski")
de.run(s=1)